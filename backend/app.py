import requests 
from flask import Flask, jsonify , render_template

app = Flask(__name__)

JENKINS_URL = "http://localhost:8080/job/devops-pipeline/lastBuild/api/json"
JENKINS_USER = "ry"
JENKINS_TOKEN = "11359df710fab57fd9201b0eb3556fa627"

def get_jenkins_data():
    try:
        response = requests.get(JENKINS_URL, auth=(JENKINS_USER, JENKINS_TOKEN))
        data = response.json()

        build_number = data.get("number", "N/A")
        status = data.get("result", "Unknown")  # This gets the actual build status
        duration = round(data.get("duration", 0) / 1000, 2)  # Convert from ms to sec

        return {
            "build_number": build_number,
            "status": status,
            "duration": duration
        }
    except Exception as e:
        print(f"Error fetching Jenkins data: {e}")
        return {
            "build_number": "N/A",
            "status": "Unknown",
            "duration": 0
        }
@app.route("/")
def home():
    return render_template("dashboard.html")  

@app.route('/jenkins-stats')
def jenkins_stats():
    return jsonify(get_jenkins_data())

if __name__ == '__main__':
    app.run(debug=True)
