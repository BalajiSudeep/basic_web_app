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
                    sh 'ls -l ${VENV_DIR}/bin'
                    sh './${VENV_DIR}/bin/python -m ensurepip --upgrade'
                    sh './${VENV_DIR}/bin/python --version'
                    sh './${VENV_DIR}/bin/python -m pip --version'
                    
                    // Use a compatible pip version (e.g., 25.1.1 for Python 3.12)
                    sh './${VENV_DIR}/bin/python -m pip install pip==25.1.1'
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                sh './${VENV_DIR}/bin/python -m pip install -r requirements.txt'
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
