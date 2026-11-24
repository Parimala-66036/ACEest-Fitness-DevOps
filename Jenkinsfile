
pipeline {
    agent any

    environment {
        IMAGE_NAME = 'parimala66036/aceest-fitness'
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv .venv
                    .venv/bin/python -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run Automated Tests') {
            steps {
                sh '''
                    .venv/bin/python -m pytest -v \
                        --junitxml=test-results.xml
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build \
                        -t ${IMAGE_NAME}:build-${BUILD_NUMBER} \
                        -t ${IMAGE_NAME}:latest .
                '''
            }
        }

        stage('Test Inside Docker') {
            steps {
                sh '''
                    touch test-results-docker.xml

                    docker run --rm \
                        -v "$WORKSPACE/test-results-docker.xml:/app/test-results-docker.xml" \
                        ${IMAGE_NAME}:build-${BUILD_NUMBER} \
                        python -m pytest -v \
                        --junitxml=/app/test-results-docker.xml
                '''
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-creds',
                        usernameVariable: 'DOCKERHUB_USER',
                        passwordVariable: 'DOCKERHUB_TOKEN'
                    )
                ]) {
                    sh '''
                        set +x
                        echo "$DOCKERHUB_TOKEN" | docker login \
                            -u "$DOCKERHUB_USER" --password-stdin

                        docker push ${IMAGE_NAME}:build-${BUILD_NUMBER}
                        docker push ${IMAGE_NAME}:latest

                        docker logout
                    '''
                }
            }
        }
    }

    post {
        always {
            junit allowEmptyResults: true,
                  testResults: 'test-results*.xml'
        }

        success {
            echo 'ACEest Fitness pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed. Please check the console output.'
        }
    }
}
