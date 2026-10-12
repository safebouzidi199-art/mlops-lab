import os
import mlflow

mlflow.set_tracking_uri("sqlite:///mlflow.db")
mlflow.set_experiment("mlops-minio-test")

with mlflow.start_run():
    mlflow.log_param("storage", "MinIO")
    mlflow.log_metric("accuracy", 0.92)

    with open("artefact_minio.txt", "w") as f:
        f.write("Artefact MLflow stocké dans MinIO.\n")

    mlflow.log_artifact("artefact_minio.txt")

print("Test MLflow avec MinIO terminé.")
