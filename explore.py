import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data_loader import load_data
from data_cleaner import clean_data
from model_trainer import train_model

# Set page configuration to hide default sidebar menu
st.set_page_config(page_title="Explore - Diabetes Prediction App", layout="wide")

# Custom CSS for enhanced UI
st.markdown("""
    <style>
    .main {
        background-color: #000000;
        padding: 20px;
        font-family: 'Roboto', sans-serif;
        color: #ffffff;
    }
    h1, h2, h3 {
        color: #ffffff;
        font-weight: 500;
    }
    .stPlotlyChart, .stImage {
        background-color: #1a1a1a;
        border-radius: 10px;
        padding: 10px;
        border: 1px solid #333333;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
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
        if st.button("🔍 Predict", key="nav_predict"):
            st.switch_page("pages/predict.py")
        if st.button("📊 Explore", key="nav_explore", disabled=True):  # Disabled to indicate active page
            pass

    st.title("Explore Data and Model Performance")
    st.markdown("Dive into the PIMA Indians Diabetes Dataset and analyze the XGBoost model's performance with interactive visualizations.")

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
        model, scaler, X_train, X_test, accuracy, conf_matrix, class_report = train_model(X, y)
    except Exception as e:
        st.error(f"Error training model: {e}")
        return
    
    # Dataset preview
    st.header("Dataset Preview")
    with st.expander("View First 5 Rows", expanded=True):
        st.markdown("<div class='expander-content'>", unsafe_allow_html=True)
        st.write(data.head())
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Visualizations
    st.header("Visualizations")
    st.subheader("Feature Distributions")
    try:
        fig, axes = plt.subplots(2, 5, figsize=(20, 8))
        axes = axes.ravel()
        for idx, col in enumerate(X.columns):
            sns.histplot(data[col], ax=axes[idx], kde=True, bins=20, color='#007bff', edgecolor='#ffffff')
            axes[idx].set_title(col, fontsize=10, color='#ffffff')
            axes[idx].set_facecolor('#1a1a1a')
            axes[idx].tick_params(axis='x', colors='#ffffff')
            axes[idx].tick_params(axis='y', colors='#ffffff')
            axes[idx].grid(True, color='#333333', linestyle='--', alpha=0.5)
        plt.tight_layout()
        plt.savefig('feature_distributions.png', transparent=True)
        st.image('feature_distributions.png')
    except Exception as e:
        st.error(f"Error generating histograms: {e}")
    
    st.subheader("Correlation Heatmap")
    try:
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.heatmap(data.corr(), annot=True, cmap='coolwarm', ax=ax, fmt='.2f', cbar_kws={'label': 'Correlation'})
        ax.set_facecolor('#1a1a1a')
        ax.tick_params(axis='x', colors='#ffffff')
        ax.tick_params(axis='y', colors='#ffffff')
        ax.set_title("Correlation Heatmap", color='#ffffff')
        plt.savefig('correlation_heatmap.png', transparent=True)
        st.image('correlation_heatmap.png')
    except Exception as e:
        st.error(f"Error generating heatmap: {e}")
    
    st.subheader("Feature Importance")
    try:
        fig, ax = plt.subplots(figsize=(8, 5))
        feat_importance = pd.Series(model.feature_importances_, index=X.columns)
        feat_importance.sort_values().plot(kind='barh', ax=ax, color='#007bff')
        ax.set_title("Feature Importance in XGBoost Model", color='#ffffff')
        ax.set_facecolor('#1a1a1a')
        ax.tick_params(axis='x', colors='#ffffff')
        ax.tick_params(axis='y', colors='#ffffff')
        plt.savefig('feature_importance.png', transparent=True)
        st.image('feature_importance.png')
    except Exception as e:
        st.error(f"Error generating feature importance: {e}")
    
    # Model performance
    st.header("Model Performance")
    st.metric("Accuracy", f"{accuracy:.2%}")
    
    st.subheader("Confusion Matrix")
    try:
        fig, ax = plt.subplots(figsize=(5, 4))
        sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', ax=ax)
        ax.set_xlabel("Predicted", color='#ffffff')
        ax.set_ylabel("Actual", color='#ffffff')
        ax.set_facecolor('#1a1a1a')
        ax.tick_params(axis='x', colors='#ffffff')
        ax.tick_params(axis='y', colors='#ffffff')
        plt.savefig('confusion_matrix.png', transparent=True)
        st.image('confusion_matrix.png')
    except Exception as e:
        st.error(f"Error generating confusion matrix: {e}")
    
    st.subheader("Classification Report")
    with st.expander("View Classification Report", expanded=True):
        st.markdown("<div class='expander-content'>", unsafe_allow_html=True)
        st.write(pd.DataFrame(class_report).transpose())
        st.markdown("</div>", unsafe_allow_html=True)

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