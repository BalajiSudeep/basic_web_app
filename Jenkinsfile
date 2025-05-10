pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
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
                    echo "Current working directory: ${pwd()}"
                    sh 'python3 -m venv ${VENV_DIR}'
                    sh 'ls -l ${VENV_DIR}'
                    sh 'ls -l ${VENV_DIR}/bin'
                    sh './${VENV_DIR}/bin/python -m ensurepip --upgrade'
                    sh './${VENV_DIR}/bin/python --version'
                    sh './${VENV_DIR}/bin/pip --version'
                    sh './${VENV_DIR}/bin/pip install --upgrade pip'
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                sh './${VENV_DIR}/bin/pip install -r requirements.txt'
            }
        }

        stage('Run App') {
            steps {
                sh './${VENV_DIR}/bin/python app.py'
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

