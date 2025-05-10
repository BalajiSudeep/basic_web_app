pipeline {
    agent any

    environment {
        PYTHON_ENV = "venv"
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    // Checkout the code from GitHub
                    checkout scm
                }
            }
        }

        stage('Set Up Python Environment') {
            steps {
                script {
                    echo "Setting up Python virtual environment"
                    // Create a virtual environment
                    sh 'python3 -m venv ${PYTHON_ENV}'
                    
                    // Ensure pip is upgraded and works correctly
                    sh './${PYTHON_ENV}/bin/python -m ensurepip --upgrade'
                    sh './${PYTHON_ENV}/bin/python -m pip install --upgrade pip'
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    echo "Installing dependencies from requirements.txt"
                    // Install dependencies
                    sh './${PYTHON_ENV}/bin/python -m pip install -r requirements.txt'
                }
            }
        }

        stage('Run App') {
            steps {
                script {
                    echo "Running the Flask app"
                    // Run the application (adjust the command based on your app)
                    sh './${PYTHON_ENV}/bin/python app.py'
                }
            }
        }
    }

    post {
        always {
            echo "Cleaning up..."
            // Clean up virtual environment after the build
            sh 'rm -rf ${PYTHON_ENV}'
        }
        success {
            echo "Build completed successfully!"
        }
        failure {
            echo "Build failed!"
        }
    }
}
