FROM python:3.9-slim

# Port will be exposed, for documentation only
EXPOSE 7000

# Define working folder
WORKDIR /api_source

# Copy source code
COPY service/model_api_serving/api_source ./api_source

# Copy MLflow model
COPY ./model/mlflow_model ./mlflow_model

RUN pip install --upgrade pip && \
	pip install --no-cache-dir -r api_source/requirements.txt psycopg2-binary

CMD ["uvicorn", "api_source.instrument:app", "--host", "0.0.0.0", "--port", "7000", "--reload"]
