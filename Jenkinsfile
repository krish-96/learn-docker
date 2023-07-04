pipeline{
    agent any

    // environment {
    //     DOCKERHUB_CREDENTIALS = credentials('dockerhub')
    // }
    stages{
        stage("Cloning"){
            steps{
                echo "cloning the data..."
                git branch: 'main', url: 'https://github.com/krish-96/learn-docker.git'
                 echo "cloning of the data completed..."
                 sh "sudo service docker status"
            }
        }
        stage("Build"){
            steps{
                echo "Building the app..."
                sh 'docker build -t jenkins-docker:latest .'
                sh 'docker run -it --name jenkins-docker --network host -d jenkins-docker'
                echo "Building the app completed..."
            }
        }
        // stage('Login') {
        //     steps {
        //         sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
        //     }
        // }
        // stage('Push') {
        //     steps {
        //         sh 'docker push '
        //     }
        // }
        stage("Pull"){
            steps{
                echo "Pulling the code..."
            }
        }
    } 
}