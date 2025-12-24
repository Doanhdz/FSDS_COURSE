import argparse
import pickle
import pandas as pd
import mlflow
import mlflow.sklearn


class ModelPredictor:
    def __init__(
        self,
        mlflow_uri: str = "http://0.0.0.0:5000",
        model_name: str = "xgb",
        model_version: str = "1"
    ) -> None:
        self.mlflow_uri = mlflow_uri
        self.model_name = model_name
        self.model_version = model_version

        mlflow.set_tracking_uri(self.mlflow_uri)

    def load_model(self):
        model_uri = f"models:/{self.model_name}/{self.model_version}"
        return mlflow.sklearn.load_model(model_uri)

    def load_scaler(self):
        with open("models/scaler.pkl", "rb") as f:
            return pickle.load(f)

    def predict(self, val_path: str = "data/val.csv"):
        # Load data
        df_val = pd.read_csv(val_path)

        # If Outcome exists, keep it for evaluation
        y_true = None
        if "Outcome" in df_val.columns:
            y_true = df_val["Outcome"]
            X_val = df_val.drop(columns=["Outcome"])
        else:
            X_val = df_val

        # Load scaler and model
        scaler = self.load_scaler()
        model = self.load_model()

        # Scale data
        X_val_scaled = scaler.transform(X_val)

        # Predict
        y_pred = model.predict(X_val_scaled)

        # Predict probabilities if supported
        if hasattr(model, "predict_proba"):
            y_proba = model.predict_proba(X_val_scaled)[:, 1]
        else:
            y_proba = None

        # Save results
        result_df = X_val.copy()
        result_df["prediction"] = y_pred

        if y_proba is not None:
            result_df["probability"] = y_proba

        if y_true is not None:
            result_df["actual"] = y_true

        result_df.to_csv("data/val_predictions.csv", index=False)
        print("Predictions saved to data/val_predictions.csv")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_name", type=str, default="xgb")
    parser.add_argument("--model_version", type=str, default="1")
    parser.add_argument("--val_path", type=str, default="data/val.csv")

    args = parser.parse_args()

    predictor = ModelPredictor(
        model_name=args.model_name,
        model_version=args.model_version,
    )
    predictor.predict(args.val_path)
