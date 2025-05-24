def generate_suggestions(user_data):
    """Generate comprehensive personalized suggestions for diabetes risk reduction."""
    suggestions = {
        "Medical Metrics": [],
        "Lifestyle Recommendations": []
    }
    pregnancies = user_data['Pregnancies'].iloc[0]
    glucose = user_data['Glucose'].iloc[0]
    blood_pressure = user_data['BloodPressure'].iloc[0]
    skin_thickness = user_data['SkinThickness'].iloc[0]
    insulin = user_data['Insulin'].iloc[0]
    bmi = user_data['BMI'].iloc[0]
    dpf = user_data['DiabetesPedigreeFunction'].iloc[0]
    age = user_data['Age'].iloc[0]

    # Medical Metrics Suggestions (based on CDC, WHO, ADA guidelines)
    if glucose > 126:
        suggestions["Medical Metrics"].append(" High Glucose: Your glucose level (>126 mg/dL) suggests possible diabetes. Consult a healthcare provider for an A1C test and adopt a lowglycemic diet (e.g., whole grains, leafy greens, lean proteins).")
    elif glucose > 100:
        suggestions["Medical Metrics"].append(" Elevated Glucose: Your glucose (100-126 mg/dL) indicates prediabetes risk. Monitor blood sugar regularly and reduce intake of refined sugars and highcarb foods.")
    elif glucose < 70:
        suggestions["Medical Metrics"].append(" Low Glucose: Your glucose (<70 mg/dL) is below normal. Consult a doctor to rule out hypoglycemia and ensure balanced meals with complex carbohydrates.")

    if bmi > 30:
        suggestions["Medical Metrics"].append(" Obesity: Your BMI (>30) indicates obesity, a major diabetes risk factor. Work with a dietitian to create a weight loss plan targeting 510% body weight reduction through diet and exercise.")
    elif bmi > 25:
        suggestions["Medical Metrics"].append(" Overweight: Your BMI (25-30) suggests overweight. Aim for a balanced diet and 150 min/week of moderate exercise (e.g., brisk walking) to reach a BMI below 25.")
    elif bmi < 18.5:
        suggestions["Medical Metrics"].append(" Underweight: Your BMI (<18.5) is below normal. Consult a healthcare provider to ensure adequate nutrition and rule out underlying conditions.")

    if blood_pressure > 130:
        suggestions["Medical Metrics"].append(" High Blood Pressure: Your blood pressure (>130 mm Hg) indicates hypertension. Reduce salt intake, manage stress, and consult a doctor for medication or monitoring.")
    elif blood_pressure > 120:
        suggestions["Medical Metrics"].append(" Elevated Blood Pressure: Your blood pressure (120-130 mm Hg) is above optimal. Limit sodium, increase physical activity, and monitor regularly.")
    elif blood_pressure < 90:
        suggestions["Medical Metrics"].append(" Low Blood Pressure: Your blood pressure (<90 mm Hg) is below normal. Consult a doctor to address potential causes and ensure proper hydration.")

    if insulin > 200:
        suggestions["Medical Metrics"].append(" High Insulin: Your insulin level (>200 mu U/ml) suggests insulin resistance. Consult an endocrinologist and focus on lowcarb diets and regular exercise to improve insulin sensitivity.")
    elif insulin < 20:
        suggestions["Medical Metrics"].append(" Low Insulin: Your insulin level (<20 mu U/ml) is below typical ranges. Consult a doctor to evaluate pancreatic function and diabetes risk.")

    if skin_thickness > 40:
        suggestions["Medical Metrics"].append(" High Skin Thickness: Your skin thickness (>40 mm) may indicate higher fat deposits. Combine aerobic exercise (e.g., running) and strength training to reduce body fat.")
    elif skin_thickness < 10:
        suggestions["Medical Metrics"].append(" Low Skin Thickness: Your skin thickness (<10 mm) is below typical ranges. Ensure adequate nutrition and consult a doctor if related to weight loss or other conditions.")

    if pregnancies > 4:
        suggestions["Medical Metrics"].append(" Multiple Pregnancies: Having more than 4 pregnancies increases gestational diabetes risk. Discuss screening with your doctor, especially if planning future pregnancies.")
    elif pregnancies > 0:
        suggestions["Medical Metrics"].append(" Pregnancy History: Previous pregnancies may increase diabetes risk. Maintain a healthy weight and monitor blood sugar, especially postpregnancy.")

    if dpf > 0.5:
        suggestions["Medical Metrics"].append(" Genetic Risk: Your Diabetes Pedigree Function (>0.5) indicates a higher genetic predisposition. Schedule regular screenings and adopt a proactive healthy lifestyle.")
    elif dpf > 0.2:
        suggestions["Medical Metrics"].append(" Moderate Genetic Risk: Your Diabetes Pedigree Function (0.20.5) suggests some genetic risk. Stay vigilant with annual checkups and healthy habits.")

    if age > 45:
        suggestions["Medical Metrics"].append(" AgeRelated Risk: Being over 45 increases diabetes risk. Schedule annual checkups, maintain a healthy weight, and monitor blood sugar regularly.")
    elif age > 30:
        suggestions["Medical Metrics"].append(" Age Consideration: Being over 30, especially with other risk factors, warrants attention. Incorporate regular exercise and a balanced diet to reduce risk.")

    # Lifestyle Recommendations (applicable to all)
    suggestions["Lifestyle Recommendations"].extend([
        " Physical Activity: Engage in at least 150 minutes of moderate aerobic activity (e.g., brisk walking, cycling, swimming) per week, plus strength training (e.g., weightlifting) twice weekly to improve insulin sensitivity.",
        " Healthy Diet: Follow a balanced diet rich in whole grains (e.g., quinoa, brown rice), lean proteins (e.g., chicken, fish), healthy fats (e.g., avocados, nuts), and plenty of vegetables. Limit processed foods, sugary drinks, and trans fats.",
        " Weight Management: Maintain or achieve a healthy BMI (18.524.9) through portion control and regular physical activity to reduce diabetes risk.",
        " Stress Management: Practice stressreduction techniques like meditation, yoga, or deep breathing to lower cortisol levels, which can affect blood sugar.",
        " No Smoking: Quit smoking, as it increases diabetes risk and complicates blood sugar control. Seek support through cessation programs if needed.",
        " Limit Alcohol: Keep alcohol intake moderate (up to 1 drink/day for women, 2 for men) to avoid blood sugar spikes and support overall health.",
        " Regular Monitoring: Check blood glucose, blood pressure, and weight regularly, especially if you have a family history of diabetes or other risk factors.",
        " Sleep Hygiene: Aim for 79 hours of quality sleep per night to support metabolic health and reduce insulin resistance.",
        " Hydration: Drink adequate water (810 cups/day) to support overall health and kidney function, especially if glucose levels are high."
    ])

    return suggestions