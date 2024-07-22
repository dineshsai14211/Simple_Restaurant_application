pipeline {
    agent any

    environment{
        img_tag = "${BUILD_NUMBER}"
    }

    stages{
        stage('Checkout'){
            steps{
                checkout scmGit(branches: [[name: '*/main']], extensions: [],
                userRemoteConfigs: [[credentialsId: 'github', url: 'https://github.com/dineshsai14211/Simple_Restaurant_application']])
            }
        }

        stage('Build Docker'){
            steps{
                script{
                sh '''
                   docker build -t dineshsai14211/simple-restaurant-app-img:${img_tag} .
                   echo "Build Docker Success"
                '''
                }
            }
        }

        stage('Push Docker Image'){
            steps{
                script{
                    withDockerRegistry(credentialsId: 'docker'){
                    sh '''
                    docker push  dineshsai14211/simple-restaurant-app-img:${img_tag}
                    echo "Image Pushed to DockerHub"
                     '''
                    }
                }
            }
        }

        stage('Update the Manifeast files'){
            steps{
                script{
                    withCredentials([gitUsernamePassword(credentialsId: 'github', gitToolName: 'Default')]){

                    sh '''
                      cat kube-manifest/deployment.yml
                      git config  user.email "dinesh@example.com"
                      git config  user.name "dinesh"

                      sed -i "s/simple-restaurant-app-img.*/simple-restaurant-app-img:${BUILD_NUMBER}/g" kube-manifest/deployment.yml
                      cd kube-manifest
                      git add *
                      git commit -m "Image tag has changed"
                      git remote -v
                      git push origin HEAD:main
                    '''
                    }
                }
            }
        }
    }
}

