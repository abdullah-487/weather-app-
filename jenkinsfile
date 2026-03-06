pipeline {
    agent any

    stages {

        stage('Clone Code') {
            steps {
                git 'https://github.com/abdullah-487/weather-app-.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Run Weather App') {
            steps {
                sh 'python3 app.py'
            }
        }

    }
}
