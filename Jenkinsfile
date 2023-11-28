pipeline{
  agent any
  stages { 
    stage('building fronend image...') {
      steps { 
        sh 'docker build -t n01551957/python_app:latest .'
          } 
        }
    stage('building backend image'){
      agent { docker { image 'mysql:latest'}}
      steps{
        sh 'mysql --version'
      }
    }
    stage('Login') {
      steps {
      	withCredentials([usernamePassword(credentialsId: 'DockerHubID', passwordVariable: 'dockerHubPassword', usernameVariable: 'dockerHubUser')]) {
        	sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPassword} docker.io "
        }
      }
     }
    stage('Push image') {
       steps {
             	withCredentials([usernamePassword(credentialsId: 'DockerHubID', passwordVariable: 'dockerHubPassword', usernameVariable: 'dockerHubUser')]) {
        sh "docker push n01551957/python_app:latest"
            }
       }
    }
}
}
