pipeline {
    agent any

    environment {
        EC2_IP          = '16.16.242.152'
        EC2_USER        = 'ubuntu'
        // The ID of your SSH Key credential in Jenkins
        SSH_KEY_ID      = 'ec2-ssh-key' 
    }

    stages {
        stage('Deploy & Build on EC2') {
            steps {
                echo "Connecting to EC2 instance to fetch latest code and build..."
                
                // Securely binds your private key file to a temporary file path variable ($PRIVATE_KEY)
                withCredentials([file(credentialsId: "${SSH_KEY_ID}", variable: 'PRIVATE_KEY')]) {
                    bat """
                        ssh -i "%PRIVATE_KEY%" -o StrictHostKeyChecking=no ${EC2_USER}@${EC2_IP} "
                            cd ~/protostruct3 && \
                            git checkout deploy && \
                            git pull origin deploy && \
                            sudo docker compose down && \
                            sudo docker compose up --build -d
                        "
                    """
                }
            }
        }
    }

    post {
        success {
            echo "Successfully deployed ProtoStruct2 directly on EC2 at http://${EC2_IP}:3000"
        }
        failure {
            echo 'Deployment failed. Check the SSH configuration or EC2 logs.'
        }
    }
}
