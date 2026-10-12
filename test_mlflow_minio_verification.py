import boto3
import mlflow

mlflow.set_tracking_uri("sqlite:///mlflow.db")

experiment_name = "mlops-minio-artifacts-verification"
experiment = mlflow.get_experiment_by_name(experiment_name)

if experiment is None:
    experiment_id = mlflow.create_experiment(
        experiment_name,
        artifact_location="s3://mlops-test/mlflow-artifacts"
    )
else:
    experiment_id = experiment.experiment_id

with mlflow.start_run(experiment_id=experiment_id):
    mlflow.log_param("storage", "MinIO")
    mlflow.log_metric("accuracy", 0.92)

    with open("artefact_minio_verification.txt", "w") as f:
        f.write("Verification du stockage MLflow dans MinIO.\n")

    mlflow.log_artifact("artefact_minio_verification.txt")
    print("URI des artefacts :", mlflow.get_artifact_uri())

s3 = boto3.client(
    "s3",
    endpoint_url="http://127.0.0.1:9000",
    region_name="us-east-1"
)

response = s3.list_objects_v2(
    Bucket="mlops-test",
    Prefix="mlflow-artifacts/"
)

objects = response.get("Contents", [])
print("Nombre d'objets trouvés dans MinIO :", len(objects))

for obj in objects:
    print("-", obj["Key"])
