import mlflow
from pathlib import Path

# Get outer folder (project root)
project_root = Path(__file__).resolve().parent.parent.parent
print(project_root)

REGISTERED_MODEL_NAME = 'stroke_prediction_model'
STAGE_STATUS = 'Production'

mlflow.set_tracking_uri("http://0.0.0.0:5001")

mlflow.artifacts.download_artifacts(
	artifact_uri=f"models:/{REGISTERED_MODEL_NAME}/{STAGE_STATUS}",
	dst_path=str(project_root / "model/mlflow_model")
)