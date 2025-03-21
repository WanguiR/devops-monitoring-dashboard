pipeline {
    agent any 

    stages
        stage ('Clone Repo'){
            steps {
                git Clone 'https://github.com/WanguiR/devops-monitoring-dashboard.git'
            }
        }
        stage ('install dependencies'){
            steps{
                sh 'pip install -r requirements.txt'
            }
        }
}