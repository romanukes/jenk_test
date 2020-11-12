pipeline {
  agent {
    dockerfile {
      filename 'Dockerfile'
    }

  }
  stages {
    stage('test') {
      steps {
        sh 'poetry --version'
      }
    }

  }
  environment {
    PYTHON_VER = '3.9'
  }
}