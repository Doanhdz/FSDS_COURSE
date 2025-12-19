import mlflow.pyfunc

# Load from local folder
model = mlflow.pyfunc.load_model("mlflow_model")

# Example input
import pandas as pd
data = {'gender':'Female', 
        'ever_married':'No', 
        'work_type':'Private', 
        'Residence_type':'Urban', 
        'smoking_status':'never smoked', 
        'avg_glucose_level_cat':'Low', 
        'bmi_cat':'Underweight', 
        'age_cat':'Adults', 
        'heart_disease_cat':'No', 
        'hypertension_cat':'No'
        }
input_df = pd.DataFrame([data])

# Predict
preds = model.predict(input_df)

print(preds)