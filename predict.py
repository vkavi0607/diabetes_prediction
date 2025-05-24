import streamlit as st
import pandas as pd
import time
from data_loader import load_data
from data_cleaner import clean_data
from model_trainer import train_model
from suggestions import generate_suggestions

# Set page configuration to hide default sidebar menu
st.set_page_config(page_title="Predict - Diabetes Prediction App", layout="wide")

# Custom CSS for enhanced UI
st.markdown("""
    <style>
    .main {
        background-color: #000000;
        padding: 20px;
        font-family: 'Roboto', sans-serif;
        color: #ffffff;
    }
    .stButton>button {
        background: linear-gradient(90deg, #007bff, #0056b3);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 12px 24px;
        font-size: 1.1em;
        font-weight: 500;
        transition: transform 0.2s, box-shadow 0.2s;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #0056b3, #003d82);
        transform: translateY(-2px);
        box-shadow: 0 4px 10px rgba(0, 123, 255, 0.3);
    }
    .stButton>button.explore-btn {
        background: linear-gradient(90deg, #28a745, #218838);
    }
    .stButton>button.explore-btn:hover {
        background: linear-gradient(90deg, #218838, #1a6b30);
    }
    h1, h2, h3 {
        color: #ffffff;
        font-weight: 500;
    }
    .stTextInput, .stNumberInput {
        background-color: #1a1a1a;
        border-radius: 8px;
        padding: 10px;
        color: #ffffff;
        border: 1px solid #333333;
    }
    .stTextInput>label, .stNumberInput>label {
        color: #d1d1d1;
        font-weight: 500;
    }
    .form-container {
        background-color: #1a1a1a;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
    }
    .sidebar .sidebar-content {
        background-color: #1a1a1a;
        color: #ffffff;
        padding: 20px;
    }
    .sidebar .stButton>button {
        background-color: #28a745;
        border-radius: 8px;
        width: 100%;
        margin-bottom: 10px;
        font-size: 1em;
    }
    .sidebar .stButton>button:hover {
        background-color: #218838;
    }
    .sidebar .stButton>button.active {
        background-color: #007bff;
        font-weight: 600;
    }
    .expander-content {
        background-color: #1a1a1a;
        padding: 15px;
        border-radius: 8px;
        color: #d1d1d1;
    }
    .footer {
        text-align: center;
        padding: 20px;
        background-color: #1a1a1a;
        color: #d1d1d1;
        border-radius: 10px;
        margin-top: 30px;
        font-size: 0.9em;
    }
    .footer a {
        color: #007bff;
        text-decoration: none;
    }
    .footer a:hover {
        text-decoration: underline;
    }
    </style>
""", unsafe_allow_html=True)

