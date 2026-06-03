pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/Kosten-73/CICDJob.git'
            }
        }
        stage('Run Orchestrator') {
            steps {
                bat 'python orchestrator/main.py'
            }
        }
        stage('Load Testing') {
            steps {
                bat 'scripts\\load_test.bat'
            }
        }
    }
}