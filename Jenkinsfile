def output

pipeline {
    
   agent { docker { image 'python:3.7.7-slim' } }

   stages {
      stage('Hello') {
         steps {
             script {
                 output = sh label: '', returnStdout: true, script: 'echo "Hello, World"'
             }
         }
      }
      stage('echo') {
         steps {
            echo output
         }
      }
	  stage('build') {
		  steps {
			  sh 'python3 --version'
			  sh 'python3 ./fib.py'
		  }
	  }
   }
}
