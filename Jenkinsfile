pipeline {
  agent any
  
  stages {
    stage('build') {
      steps {
      	sh 'curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py'
      	sh 'python get-pip.py'
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