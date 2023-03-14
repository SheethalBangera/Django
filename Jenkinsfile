pipeline {
<<<<<<< HEAD
  environment {
    imagename = "sharanyajayaram/trialpython"
    dockerImage = ''
  }
=======
//   environment {
//     imagename = "sharanyajayaram/trialpython"
//     dockerImage = ''
//   }
>>>>>>> development_anusha
  agent any
    options { 
        timestamps ()
        timeout(time: 2, unit: 'MINUTES')   
        skipDefaultCheckout true
        buildDiscarder(logRotator(numToKeepStr: '2'))
    }
  stages {
    stage('Code checkout') {
      steps {
        checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'gitcred', url: 'https://github.com/chaitanyapriya123/Basic_signup.git']])
      }
    }
      stage('Building image') {
      steps{
        //script {
<<<<<<< HEAD
        sh 'dockerImage = docker.build imagename'
=======
        sh 'docker build -t shrth7/devops .'
>>>>>>> development_anusha
       // }
      }
    }
    stage('Deploy Image to dockerhub') {
      steps{
        // sh 'dockerImage.push("latest")'
<<<<<<< HEAD
          withCredentials([usernamePassword(credentialsId: 'dockerid', passwordVariable: 'dockeridPassword', usernameVariable: 'dockeridUser')]) {
            sh "docker login -u ${env.dockeridUser} -p ${env.dockeridPassword}"
            sh 'docker push sharanyajayaram/trialpython:latest'
=======
          withCredentials([usernamePassword(credentialsId: 'DockerCreds', passwordVariable: 'DockerCredsPassword', usernameVariable: 'DockerCredsUser')]) {
            sh "docker login -u ${env.DockerCredsUser} -p ${env.DockerCredsPassword}"
            sh 'docker push shrth7/devops:latest'
>>>>>>> development_anusha
          }
      }
    }
    stage('Run the container'){
      steps{
<<<<<<< HEAD
      sh '''docker pull sharanyajayaram/trialpython:latest"
      docker run -d -t -p 8000:8000 --name trialcont${BUILD_NUMBER} sharanyajayaram/trialpython:latest
      docker stop --time=60 trialcont${BUILD_NUMBER}
      docker system prune -af'''
=======
      sh '''docker pull shrth7/devops:latest
      docker run -d -t -p 8000:8000 --name trialcont${BUILD_NUMBER} shrth7/devops:latest
      docker ps -a
      docker stop --time=60 trialcont${BUILD_NUMBER}

      '''
>>>>>>> development_anusha
      }
    }
 }
    post{
          success{
              sh 'echo "Container is up and running"'
          }
      }
      }
