pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout code from GitHub repository
                checkout scm
            }
        }

        stage('Set Up Python Environment') {
            steps {
                script {
                    echo "Setting up Python virtual environment"

                    // Create a Python virtual environment
                    sh 'python3 -m venv ${VENV_DIR}'

                    // Ensure that pip is upgraded inside the virtual environment
                    sh './${VENV_DIR}/bin/python -m ensurepip --upgrade'

                    // Display Python version and pip version inside virtual environment
                    sh './${VENV_DIR}/bin/python --version'
                    sh './${VENV_DIR}/bin/python -m pip --version'
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Install the required dependencies from requirements.txt
                    echo "Installing dependencies"
                    sh './${VENV_DIR}/bin/python -m pip install -r requirements.txt'
                }
            }
        }

        stage('Run App') {
            steps {
                script {
                    echo "Running the application"
                    // Run Flask app in the background and on all interfaces
                    sh './${VENV_DIR}/bin/python app.py &'
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