def main():
    # Custom sidebar with navigation
    with st.sidebar:
        st.markdown("<h2 style='color: #ffffff;'>Navigation</h2>", unsafe_allow_html=True)
        if st.button("🏠 Home", key="nav_home"):
            st.switch_page("home.py")
        if st.button("🔍 Predict", key="nav_predict", disabled=True):  # Disabled to indicate active page
            pass
        if st.button("📊 Explore", key="nav_explore"):
            st.switch_page("pages/explore.py")

    st.title("Predict Your Diabetes Risk")
    st.markdown("Enter your health metrics to receive a personalized diabetes risk prediction and actionable recommendations.")

    # Load and prepare data
    data = load_data()
    if data is None:
        st.error("Failed to load data. Please try again later.")
        return
    
    data = clean_data(data)
    X = data.drop('Outcome', axis=1)
    y = data['Outcome']
    
    # Train model
    try:
        model, scaler, _, _, _, _, _ = train_model(X, y)
    except Exception as e:
        st.error(f"Error training model: {e}")
        return
    
    # Input form
    st.header("Health Metrics")
    with st.container():
        st.markdown("<div class='form-container'>", unsafe_allow_html=True)
        with st.form(key="diabetes_form"):
            col1, col2 = st.columns(2)
            with col1:
                pregnancies = st.number_input("Pregnancies", min_value=0, max_value=17, value=1, step=1)
                glucose = st.number_input("Glucose (mg/dL)", min_value=0, max_value=200, value=120, step=1)
                blood_pressure = st.number_input("Blood Pressure (mm Hg)", min_value=0, max_value=140, value=70, step=1)
                skin_thickness = st.number_input("Skin Thickness (mm)", min_value=0, max_value=99, value=20, step=1)
            with col2:
                insulin = st.number_input("Insulin (mu U/ml)", min_value=0, max_value=846, value=79, step=1)
                bmi = st.number_input("BMI", min_value=0.0, max_value=67.1, value=32.0, step=0.1)
                dpf = st.number_input("Diabetes Pedigree Function", min_value=0.078, max_value=2.42, value=0.3725, step=0.001)
                age = st.number_input("Age", min_value=21, max_value=81, value=30, step=1)
            
            submit_button = st.form_submit_button(label="Predict Risk")
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Explore Data button (outside form)
    if st.button("Explore Data", key="explore_btn", help="View dataset and model insights"):
        st.switch_page("pages/explore.py")
    
    # Process submission
    if submit_button:
        start_time = time.time()
        user_data = {
            'Pregnancies': pregnancies,
            'Glucose': glucose,
            'BloodPressure': blood_pressure,
            'SkinThickness': skin_thickness,
            'Insulin': insulin,
            'BMI': bmi,
            'DiabetesPedigreeFunction': dpf,
            'Age': age,
            'Glucose_BMI': glucose * bmi
        }
        user_input = pd.DataFrame(user_data, index=[0])
        
        # Validate input
        if user_input['Glucose'].iloc[0] == 0:
            st.warning("Glucose value of 0 is invalid. Please enter a realistic value.")
        elif user_input['BloodPressure'].iloc[0] == 0:
            st.warning("Blood Pressure value of 0 is invalid. Please enter a realistic value.")
        elif user_input['BMI'].iloc[0] == 0:
            st.warning("BMI value of 0 is invalid. Please enter a realistic value.")
        else:
            try:
                user_input_scaled = scaler.transform(user_input)
                prediction = model.predict(user_input_scaled)
                prediction_proba = model.predict_proba(user_input_scaled)[0]
                elapsed_time = time.time() - start_time

                # Display prediction
                st.header("Your Prediction")
                with st.container():
                    if prediction[0] == 0:
                        st.success("Low risk of diabetes")
                    else:
                        st.error("High risk of diabetes")
                    st.metric("Probability of Diabetes", f"{prediction_proba[1]:.2%}")
                    st.metric("Probability of No Diabetes", f"{prediction_proba[0]:.2%}")
                    st.metric("Prediction Time", f"{elapsed_time:.2f} seconds")

                # Display suggestions
                st.header("Personalized Suggestions")
                suggestions = generate_suggestions(user_input)
                with st.expander("Medical Metrics", expanded=True):
                    if suggestions["Medical Metrics"]:
                        for suggestion in suggestions["Medical Metrics"]:
                            st.markdown(f"<div class='expander-content'>{suggestion}</div>", unsafe_allow_html=True)
                    else:
                        st.markdown("<div class='expander-content'>- Your medical metrics are within normal ranges. Continue monitoring.</div>", unsafe_allow_html=True)
                
                with st.expander("Lifestyle Recommendations", expanded=True):
                    for suggestion in suggestions["Lifestyle Recommendations"]:
                        st.markdown(f"<div class='expander-content'>{suggestion}</div>", unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Error making prediction: {e}")

    # Footer
    st.markdown("""
    <div class="footer">
        © 2025 Diabetes Prediction App. All rights reserved. 
        | <a href="https://github.com/your-repo">GitHub</a> 
        | <a href="mailto:your-email@example.com">Contact Us</a>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()