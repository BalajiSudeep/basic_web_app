pipeline {
    agent any

    environment {
        VIRTUAL_ENV = './venv'  // Define path for the virtual environment
    }

    stages {
        stage('Declarative: Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Set Up Python Environment') {
            steps {
                script {
                    // Create virtual environment
                    sh 'python3 -m venv venv'

                    // Ensure pip is installed and upgrade it
                    sh 'venv/bin/python -m ensurepip --upgrade'
                    sh 'venv/bin/pip install --upgrade pip'  // Upgrade pip
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Install dependencies from requirements.txt
                    sh 'venv/bin/pip install -r requirements.txt'
                }
            }
        }

        stage('Run App') {
            steps {
                script {
                    // Run your Flask app (or any app you want to run)
                    sh 'venv/bin/python app.py'  // Assuming `app.py` is the entry point
                }
            }
        }
    }

    post {
        always {
            echo 'Build completed!'
        }
        success {
            echo 'Build succeeded!'
        }
        failure {
            echo 'Build failed!'
        }
    }
}

