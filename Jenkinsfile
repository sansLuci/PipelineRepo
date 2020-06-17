pipeline {
  agent any
  
  stages {
    stage('build') {
      steps {
      	sh 'PATH=${PATH}:/usr/local/bin'
        sh 'pip install -r requirements.txt'
      }
    }
    stage('test') {
      steps {
        sh 'pytest test_Calculator.py -v'
      }   
    }
  }
}