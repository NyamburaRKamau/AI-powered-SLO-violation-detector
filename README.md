🚀 AI-Powered SLO Violation Detector

An intelligent system that predicts potential Service Level Objective (SLO) violations in real-time using machine learning. Designed to empower SRE and DevOps teams with proactive insights and fast incident prevention.

🔧 Built With
Tech Description
🧠 Machine Learning Random Forest Classifier
🧼 Data Preprocessing StandardScaler
📊 Pandas & NumPy Feature engineering and EDA
🐍 FastAPI API for real-time prediction
🔁 Uvicorn Lightning-fast ASGI server
🧪 Swagger UI Beautiful API testing interface
💾 Joblib Model serialization
🧪 Scikit-learn Training & evaluation

📁 Project Structure
AI-Powered-SLO-Violation-Detector/
├── slo_data.csv
├── model_training.ipynb
├── slo_violation_model.pkl
├── scaler.pkl
├── main.py
├── requirements.txt
└── README.md

⚙️ How It Works 1. Data Input: System metrics like CPU, memory, latency, error rate, disk I/O 2. Model Prediction: ML model detects if an SLO violation is likely 3. Real-Time API: Query the API with live data, get immediate insights

▶️ Run Locally
git clone https://github.com/roseemaryy/AI-Powered-Violation-Detector.git
cd AI-Powered-Violation-Detector

# (Optional) Use virtual environment

python -m venv venv
source venv/bin/activate

# Install dependencies

pip install -r requirements.txt

# Run FastAPI server

uvicorn main:app --reload

📦 Example Request
POST /predict

{
"cpu_usage": 73.2,
"memory_usage": 85.0,
"request_latency": 450,
"error_rate": 0.15,
"disk_io": 110.4
}

✅ Response
{
"slo_violation": 1
}

💼 Use Cases
• Proactive SRE Monitoring
• Incident Root Cause Detection
• Infrastructure Performance Intelligence
• SLA/SLO Governance

✨ Author

Rosemary Kamau
MLOps Engineer | DevOps | Azure | SRE
🚀 Focused on building intelligent systems that make companies smarter and faster.
