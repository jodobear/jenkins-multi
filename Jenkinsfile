def output

pipeline {
    
   agent any
   
   tools {
	   go { 'go-1.4' }
   }

   stages {
	   stage('build') {
		   steps {
			   sh 'go build'
		   }
	   }
	   stage('Publish artifact') {
		   steps {
			   archiveArtifacts 'jenkins-multi'
		   }
	   }
   }
}
