import requests
from flask import Flask, jsonify, render_template


app = Flask(__name__)

JENKINS_URL = "http://localhost:8080"
JOB_NAME = "devops-pipeline"
USERNAME = "ry"
API_TOKEN = "11359df710fab57fd9201b0eb3556fa627"

def get_jenkins_data():
    url = f"{JENKINS_URL}/job/{JOB_NAME}/lastBuild/api/json"
    response = requests.get(url, auth=(USERNAME, API_TOKEN))

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Unauthorized", "status_code": response.status_code}
    
@app.route ('/')
def home():
    return render_template("dashboard.html")

@app.route('/jenkins-stats')
def jenkins_stats():
    return jsonify(get_jenkins_data())

if __name__ == '__main__':
    app.run(debug=True, port=5000)
