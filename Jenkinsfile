pipeline{
  agent any
  stages { 
    stage('building fronend image') {
      steps { 
        sh 'docker build -t n01551957/python_app:latest .'
          } 
        }
    stage('building backend image'){
      steps{
        sh 'docker build -t n01551957/mysql_db:latest -f SQLdatabase/Dockerfile .'
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
        sh "docker push n01551957/mysql_db:latest"
            }
       }
    }
}
}
