### FACE RECOGNITION SYSTEM (DeepFake) ###

Ce projet consiste à identifier des modèles d'IA et d'apprentissage automatique dans les images mélangées(Images générées par l'IA et les vraies images de visage) afin de vérifier l'authenticité, la détection de deepfake.


### A* EXPERIENCES AND TRACKING WITH MLFLOW

***1- Pour installez MLFlow et le client Python DagsHub.***

```bash
pip install -q dagshub mlflow

```

***2-Utilisez le client DagsHub pour configurer les informations de connexion à MLflow. ***

```bash
import dagshub

dagshub.init(
    repo_owner='dona-eric', 
    repo_name='FaceSystemRecognition-DeepFake-', 
    mlflow=True
    )
```
***3- Utilisez MLflow pour consigner les paramètres et les métriques.***

```bash
import mlflow

with mlflow.start_run():
  # Your training code here...
  mlflow.log_metric('accuracy', 42)
  mlflow.log_param('Param name', 'Value')

```
Ou activez la journalisation automatique pour la plupart des frameworks ML populaires, puis exécutez votre code d'entraînement sans aucune modification !

[mlflow](https://mlflow.org/docs/latest/tracking.html)

```bash
mlflow.autolog()
```

### B* Initialisation de DVC and Dagshub Connect S3

***1- Initialisé DVC***

```bash
pip install dvc
dvc init

```
Après avoir initialisé, il est important de vous signaler que l'objectif n'est pas seulement de developper un modèle mais de vous apprendre les bonnes techniques de data engineering.
Pour ce fait, nous allons versionner, les datasets avec *dvc* :

```bash
dvc add yours_datasets

git commit -m "un message de commit personnaliser"

git push -u origin your_branch

```
*Attention*: C'est pas fini !!!

***2- Dagshub DVC Remote***

Pour vous connecter à mlflow et dvc via la plateforme Dagshub, plusieurs possiblités s'offrent à vous.
Vous pouvez configurer une connexion externe de stockage comme (S3, AWS, AZure et GCS). Ainsi vous suivrez exactement les memes démarches comme ce qui se délivre dans ce projet avec le serveur S3.

Ici, à travers la pateforme Dagshub [dagshub]([dagshub](https://dagshub.com/dona-eric)), vous disposez directement d'un point d'accès vers le serveur **S3** compatible.

Dans votre terminal(Linux)/(MacOS):

```bash
pip install dvc-s3
dvc remote add origin s3://dvc
dvc remote modify origin endpointurl https://dagshub.com/dona-eric/FaceSystemRecognition-DeepFake-.s3

```
***Setup credentials***

Dans l'onglet **Remote** vous verrez ***Data** et vous choisissez l'option ****DVC****

```bash
dvc remote modify origin --local access_key_id your_token
dvc remote modify origin --local secret_access_key your_token
```
***your_token*** = le token disponible dans le lien de l'onglet


Now, dans la partie **B**, nous avons ajouter nos datasets sur dvc, mais pour s'assurer que les données sont bien versionnés et etre suivis meme après modification, il faut les pousser sur dagshub par la connexion  S3 . Et c'est ce que nous allons voir.

***Push the datasets versioning***
```bash
dvc push -r origin

``` 
Et c'est terminé


## 📁 Project Structure

```
FaceSystemRecognition-DeepFake-/
│
├── src/
│   └── Face_Recognition_System/          # Main package
│       ├── __init__.py
│       ├── components/                   # Modular components for pipeline
│       │   └── __init__.py
│       ├── config/                       # Configuration management
│       │   ├── __init__.py
│       │   └── configuration.py          # Config class definitions
│       ├── constants/                    # Constants & paths
│       │   ├── __init__.py
│       │   └── (CONFIG_FILE_PATH, PARAMS_FILE_PATH)
│       ├── entity/                       # Data models/entities
│       │   └── __init__.py
│       ├── pipeline/                     # ML pipeline orchestration
│       │   └── __init__.py
│       └── utils/                        # Utility functions
│           ├── __init__.py
│           └── common.py                 # YAML reader, logging, etc.
│
├── research/                             # Jupyter notebooks for experimentation
│   ├── 01_data_ingestion.ipynb          # Data loading & preprocessing
│   └── trials.ipynb                      # Experimental notebooks
│
├── config/
│   └── config.yml                        # Configuration file
│
├── templates/
│   └── index.html                        # Web UI template
│
├── logs/                                 # Application logs
│
├── main.py                               # Entry point
├── test.py                               # Testing
├── setup.py                              # Package setup
├── requirements.txt                      # Dependencies
├── params.yml                            # ML parameters
├── dvc.yml                               # DVC pipeline definition
├── mlflow_s3.yml                         # MLFlow S3 configuration
└── README.md                             # Documentation
```

---

## 🔧 Technology Stack

### Core ML/CV Libraries
- **torch** (2.4.1) - Deep Learning Framework
- **torchvision** (0.19.1) - Computer Vision utilities
- **tensorflow** (2.20.0) - Alternative DL framework
- **keras** (3.13.1) - High-level neural networks API
- **opencv-python** (4.10.0.84) - Image processing

### Data Processing
- **pandas** (2.2.2) - Data manipulation
- **numpy** (2.4.1) - Numerical computing
- **scikit-learn** (1.8.0) - ML utilities

### MLOps & Experiment Tracking
- **mlflow** (3.8.1) - Experiment tracking & model registry
- **dvc** (3.59.0) - Data versioning & pipeline orchestration
- **dagshub** (0.6.4) - MLOps platform integration

### Web Framework
- **fastapi** (0.115.0, 0.128.0) - Modern async web framework
- **uvicorn** (0.40.0) - ASGI server
- **requests** (2.32.3) - HTTP client

### Data Storage
- **boto3** (1.42.32) - AWS S3 integration for cloud storage
- **gdown** (5.1.0) - Google Drive downloads

### Utilities
- **pyYAML** (6.0.1) - YAML parsing
- **python-box** (7.3.2) - Dict-to-object conversion
- **joblib** (1.5.3) - Serialization & parallel processing
- **tqdm** (4.66.5) - Progress bars
- **matplotlib** (3.10.8) - Visualization
- **seaborn** (0.13.2) - Statistical visualization
- **transformers** (4.45.2) - Pretrained models (HuggingFace)

### Development
- **ipykernel** (7.1.0) - Jupyter kernel

---

## 🏗️ Architecture Layers

### 1. **Constants Layer** (`constants/`)
- Configuration file paths
- Hyperparameters
- Global constants

### 2. **Entity/Data Models Layer** (`entity/`)
- Data classes for type hints
- Configuration objects
- Data structures

### 3. **Utilities Layer** (`utils/`)
- `common.py`:
  - `read_yml()` - YAML configuration loader
  - Logging initialization
  - Helper functions (file I/O, base64 encoding, etc.)

### 4. **Configuration Layer** (`config/`)
- `configuration.py` - Config class for managing settings
- Reads from `config.yml` and `params.yml`

### 5. **Components Layer** (`components/`)
- Modular pipeline components:
  - Data ingestion
  - Data validation
  - Feature engineering
  - Model training
  - Model evaluation

### 6. **Pipeline Layer** (`pipeline/`)
- Orchestrates components
- Defines ML workflow execution order

### 7. **Web Layer** (`templates/`)
- Frontend UI (FastAPI/Flask)
- API endpoints for inference

---

## 📊 MLOps Integration

### DVC (Data Version Control)
- Pipeline definition: `dvc.yml`
- Tracks data & model versioning
- Remote storage on DagsHub S3

### MLFlow
- Experiment tracking with metrics/parameters
- Model registry
- Integration with DagsHub
- Config: `mlflow_s3.yml`


## 📦 Installation & Setup

### 1. Install Package (Recommended)
```bash
pip install -e .
```

### 2. Or Install Dependencies Only
```bash
pip install -r requirements.txt
```

### 3. Configure Credentials
Edit `config/config.yml` with:
- Model paths
- Data directories
- API credentials

---

## ⚙️ Configuration Files

### `config/config.yml`
- Application settings
- Path configurations
- Model parameters

### `params.yml`
- ML hyperparameters
- Training configurations
- Model architecture details

### `dvc.yml`
- DVC pipeline stages
- Data dependencies
- Output artifacts

### `mlflow_s3.yml`
- MLFlow S3 backend config
- Tracking server settings
- Artifact store location

---

## 🔄 Data Flow

```
Raw Data
    ↓
[Data Ingestion Component] → logs/
    ↓
[Data Validation Component]
    ↓
[Feature Engineering Component]
    ↓
[Model Training Component] → MLFlow (metrics, params)
    ↓                      → DVC (model artifacts)
[Model Evaluation Component]
    ↓
[API Inference]
    ↓
Frontend (streamlit.app)
```

---

## 🔗 GitHub Repository
- **Owner**: Dona Eric KOULODJI
- **Repo**: FaceSystemRecognition-DeepFake-
- **Branch**: develop
- **License**: MIT


## Contacts

Pour toutes collaborations, projets ou accompagnement,je suis ouvert à toutes les opportunités qui me permttent d'avoir un cadre d'échange, d'apprentissage et de partage.

- **Email**: [dona-eric](donaerickoulodji@gmail.com)
- **Linkedin**: [dona-erick](https://www.linkedin.com/in/dona-erick)
- **Whatsapp**: [KOULODJI Eric](https://wa.me/+2290151344289)
- **Github**: [dona-eric](https://github.com/dona-eric)
- **Portfolio**: [mon-portfolio](https://donerick.vercel.app)

##                                 ***Fait par Dona Eric KOULODJI***
