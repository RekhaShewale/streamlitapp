pipeline{
	agent {
		node{
			label 'jenkins-slave-node'
		}
	}
	stages{
		stage("Checkout Code"){
			steps{
				git url:"https://github.com/RekhaShewale/streamlitapp.git", branch:'main'
			}
		}
		
		stage("Build Docker image"){
			steps{
				sh 'docker build -t myimage .'
			}
		}
				
   	      	stage('Add tag and Push Image') {
              		steps {
               			withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                 			sh 'echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin'
                    			sh 'docker tag myimage $DOCKER_USERNAME/myimage'
                    			sh 'docker push $DOCKER_USERNAME/myimage'
		                }
                       }
     	   }

	}
}