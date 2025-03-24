pipeline {
    agent any 

    stages{
        stage ('Clone Repo'){
            steps {
                git branch: 'main', url: 'https://github.com/WanguiR/devops-monitoring-dashboard.git', credentialsId: 'a0995e37-3a9e-4b7b-a97a-bf8de37cec10'
            }
        }
        stage ('install dependencies'){
            steps{
                sh '''
                pip install --break-system-packages -r requirements.txt
                '''
            }
        }
        stage ('Restart Flask app') {
            steps {
                sh 'pkill -f app.py || true' // Stop old Flask process if running
                sh 'nohup python3 backend/app.py &'
            }
        }
     } 
}
