pipeline {
    agent any

    environment {
        EC2_IP          = '16.16.242.152'
        EC2_USER        = 'ubuntu'
        SSH_KEY_ID      = 'ec2-ssh-key' 
    }

    stages {
        stage('Deploy & Build on EC2') {
            steps {
                echo "Connecting to EC2 instance to fetch latest code and build..."
                
                withCredentials([file(credentialsId: "${SSH_KEY_ID}", variable: 'PRIVATE_KEY')]) {
                    bat """
                        @echo off
                        :: Reset permissions and remove inheritance on the temporary key file
                        icacls "%PRIVATE_KEY%" /inheritance:r /grant:r "%USERNAME%":(R)
                        
                        :: Run the deployment pipeline completely via SSH in a single execution string
                        ssh -i "%PRIVATE_KEY%" -o StrictHostKeyChecking=no ${EC2_USER}@${EC2_IP} "cd ~/protostruct3 && git checkout deploy && git pull origin deploy && sudo docker compose down && sudo docker compose up --build -d"
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
