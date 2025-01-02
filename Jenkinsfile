pipeline{
	agent any
	stages{
		stage("Checkout Code"){
			steps{
				git url:"https://github.com/RekhaShewale/streamlitapp.git", branch:'main'
			}
		}
		/*
		stage("Cleanup stage"){
			steps{
				sh 'docker rm -f $(docker ps -aq) '
			}
		}
		*/
		stage("Build Docker image"){
			steps{
				sh 'docker build -t myimage .'
			}
		}
		/*
		stage("Create Container"){
			steps{
				sh 'docker run -d -p 8501:8501 myimage'
			}
		}
		*/
		
   	      stage('Build and Push Image') {
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