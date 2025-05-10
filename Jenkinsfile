stage('Set Up Python Environment') {
    steps {
        script {
            echo "Current working directory: ${pwd()}" // Print the current directory

            // Create virtual environment
            sh 'python3 -m venv venv'

            echo "Contents of venv directory:"
            sh 'ls -l venv'

            echo "Contents of venv/bin directory:"
            sh 'ls -l venv/bin'

            // Check for pip specifically
            sh 'ls -l venv/bin/pip'

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
