 Fraud Detection System

A cloud-native fraud detection platform for identifying suspicious financial transactions using Machine Learning.
The system includes a FastAPI backend, a Streamlit dashboard, a PostgreSQL database, and is fully containerized with Docker and deployed on Render.

 Table of Contents

Overview

Architecture

Project Structure

Setup & Installation

Usage

API

Dashboard

Model Training

Logging

Deployment

Future Improvements

License

 Overview

This project implements an anomaly-based fraud detection system using XGBoost and Isolation Forest. It supports:

* Real-time detection of fraudulent transactions.
* REST API (FastAPI) to serve predictions.
* PostgreSQL database for storing results and logs.
* Streamlit dashboard for monitoring anomalies and alerts.
* Cloud deployment on Render with Docker.

 Architecture
flowchart TD
    subgraph Client
    A[User Transaction Request]
    end

    subgraph Backend
    B[FastAPI Service] --> C[XGBoost Fraud Model]
    end

    subgraph Database
    D[(PostgreSQL Database)]
    end

    subgraph Dashboard
    E[Streamlit Dashboard]
    end


---

 Project Structure  


fraud-detection-cloud/
│
├─ app/ # FastAPI backend app
│ ├─ app.py # API entry point
│ ├─ crud.py 
│ |─ db.py
│ ├─ dependencies.py
│ |─init_db.py
| |─model_utils.py
│ |─models.py
| |─schemas.py
|
├─ dashboard/ # Streamlit dashboard
│ └─ streamlit_app.py
│
├─ data/ # Datasets
│ 
├─ model/ # Training & evaluation scripts
│ ├─ preprocess_data.py
│ ├─ train_model.py
│ ├─ explore_data.py
│ └─ evaluate_model.py
|
├─ tests/ # Unit & API tests
│
├─ Dockerfile # Docker config for API
├─ docker-compose.yml # Multi-service orchestration
├─ requirements.txt # Dependencies
├─ transactions.db # Local SQLite (deprecated, now PostgreSQL)
├─ xgb_fraud_model.pkl # Pre-trained XGBoost model
└─ README.md


---

 Setup & Installation  

###  Clone Repository  
```bash
git clone https://github.com/MedEzzoghlami/fraud-detection-cloud.git
cd fraud-detection-cloud

 Create Virtual Environment
python -m venv venv


Activate:

Windows: venv\Scripts\activate

Linux/Mac: source venv/bin/activate

 Install Dependencies
pip install -r requirements.txt

 Usage
 Run API (FastAPI)
cd app
uvicorn main:app --reload


Endpoints:

POST /predict → send transaction data, get fraud probability

GET /health → check service status

API is live on Render:
👉 https://fraud-api-in8d.onrender.com

 Run Dashboard (Streamlit)
cd dashboard
streamlit run streamlit_app.py


Dashboard is live on Render:
👉 https://fraud-detection-cloud.onrender.com

🧠 Model Training

Prepare dataset in /data.

Preprocess:

python model/preprocess_data.py


Train XGBoost:

python model/train_model.py


Evaluate & save:

python model/evaluate_model.py


 A pre-trained XGBoost model (xgb_fraud_model.pkl) is included.

 Logging

Logs are stored in project root:

api.log → API requests

fraud.log → Detected frauds

daily_summary.log → Daily stats

info.log → System activity

☁️ Deployment

API → Dockerized and deployed on Render.

Dashboard → Streamlit app deployed on Render.

Database → PostgreSQL (Render free tier).

Run locally with Docker Compose:

docker-compose up --build

** Future Improvements

Add Kafka for real-time log streaming.

Build React dashboard with alerts & filters.

CI/CD with GitHub Actions.

Integrate Prometheus + Grafana for monitoring.

** License

MIT License

