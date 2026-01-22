import mlflow
from Face_Recognition_System import logger
from mlflow.data.pandas_dataset import PandasDataset
import mlflow.data
import pandas as pd
import os, pathlib


@mlflow.trace
def Tracking_dataset_mlflow(
        data_path: pathlib.Path
) -> PandasDataset:
    
    data = pd.read_csv(data_path)
    dataset = mlflow.data.from_pandas(
        data,
        source=data_path,
        name="Face_Recognition_Dataset",
    )
    
    mlflow.set_experiment("Face_Recognition_System")
    with mlflow.start_run(run_name="Dataset_Tracking") as run:

        logger.info(f"Dataset logged with run ID: {run.info.run_id}")
        mlflow.log_param("total_images", len(data))
        mlflow.log_param("ai_images", len(data[data['label'] == 1]))
        mlflow.log_param("real_images", len(data[data['label'] == 0]))
    
        # LOG DU DATASET 
        mlflow.log_input(dataset, context="training")
    
    # Tu peux aussi logger le CSV lui-même comme un fichier (artifact)
        mlflow.log_artifact(data_path, artifact_path="dataset")

        logger.info(f"Tracking du dataset terminé avec succès.")

if __name__ == "__main__":
    data_path = "artifacts/dataset_metadata.csv"
    Tracking_dataset_mlflow(data_path=data_path)

