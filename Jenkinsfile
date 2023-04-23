pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm // Checkout your source code from your version control system (e.g., Git)
            }
        }
        
        stage('Build') {
            steps {
                sh 'apt-get install -y python3-venv' // Install the Python 3 virtual environment package
                sh 'python3 -m venv venv' // Create a virtual environment
                sh 'source venv/bin/activate' // Activate the virtual environment
                sh 'pip install -r requirements.txt' // Install project dependencies inside the virtual environment
                sh 'python manage.py collectstatic --noinput' // Collect static files
                sh 'python manage.py migrate' // Apply database migrations
            }
        }
    }
}
