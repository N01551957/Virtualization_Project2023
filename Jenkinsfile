pipeline{
  agent { dockerfile true}
  stages { 
    stage('building dockerfile') { 
      steps { 
        sh 'echo building the docker image'
          } 
        } 
    stage ('extra') {
      steps {
        sh 'python --version'
        sh 'flask --version'
      }
    }
  }
}
