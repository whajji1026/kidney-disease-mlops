# kidney-disease-mlops

## Workflows

- Update config.yaml
- Update secrets.yaml [Optional]
- Update params.yaml
- Update the entity
- Update the configuration manager in `src/config`
- Update the components
- Update the pipeline
- Update the `main.py`
- Update the `dvc.yaml`
- `app.py`

## How to run?

### STEPS:

#### 1. Clone the repository:
```bash
https://github.com/whajji1026/kidney-disease-mlops
```

#### 2. Create a conda environment after opening the repository:
```bash
conda create -n cnncls python=3.8 -y 
conda activate cnncls 
```


#### 3. Install the requirements:
```bash
pip install -r requirements.txt
```
#### 4. MLflow + Dagshub:
for Linux
```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/whajji1026/kidney-disease-mlops.mlflow

export MLFLOW_TRACKING_USERNAME=whajji1026 

export MLFLOW_TRACKING_PASSWORD=d432069e83aeb456c8bdd0865fc17116e810c5c2

```
for Windows

```bash

$env:MLFLOW_TRACKING_URI = "https://dagshub.com/whajji1026/kidney-disease-mlops.mlflow"


$env:MLFLOW_TRACKING_USERNAME = "whajji1026"

$env:MLFLOW_TRACKING_PASSWORD = "d432069e83aeb456c8bdd0865fc17116e810c5c2"

```

#### 5. dvc:
```bash
dvc init
dvc repro
dvc dag
```


#### 6. azure ci/cd deployment with github actions

```bash

docker build -t ctscan.azurecr.io/kidneyscan:latest .

docker login ctscan.azurecr.io

docker push ctscan.azurecr.io/kidneyscan:latest 

```