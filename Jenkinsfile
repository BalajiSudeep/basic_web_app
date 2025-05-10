pipeline {
    agent any

    environment {
        VIRTUAL_ENV = './venv'
        PATH = "$VIRTUAL_ENV/bin:$PATH"
    }

    stages {
        stage('Declarative: Checkout SCM') {
            steps { // <-- This 'steps' block was missing
                checkout scm
            }
        }

        stage('Set Up Python Environment') {
            steps { // <-- This 'steps' block was missing
                script {
                    echo "Current working directory: ${pwd()}"

                    sh 'python3 -m venv venv'

                    echo "Contents of venv directory:"
                    sh 'ls -l venv'

                    echo "Contents of venv/bin directory:"
                    sh 'ls -l venv/bin'

                    echo "Checking for pip explicitly:"
                    sh 'ls -l venv/bin/pip'

                    // Try using the full path
                    echo "Checking with full path:"
                    sh "ls -l ${WORKSPACE}/venv/bin/pip"

                    // Activate the virtual environment
                    sh '. venv/bin/activate'

                    // Verify pip after activation
                    echo "Which pip after activation:"
                    sh 'which pip'
                    sh 'pip --version'
                    sh 'python3 --version'
                    sh 'which python3'

                    sh 'venv/bin/python -m ensurepip --upgrade'
                    sh 'pip --version'
                    sh 'pip install --upgrade pip'
                }
            }
        }

        stage('Install Dependencies') {
            steps { // <-- This 'steps' block was missing
                script {
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Run App') {
            steps { // <-- This 'steps' block was missing
                script {
                    sh 'python app.py'
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
