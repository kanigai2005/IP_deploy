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
                        copy /Y "%PRIVATE_KEY%" "%TEMP%\\ec2_key.pem" >nul
                        icacls "%TEMP%\\ec2_key.pem" /c /inheritance:r /grant:r *S-1-5-32-544:(F) *S-1-5-18:(F)
                        
                        :: Notice we changed 'git checkout deploy' to pull directly into your current active branch
                        ssh -i "%TEMP%\\ec2_key.pem" -o StrictHostKeyChecking=no ${EC2_USER}@${EC2_IP} "cd ~/protostruct3 && git fetch --all && git pull origin main && sudo docker compose down && sudo docker compose up --build -d"
                        
                        del "%TEMP%\\ec2_key.pem"
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
