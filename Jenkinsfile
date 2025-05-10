pipeline {
    agent any

    environment {
        VIRTUAL_ENV = './venv'  // Define path for the virtual environment
        PATH = "$VIRTUAL_ENV/bin:$PATH"  // Add the virtual environment's bin directory to the PATH
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
                    
                    // Debug: Check if the virtual environment and pip exist
                    sh 'ls -l venv/bin'  // List contents of venv/bin to check if pip is there
                    sh 'which pip'  // Check if pip is on the PATH
                    sh 'python3 -m venv venv'  // Recreate venv just to ensure it is clean
                    sh 'venv/bin/python -m ensurepip --upgrade'  // Ensure pip is installed
                    sh 'ls -l venv/bin'  // Verify pip installation
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

