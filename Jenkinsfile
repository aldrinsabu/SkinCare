pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    credentialsId: 'skincareID', 
                    url: 'https://github.com/aldrinsabu/SkinCare.git'
            }
        }
        stage('Build') {
            steps {
                echo 'Building project...'
                // Add build steps here
            }
        }
        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                // Add test execution commands here
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                // Add deployment steps here
            }
        }
    }
}
