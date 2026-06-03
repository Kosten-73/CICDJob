pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'develop', url: 'https://github.com/Kosten-73/demo.git'
            }
        }

        stage('Run Orchestrator') {
            steps {
                bat 'python3 orchestrator/main.py'
            }
        }

        stage('Load Testing') {
            steps {
                bat './scripts/load_test.sh'
            }
        }
    }
}
