from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__, template_folder="templates")  
JENKINS_URL = "http://localhost:8080"
JOB_NAME = "devops-pipeline"
USERNAME = "admin"
API_TOKEN = "your_api_token"

def get_jenkins_data():
    url = f"http://localhost:8080/job/devops-pipeline/lastBuild/api/json"
    response = requests.get(url, auth=(USERNAME, API_TOKEN))
    
    if response.status_code == 200:
        data = response.json()
        return {
            "build_number": data.get("number"),
            "status": data.get("result"),
            "duration": data.get("duration") / 1000,  # Convert ms to seconds
            "timestamp": data.get("timestamp")
        }
    else:
        return {"error": "Failed to fetch data from Jenkins"}

# Serve the dashboard
@app.route('/')
def dashboard():
    return render_template("dashboard.html")

# Serve the API endpoint 
@app.route('/jenkins-stats', methods=['GET'])
def jenkins_stats():
    return jsonify(get_jenkins_data())

if __name__ == '__main__':
    app.run(debug=True, port=5000)
