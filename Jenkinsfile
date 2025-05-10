pipeline {
    agent any

    environment {
        VENV_DIR = "venv"
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
                    // Create virtual environment and install dependencies
                    sh '''
                        python3 -m venv $VENV_DIR
                        $VENV_DIR/bin/pip install --upgrade pip
                        $VENV_DIR/bin/pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Run App') {
            steps {
                script {
                    // Run the Flask app in the background
                    sh '''
                        nohup $VENV_DIR/bin/python app.py > app.log 2>&1 &
                    '''
                    echo "Flask app started in background. Check app.log for output."
                }
            }
        }
    }

    post {
        success {
            echo "Build and deployment successful!"
        }
        failure {
            echo "Build failed!"
        }
    }
}

