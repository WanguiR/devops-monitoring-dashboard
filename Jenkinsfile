pipeline {
    agent any 

    stages
        stage ('Clone Repo'){
            steps {
                git 'https://github.com/WanguiR/devops-monitoring-dashboard.git'
            }
        }
        stage ('install dependencies'){
            steps{
                sh 'pip install -r requirements.txt'
            }
        }
}