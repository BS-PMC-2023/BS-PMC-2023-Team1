pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm // Checkout your source code from your version control system (e.g., Git)
            }
        }
        
        stage('Preprocessing - python install') {
            steps {
                sudo apt-get install python3-venv
            }
        }
        
        stage('Build') {
            steps {
                sh 'python3 -m venv venv' // Create a virtual environment
                sh 'source venv/bin/activate' // Activate the virtual environment
                sh 'pip install -r requirements.txt' // Install project dependencies inside the virtual environment
                sh 'python manage.py collectstatic --noinput' // Collect static files
                sh 'python manage.py migrate' // Apply database migrations
                sh 'python manage.py test' // Run tests
            }
        }
    }
}
