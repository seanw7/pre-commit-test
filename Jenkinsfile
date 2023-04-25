pipeline {
    agent {
        docker { image 'python:3.9' }
    }
    environment {
        MY_GITHUB_TOKEN = credentials('MY_GITHUB_TOKEN')
        MY_GITHUB_REPO_URL = "https://github.com/seanw7/pre-commit-test.git"
        DOCKER_HOST = 'unix:///var/run/docker.sock'
    }


    stages {
        // stage('Checkout') {
        //     steps {
        //         git '$MY_GITHUB_REPO_URL'
        //     }
        // }
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'pip install pylint'
            }
        }
        stage('Code Quality') {
            steps {

                sh 'pylint --output-format=parseable my_project_folder > pylint.log'
                recordIssues tool: pyLint(pattern: 'pylint.log')
            }
        }
    }
}
