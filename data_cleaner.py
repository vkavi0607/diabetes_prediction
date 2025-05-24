import pandas as pd
import numpy as np

def clean_data(data):
    """Clean dataset: handle zeros, impute missing values, cap outliers, and add features."""
    data = data.copy()
    
    # Replace invalid zeros with NaN
    cols_with_zeros = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
    data[cols_with_zeros] = data[cols_with_zeros].replace(0, np.nan)
    
    # Impute missing values with median
    data.fillna(data.median(), inplace=True)
    
    # Cap outliers using IQR method
    for col in ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 
                'BMI', 'DiabetesPedigreeFunction', 'Age']:
        Q1 = data[col].quantile(0.25)
        Q3 = data[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        data[col] = data[col].clip(lower=lower_bound, upper=upper_bound)
    
    # Validate ranges (based on medical plausibility)
    data['Glucose'] = data['Glucose'].clip(lower=40, upper=200)
    data['BloodPressure'] = data['BloodPressure'].clip(lower=40, upper=140)
    data['BMI'] = data['BMI'].clip(lower=15, upper=50)
    data['Insulin'] = data['Insulin'].clip(lower=10, upper=400)
    data['SkinThickness'] = data['SkinThickness'].clip(lower=5, upper=60)
    
    # Feature engineering: Glucose * BMI
    data['Glucose_BMI'] = data['Glucose'] * data['BMI']
    
    return data