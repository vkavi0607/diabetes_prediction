import pandas as pd
import streamlit as st
import os

def load_data():
    """Load PIMA dataset from local file, skipping header row."""
    file_path = "pima-indians-diabetes.data.csv"
    columns = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 
               'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome']
    try:
        # Check if file exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Dataset file not found at {file_path}")
        
        # Load CSV with header row
        data = pd.read_csv(
            file_path,
            header=0,
            names=columns,
            dtype={
                'Pregnancies': int,
                'Glucose': float,
                'BloodPressure': float,
                'SkinThickness': float,
                'Insulin': float,
                'BMI': float,
                'DiabetesPedigreeFunction': float,
                'Age': int,
                'Outcome': int
            },
            skipinitialspace=True,
            quoting=3
        )
        
        # Handle non-numeric values
        for col in columns:
            data[col] = pd.to_numeric(data[col], errors='coerce')
        data.dropna(inplace=True)
        
        # Validate column count
        if len(data.columns) != 9:
            raise ValueError(f"Expected 9 columns, got {len(data.columns)}")
        
        if data.empty:
            raise ValueError("Loaded dataset is empty")
        
        # Verify numeric types
        for col in columns:
            if not pd.api.types.is_numeric_dtype(data[col]):
                raise ValueError(f"Column {col} is not numeric: {data[col].dtype}")
        
        return data
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None