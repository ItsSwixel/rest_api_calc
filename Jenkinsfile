pipeline {

  environment {
    PROJECT_DIR = "/app"
    REGISTRY = "swixel/rest_api_calc"
    DOCKER_CREDENTIALS = "docker_auth"
    DOCKER_IMAGE = ""
  }

  agent any

  options {
    skipStagesAfterUnstable()
  }

  stages {

    stage("Cloning the code from git") {
      steps {
        git 'https://github.com/ItsSwixel/rest_api_calc.git'
      }
    }
  }
}
