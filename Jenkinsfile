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

        stage('Preprocessing') {
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

            stage('Metrics 1 - Code Complexity ') {
            steps {

                    sh """
                     id
                    export HOME=/tmp
                        DJANGO_SETTINGS_MODULE='FakeNews.settings'
                        pip install radon
                        PATH='/tmp/.local/bin'
                         radon cc --show-complexity --total-average .
                        """
            }
        }

        stage('Metrics 2 - Covrage ') {
            steps {

                    sh """
                     id
                    export HOME=/tmp
                        DJANGO_SETTINGS_MODULE='FakeNews.settings'
                        pip install coverage
                        PATH='/tmp/.local/bin'
                        coverage run manage.py test
                        coverage report
                        """
            }
        }
}







    }
