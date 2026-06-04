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
                bat 'C:\\Users\\korudenko\\AppData\\Local\\Python\\pythoncore-3.14-64\\python.exe -m pip install -r requirements.txt'
            }
        }

        stage('Run Orchestrator') {
            steps {
                bat 'C:\\Users\\korudenko\\AppData\\Local\\Python\\pythoncore-3.14-64\\python.exe orchestrator/main.py'
            }
        }

        stage('Load Testing') {
            steps {
                bat 'scripts\\load_test.bat'
            }
        }
    }
}