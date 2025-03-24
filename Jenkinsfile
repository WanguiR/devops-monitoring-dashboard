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
                python3 -m venv venv
                source venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }
     } 
}
