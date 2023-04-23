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
                sh 'pip install -r requirements.txt' // Install project dependencies
                sh 'python manage.py collectstatic --noinput' // Collect static files
                sh 'python manage.py migrate' // Apply database migrations
                sh 'python manage.py test' // Run tests
            }
        }
    }
}
