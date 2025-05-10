pipeline {
    agent any

    environment {
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
                    
                    // Debugging: List contents of the virtual environment's bin directory
                    sh 'ls -al ./venv/bin/'
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Install dependencies using python -m pip to avoid issues with pip not being executable
                    sh './venv/bin/python -m pip install -r requirements.txt'
                }
            }
        }

        stage('Run App') {
            steps {
                script {
                    // Check if the app file exists before running it
                    sh 'ls -al'

                    // Run the application (replace with your app's run command if necessary)
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

