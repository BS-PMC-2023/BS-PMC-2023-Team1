pipeline {
    agent {
         docker {
             image 'numpy/numpy-gitpod'
         }
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm // Checkout your source code from your version control system (e.g., Git)
            }
        }
        
        stage('Build') {
            steps {
                sh """
                    id
                    export HOME=/tmp
                    env | sort
                    ls -la \${HOME}
                    pip install -r requirements.txt --user
                    python manage.py migrate 
                """
            }
        }
        
        stage('Test') {
            steps {
                sh """
                  id
                    export HOME=/tmp
                    env | sort
                    ls -la \${HOME}
                pip install django
                    python manage.py test
                """
            }
        }
    }
}
