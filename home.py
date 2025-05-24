import streamlit as st

# Set page configuration to hide default sidebar menu
st.set_page_config(page_title="Diabetes Prediction App", layout="wide")

# Custom CSS for sophisticated UI
st.markdown("""
    <style>
    .main {
        background-color: #000000;
        padding: 20px;
        font-family: 'Roboto', sans-serif;
        color: #ffffff;
    }
    .hero-section {
        background: linear-gradient(135deg, #1a1a1a 0%, #333333 100%);
        padding: 40px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.5);
        margin-bottom: 30px;
    }
    .hero-title {
        font-size: 2.5em;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 10px;
    }
    .hero-subtitle {
        font-size: 1.2em;
        color: #d1d1d1;
        margin-bottom: 20px;
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
    h1, h2, h3 {
        color: #ffffff;
        font-weight: 500;
    }
    .feature-card {
        background-color: #1a1a1a;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
        transition: transform 0.3s;
        text-align: center;
        color: #ffffff;
    }
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 4px 15px rgba(0, 123, 255, 0.2);
    }
    .feature-title {
        font-size: 1.3em;
        font-weight: 600;
        margin-bottom: 10px;
    }
    .feature-desc {
        font-size: 1em;
        color: #d1d1d1;
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
    .expander-content {
        background-color: #1a1a1a;
        padding: 15px;
        border-radius: 8px;
        color: #d1d1d1;
    }
    </style>
""", unsafe_allow_html=True)

def main():
    # Custom sidebar with navigation
    with st.sidebar:
        st.markdown("<h2 style='color: #ffffff;'>Navigation</h2>", unsafe_allow_html=True)
        if st.button("🏠 Home", key="nav_home"):
            st.switch_page("home.py")
        if st.button("🔍 Predict", key="nav_predict"):
            st.switch_page("pages/predict.py")
        if st.button("📊 Explore", key="nav_explore"):
            st.switch_page("pages/explore.py")

    # Hero Section
    with st.container():
        st.markdown("""
        <div class="hero-section">
            <h1 class="hero-title">Diabetes Prediction App</h1>
            <p class="hero-subtitle">
                Discover your diabetes risk with our advanced XGBoost model, trained on the PIMA Indians Diabetes Dataset. 
                Get personalized predictions and actionable health recommendations in seconds.
            </p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Start Predicting Now", key="start_predict"):
            st.switch_page("pages/predict.py")

    # Features Section
    st.header("Why Use Our App?", anchor="get-started")
    st.markdown("Explore powerful features designed to empower you with health insights and proactive steps.")

    # Feature Cards
    cols = st.columns(3)
    features = [
        {
            "title": "Fast Predictions",
            "desc": "Get accurate diabetes risk predictions in under 3 seconds with ~78-80% accuracy."
        },
        {
            "title": "Personalized Suggestions",
            "desc": "Receive tailored medical and lifestyle recommendations based on CDC, WHO, and ADA guidelines."
        },
        {
            "title": "Interactive Visualizations",
            "desc": "Dive into data with histograms, correlation heatmaps, and feature importance plots."
        }
    ]

    for idx, feature in enumerate(features):
        with cols[idx]:
            st.markdown(f"""
            <div class="feature-card">
                <div class="feature-title">{feature['title']}</div>
                <div class="feature-desc">{feature['desc']}</div>
            </div>
            """, unsafe_allow_html=True)

    # About Section
    st.header("About the App")
    with st.expander("Learn More", expanded=False):
        st.markdown("""
        <div class="expander-content">
            <p><strong>Dataset</strong>: The app uses the PIMA Indians Diabetes Dataset, containing 768 records with 9 features like Glucose, BMI, and Age.</p>
            <p><strong>Model</strong>: Powered by an optimized XGBoost classifier, fine-tuned for high accuracy and fast predictions.</p>
            <p><strong>Suggestions</strong>: Personalized recommendations to reduce diabetes risk, grounded in medical guidelines.</p>
            <p><strong>Visualizations</strong>: Explore data distributions, correlations, and model performance through interactive plots.</p>
            <p><strong>Technology</strong>: Built with Streamlit, Pandas, Scikit-learn, and XGBoost for a seamless experience.</p>
        </div>
        """, unsafe_allow_html=True)

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