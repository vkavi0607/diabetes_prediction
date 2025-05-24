Diabetes Prediction App:
Overview:
The Diabetes Prediction App is a web-based application built with Streamlit, designed to predict diabetes risk using the PIMA Indians Diabetes Dataset. It leverages an optimized XGBoost classifier to deliver fast and accurate predictions, providing users with personalized medical and lifestyle recommendations based on their input health metrics. The app also offers interactive data visualizations and model performance insights for a deeper understanding of the dataset and the model's behavior.
Key Features

Prediction:
Users can input health metrics (e.g., Glucose, BMI, Age) to receive a diabetes risk prediction along with tailored suggestions based on CDC, WHO, and ADA guidelines.
Exploration: Visualize dataset features, correlations, and model performance metrics (e.g., accuracy, confusion matrix, feature importance).
Data Processing: Robust data cleaning handles missing values, outliers, and invalid entries, ensuring reliable predictions.

Performance:
Achieves ~78-80% accuracy with predictions processed in under 3 seconds.

User Interface: 
Modern, dark-themed design with a black background, interactive forms, and responsive visualizations.

Installation Prerequisites:

Python 3.8 or higher
pip (Python package manager)
Git (optional, for cloning the repository)

Steps:

Clone the Repository (if applicable):
git clone https://github.com/your-repo/diabetes-prediction-app.git
cd diabetes-prediction-app

Create a Virtual Environment (recommended):
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install Dependencies:Ensure the requirements.txt file is in the project directory, then run:
pip install -r requirements.txt

The requirements.txt includes:
streamlit>=1.38.0
pandas>=2.2.2
numpy>=1.26.4
scikit-learn>=1.5.1
xgboost>=2.1.1
matplotlib>=3.9.2
seaborn>=0.13.2


Verify Dataset:
Ensure the pima-indians-diabetes.data.csv file is present in the project directory. This file contains the PIMA Indians Diabetes Dataset used for training and predictions.

Run the Application:
streamlit run home.py
This will launch the app in your default web browser at http://localhost:8501.


Usage:

Home Page (home.py):
Overview of the app’s features and purpose.
Instructions to navigate to the "Predict" or "Explore" pages via the sidebar.
Expandable "About" section with details on the dataset, model, and technology stack.

Predict Page (predict.py):
Input health metrics (Pregnancies, Glucose, Blood Pressure, etc.) using the interactive form.
Submit to receive a diabetes risk prediction (Low/High risk) with probability scores.
View personalized medical and lifestyle recommendations based on your input.
Example: Enter Glucose: 120, BMI: 32, and other metrics, then click "Predict Risk" to see results.

Explore Page (explore.py):
Preview the first 5 rows of the dataset.
Visualize feature distributions (histograms), correlations (heatmap), and feature importance (bar plot).
Review model performance metrics, including accuracy, confusion matrix, and classification report.


File Structure:
diabetes-prediction-app/
├── pima-indians-diabetes.data.csv  # Dataset file
├── home.py                        # Main landing page
├── predict.py                     # Prediction page with user input and suggestions
├── explore.py                     # Data and model visualization page
├── data_loader.py                 # Loads and validates the dataset
├── data_cleaner.py                # Cleans data (handles zeros, outliers, etc.)
├── model_trainer.py               # Trains and evaluates the XGBoost model
├── suggestions.py                 # Generates personalized recommendations
├── requirements.txt               # Python dependencies
├── README.md                      # Project documentation (this file)

Dataset:
The app uses the PIMA Indians Diabetes Dataset, which contains 768 records with 9 features:
Pregnancies: Number of pregnancies (0–17)
Glucose: Plasma glucose concentration (mg/dL)
BloodPressure: Diastolic blood pressure (mm Hg)
SkinThickness: Triceps skin fold thickness (mm)
Insulin: 2-hour serum insulin (mu U/ml)
BMI: Body mass index
DiabetesPedigreeFunction: Genetic diabetes risk score
Age: Age in years
Outcome: Diabetes diagnosis (0 = No, 1 = Yes)

The dataset is cleaned to handle invalid zeros, impute missing values with medians, cap outliers using the IQR method, and add a derived feature (Glucose_BMI).
Model

Algorithm: XGBoost classifier
Parameters:
n_estimators=50
max_depth=3
learning_rate=0.1
subsample=0.8
colsample_bytree=0.8
random_state=42


Preprocessing: Features are scaled using StandardScaler after cleaning.
Performance: Achieves ~78-80% accuracy on the test set, with detailed metrics (confusion matrix, classification report) available on the Explore page.

Data Cleaning
The data_cleaner.py script performs the following:

Replaces invalid zeros in Glucose, BloodPressure, SkinThickness, Insulin, and BMI with NaN.
Imputes missing values with column medians.
Caps outliers using the IQR method.
Clips features to medically plausible ranges (e.g., Glucose: 40–200 mg/dL).
Adds a Glucose_BMI feature to capture interaction between Glucose and BMI.

Suggestions
The suggestions.py script generates recommendations based on user input, following CDC, WHO, and ADA guidelines. It provides:

Medical Metrics: Tailored advice for high/low Glucose, BMI, Blood Pressure, etc.
Lifestyle Recommendations: General advice on physical activity, diet, stress management, and more.

Visualizations
The explore.py script includes:

Feature Distributions: Histograms for each feature.
Correlation Heatmap: Visualizes feature correlations using a coolwarm colormap.
Feature Importance: Bar plot of feature contributions to the XGBoost model.
Confusion Matrix: Heatmap showing model prediction performance.
Classification Report: Detailed metrics (precision, recall, F1-score) for each class.

Troubleshooting

Dataset Not Found: Ensure pima-indians-diabetes.data.csv is in the project directory.
Dependency Issues: Verify all packages in requirements.txt are installed correctly.
Visualization Errors: Ensure matplotlib and seaborn are compatible with your Python version.
Prediction Errors: Check that input values are within valid ranges (e.g., Glucose > 0).

Contributing
Contributions are welcome! To contribute:

Fork the repository.
Create a new branch (git checkout -b feature/your-feature).
Make changes and commit (git commit -m "Add your feature").
Push to the branch (git push origin feature/your-feature).
Open a pull request with a detailed description of your changes.

Please ensure code follows PEP 8 style guidelines and includes appropriate tests.
License
This project is licensed under the MIT License. See the LICENSE file for details (not included in this repository yet).
Contact
For questions or feedback, please open an issue on the GitHub repository or contact the maintainer at [kaviyarasuv0607@gmail.com].

Built with ❤️ using Streamlit and XGBoost
