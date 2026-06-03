pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/Kosten-73/CICDJob.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install PyGithub'
                bat 'pip install requests'
                bat 'pip install python-jira'  // если используете Jira
                // bat 'pip install -r requirements.txt'  // если есть файл
            }
        }

        stage('Run Orchestrator') {
            steps {
                bat 'python orchestrator/main.py'
            }
        }

        stage('Load Testing') {
            steps {
                bat 'echo Running load tests...'
                bat 'scripts\\load_test.bat'
            }
        }
    }
}