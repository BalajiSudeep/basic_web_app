pipeline {
    agent any

    environment {
        VIRTUAL_ENV = './venv'
        PATH = "$VIRTUAL_ENV/bin:$PATH"
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
                    echo "Current working directory: ${pwd()}"
                    sh 'python3 -m venv venv'

                    echo "Contents of venv/bin directory:"
                    sh 'ls -l venv/bin'

                    echo "Activating virtual environment"
                    sh '. venv/bin/activate'

                    echo "Which pip after (attempted) activation:"
                    sh 'which pip'
                    sh './venv/bin/pip --version' // Explicitly call virtual env pip
                    sh 'python3 --version'
                    sh 'which python3'

                    echo "Ensuring pip is installed/upgraded within venv"
                    sh './venv/bin/python -m ensurepip --upgrade'
                    sh './venv/bin/pip --version' // Verify virtual env pip version
                    sh './venv/bin/pip install --upgrade pip --break-system-packages' // Explicit upgrade with override
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
                    sh './venv/bin/python app.py'
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
