from pydantic import BaseModel


class Data(BaseModel):
    data: list = [[5,140,65,35,0,36.6,0.434,56]]
    id: str = 123
    columns: list = ["Pregnancies","Glucose","BloodPressure","SkinThickness","Insulin","BMI","DiabetesPedigreeFunction","Age"]