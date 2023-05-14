pipeline {
    agent {
         docker {
             image 'python:3-alpine'
         }
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm // Checkout your source code from your version control system (e.g., Git)
            }
        }
        
        stage('Build') {
            steps{
             script {
                    sh 'python -m venv venv'
                    sh 'source venv/bin/activate'
                    sh 'pip install -r requirements.txt'
                    sh 'python manage.py collectstatic --noinput'
                    sh 'python manage.py migrate'



            }
        }
        
        stage('Test') {
            steps {
                sh """
                    python manage.py test
                """
            }
        }
    }
}
