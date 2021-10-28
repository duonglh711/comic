pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh """
                    docker-compose build
                    docker-compose up -d
                """
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }

    post {
        always {
            script {
                try {
                    //Delete containers that are not used.
                    sh """
                        yes | docker container prune
                    """
                    //Delete all images with none tags
                    sh """
                        docker images | grep none | awk '{ print \$3; }' | xargs docker rmi
                    """
                } catch (Exception e) {
                    echo 'Exception occurred: ' + e.toString()
                }
            }
        }
        failure {
            echo 'Fail!'
        }
    }
}