CloudFormation and Flask Deployment

Overview

This project automates the deployment of a Flask application using AWS CloudFormation and Ansible. The application runs inside a Docker container on an EC2 instance.

Project Structure

├── cloudformationsetup.json  # CloudFormation template for infrastructure
├── flask-app/
│   ├── app.py                # Flask application
│   ├── Dockerfile            # Docker setup for the app
│   ├── requirements.txt      # Dependencies
│   ├── deploy_flask.yml      # Ansible playbook to deploy Flask app
├── ConfigDocker.yml          # Docker configuration
├── NetworkSec.ini            # Security configurations
├── README.md                 # Project documentation

Deployment Steps

1️⃣ CloudFormation Setup

Navigate to AWS CloudFormation and create a stack using cloudformationsetup.json.

This will provision an EC2 instance with necessary security groups.

2️⃣ Connect to EC2 Instance

ssh -i Security-key.pem ec2-user@<EC2-PUBLIC-IP>

3️⃣ Install Dependencies

sudo yum update -y
sudo yum install docker -y
sudo service docker start
sudo usermod -aG docker ec2-user
exit

Reconnect to apply changes:

ssh -i Security-key.pem ec2-user@<EC2-PUBLIC-IP>

4️⃣ Deploy Flask App with Docker

cd flask-app
docker build -t flask-app .
docker run -d -p 80:80 flask-app

5️⃣ Verify Deployment

Check if the application is running:

docker ps

Access the app in a browser using http://<EC2-PUBLIC-IP>.

6️⃣ Push to GitHub

git add .
git commit -m "Added CloudFormation and Flask setup"
git push origin main

Future Improvements

Add a custom domain and SSL (Let's Encrypt).

Automate deployment with CI/CD pipelines.

Implement a Load Balancer for high availability.

Done! 🎉 Your Flask app is live on AWS. 🚀

