pipeline {
    agent any

    environment {
        VENV_DIR = "venv"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Set Up Python Environment') {
            steps {
                script {
                    sh 'python3 -m venv venv'
                    sh './venv/bin/python -m ensurepip --upgrade'
                    // Use a stable pip version that works with Python 3.12
                    sh './venv/bin/python -m pip install pip==23.3.1'
                    sh './venv/bin/python --version'
                    sh './venv/bin/pip --version'
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    sh './venv/bin/pip install -r requirements.txt'
                }
            }
        }

        stage('Run App') {
            steps {
                script {
                    sh './venv/bin/python app.py &'
                }
            }
        }
    }

    post {
        always {
            echo 'Build completed!'
        }
        failure {
            echo 'Build failed!'
        }
    }
}

