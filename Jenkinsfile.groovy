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
                sh 'python3 orchestrator/main.py'
            }
        }

        stage('Load Testing') {
            steps {
                sh './scripts/load_test.sh'
            }
        }
    }
}
