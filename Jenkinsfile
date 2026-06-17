pipeline {
    agent any

    environment {
        // Your EC2 instance public IP address
        EC2_IP          = '16.16.242.152'
        EC2_USER        = 'ubuntu'
        
        // The ID of your private SSH key (.pem) saved inside Jenkins Credentials
        SSH_CREDENTIALS_ID = 'ec2-ssh-key' 
    }

    stages {
        stage('Deploy & Build on EC2') {
            steps {
                // Securely fetches your .pem key from Jenkins credentials manager
                sshagent(credentials: ["${SSH_CREDENTIALS_ID}"]) {
                    
                    echo "Connecting to EC2 instance to fetch latest code and build..."
                    
                    // 1. SSH into EC2, go to project folder, pull latest code, and restart containers
                    bat """
                        ssh -o StrictHostKeyChecking=no ${EC2_USER}@${EC2_IP} "
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