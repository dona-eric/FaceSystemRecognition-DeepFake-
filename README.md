### FACE RECOGNITION SYSTEM

Ce projet consiste à identifier des modèles d'IA et d'apprentissage automatique dans les images mélangées(Images générées par l'IA et les vraies images de visage) afin de vérifier l'authenticité, la détection de deepfake.


### EXPERIENCES AND TRACKING WITH MLFLOW

##### 1- Pour installez MLFlow et le client Python DagsHub.
```bash
%pip install -q dagshub mlflow
```

##### 2- Utilisez le client DagsHub pour configurer les informations de connexion à MLflow.
```bash
import dagshub

dagshub.init(repo_owner='dona-eric', repo_name='FaceSystemRecognition-DeepFake-', mlflow=True)
```
##### 3- Utilisez MLflow pour consigner les paramètres et les métriques.
```bash
import mlflow
with mlflow.start_run():
  # Your training code here...
  mlflow.log_metric('accuracy', 42)
  mlflow.log_param('Param name', 'Value')
```
Ou activez la journalisation automatique pour la plupart des frameworks ML populaires, puis exécutez votre code d'entraînement sans aucune modification !

![mlflow]https://mlflow.org/docs/latest/tracking.html
```bash
mlflow.autolog()
```

### Initialisation de DVC and Dagshub Connect S3

1- Initialisé DVC
```bash
dvc init

### votre repertoire .dvc est initialisé
```