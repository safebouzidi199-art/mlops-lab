import mlflow

mlflow.set_experiment("mlops-lab-test")

with mlflow.start_run():
    mlflow.log_param("learning_rate", 0.01)
    mlflow.log_param("epochs", 10)
    mlflow.log_metric("accuracy", 0.92)

    with open("resultat.txt", "w") as f:
        f.write("Test MLflow réussi !\n")

    mlflow.log_artifact("resultat.txt")

print("Test MLflow terminé avec succès !")
