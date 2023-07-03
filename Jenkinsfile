pipeline{
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub')
    }
    stages{
        stage("Cloning"){
            steps{
                echo "cloning the data..."
            }
        }
        stage("Build"){
            steps{
                echo "Building the app..."
                sh 'docker build -t lloydmatereke/jenkins-docker-hub .'
                echo "Building the app completed..."
            }
        }
        stage('Login') {
            steps {
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
            }
        }
        stage('Push') {
            steps {
                sh 'docker push '
            }
        }
        stage("Pull"){
            steps{
                echo "Pulling the code..."
            }
        }
    } 
}