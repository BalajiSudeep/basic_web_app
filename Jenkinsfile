pipeline {
    agent any

    environment {
        // Define any environment variables here
        VENV_PATH = './venv'
    }

    stages {
        stage('Checkout SCM') {
            steps {
                // Checkout the latest code from the repository
                checkout scm
            }
        }

        stage('Set Up Python Environment') {
            steps {
                script {
                    // Set up Python virtual environment
                    sh 'python3 -m venv venv'
                    // Ensure pip is available (without upgrading)
                    sh './venv/bin/python -m ensurepip --upgrade'
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Install dependencies from requirements.txt
                    sh './venv/bin/pip install -r requirements.txt'
                }
            }
        }

        stage('Run App') {
            steps {
                script {
                    // Run the application (you may need to adjust this for your app)
                    sh './venv/bin/python app.py'
                }
            }
        }
    }

    post {
        always {
            // Clean up or notify based on the result
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

