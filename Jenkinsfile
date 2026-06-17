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
                        :: Copy key to a private directory to isolate it from workspace permissions
                        copy /Y "%PRIVATE_KEY%" "%TEMP%\\ec2_key.pem" >nul
                        
                        :: Force block inheritance and explicitly grant permissions to system and administrators
                        icacls "%TEMP%\\ec2_key.pem" /c /inheritance:r /grant:r *S-1-5-32-544:(F) *S-1-5-18:(F)
                        
                        :: Execute SSH command using the newly secured key file
                        ssh -i "%TEMP%\\ec2_key.pem" -o StrictHostKeyChecking=no ${EC2_USER}@${EC2_IP} "cd ~/protostruct3 && git checkout deploy && git pull origin deploy && sudo docker compose down && sudo docker compose up --build -d"
                        
                        :: Clean up the temporary key copy
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
