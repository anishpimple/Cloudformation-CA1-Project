# Automated Flask Application Deployment

This project demonstrates an automated cloud deployment pipeline for a containerized Flask application using AWS CloudFormation, Ansible, Docker, and GitHub Actions. The implementation provides a complete end-to-end automation solution from infrastructure provisioning to continuous deployment.

## Project Overview

The project creates a seamless deployment pipeline with the following components:

- **Infrastructure as Code**: AWS CloudFormation for provisioning cloud resources
- **Configuration Management**: Ansible for server configuration and application deployment
- **Containerization**: Docker for application packaging and isolation
- **CI/CD Pipeline**: GitHub Actions for automated deployment on code changes


The deployment architecture includes:

1. An EC2 instance provisioned using CloudFormation
2. Docker installed and configured via Ansible
3. A Flask application containerized with Docker
4. GitHub Actions for continuous deployment

## Prerequisites

To use this project, you'll need:

- An AWS account with appropriate permissions
- A GitHub account
- Basic knowledge of AWS, Docker, and GitHub Actions
- Python 3.8+ installed for local development

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

### 2. Configure AWS Credentials

Store your AWS credentials as GitHub secrets:

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_REGION`
- 'EC2_PUBLIC_IP'

Also, create an SSH key for deployment and add it as `SSH_PRIVATE_KEY` in your GitHub secrets.

### 3. Deploy the Infrastructure

The infrastructure is deployed using the CloudFormation template:

```json
{
  "Description": "CloudFormation script to set up an EC2 instance in AWS with Docker installed",
  "Resources": {
    "WebServerInstance": {
      "Type": "AWS::EC2::Instance",
      ...
    }
  }
}
```

### 4. Update the Inventory File

Update the `NetworkSec.ini` file with your EC2 instance's IP address:

```ini
[webserver]
your-ec2-ip ansible_user=ec2-user ansible_ssh_private_key_file=~/.ssh/id_rsa
```

## CI/CD Pipeline

The project uses GitHub Actions for continuous deployment. When code changes are pushed to the main branch, the workflow:

1. Checks out the repository
2. Sets up the SSH connection to the EC2 instance
3. Runs Ansible playbooks to deploy the application

The workflow is defined in `.github/workflows/deploy.yml`:

```yaml
name: Deploy Flask App

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest
    
    steps:
      # Workflow steps...
```

## Application Structure

```
├── cloudformationsetup.json  # AWS CloudFormation template
├── ConfigDocker.yml         # Ansible playbook for Docker setup
├── flask-app/               # Flask application
│   ├── app.py              # Main application file
│   ├── Dockerfile          # Container definition
│   ├── requirements.txt    # Python dependencies
│   └── deploy_flask.yml    # Ansible deployment playbook
├── NetworkSec.ini          # Ansible inventory
└── .github/workflows/      # GitHub Actions workflows
    └── deploy.yml         # Deployment workflow
```

## Flask Application

The application is a simple Flask web server:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Hello from Flask in Docker!</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
```

## Docker Configuration

The application is containerized using the following Dockerfile:

```dockerfile
FROM python:3.9
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 80
CMD ["python", "app.py"]
```

## Ansible Deployment

The Flask application is deployed using Ansible:

```yaml
- name: Deploy Flask App in Docker
  hosts: webserver
  become: yes
  tasks:
    # Deployment tasks...
```

## Troubleshooting

### Common Issues

1. **Python Version Compatibility**: Ensure Python 3.8+ is installed on the EC2 instance.
2. **SSH Connection Issues**: Verify that the SSH key permissions are correct (chmod 600) and the key is properly configured in GitHub secrets.
3. **Container Not Starting**: Check Docker logs with `docker logs my-flask-app`.
4. **Website Unreachable**: Ensure the EC2 security group allows inbound traffic on port 80.

### Debugging Commands

```bash
# Check if container is running
docker ps

# View container logs
docker logs my-flask-app

# Test local connectivity
curl localhost:80

# Check port bindings
sudo netstat -tulpn | grep 80
```

## Future Improvements

- Add proper health checks after deployment
- Implement blue-green deployment strategy
- Add automated testing before deployment
- Set up monitoring and alerting
- Configure HTTPS with Let's Encrypt
- Implement database integration
- Add load balancing for high availability
