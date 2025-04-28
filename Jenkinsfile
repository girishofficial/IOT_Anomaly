pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-login') // create this Jenkins credential
        DOCKERHUB_USER = 'girish445g'
    }

    stages {
        stage('Clone Code') {
            steps {
                git branch: 'main', url: 'https://github.com/girishofficial/IOT_Anomaly.git'
            }
        }

        stage('Build Docker Images') {
            steps {
                script {
                    def services = ['api_service', 'data_collection_service', 'monitoring_service', 'retraining_service', 'notification_service']
                    for (service in services) {
                        sh """
                        docker build -t ${DOCKERHUB_USER}/${service}:latest ${service}
                        """
                    }
                }
            }
        }

        stage('Login to DockerHub') {
            steps {
                sh "echo ${DOCKERHUB_CREDENTIALS_PSW} | docker login -u ${DOCKERHUB_CREDENTIALS_USR} --password-stdin"
            }
        }

        stage('Push Docker Images') {
            steps {
                script {
                    def services = ['api_service', 'data_collection_service', 'monitoring_service', 'retraining_service', 'notification_service']
                    for (service in services) {
                        sh """
                        docker push ${DOCKERHUB_USER}/${service}:latest
                        """
                    }
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f k8s-manifests/'
            }
        }
    }
}

