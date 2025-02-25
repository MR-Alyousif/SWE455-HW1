# SWE-455 Homework 1: Cloud Application Deployment

This repository contains a Flask web application that serves as both the deployed application and the homework documentation.

## Live Demo
http://swe455-hw1-env.eba-xyzabc123.us-east-1.elasticbeanstalk.com/ - *AWS Elastic Beanstalk URL*

## Project Overview
This project demonstrates the deployment of a cloud-based web application, fulfilling the requirements of SWE-455 Homework 1. The application serves as both the deliverable and its own documentation, featuring:

- A Flask web application with Tailwind CSS for modern styling
- AWS Cloud deployment with auto-scaling configuration
- AWS CloudWatch monitoring and metrics visualization
- Comprehensive documentation of the deployment process

## Technical Stack
- **Backend**: Python Flask
- **Frontend**: HTML with Tailwind CSS
- **Cloud Platform**: Amazon Web Services (AWS)
  - AWS Elastic Beanstalk for application deployment
  - Auto Scaling for handling traffic
  - CloudWatch for monitoring
- **Monitoring**: AWS CloudWatch

## Project Structure
- `app.py` - Main Flask application
- `templates/` - HTML templates with Tailwind CSS
- `requirements.txt` - Python dependencies
- `README.md` - Project documentation

## Local Development Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/MR-Alyousif/SWE455-HW1.git
   cd SWE455-HW1
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   # Windows
   .\.venv\Scripts\activate
   # Unix/MacOS
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Visit `http://localhost:5000` in your browser

## Cloud Deployment Details
### AWS Services Used
- **AWS Elastic Beanstalk**: For hosting the Flask application
- **AWS CodePipeline**: For continuous integration and deployment
- **AWS CodeBuild**: For building the application
- **AWS CloudWatch**: For monitoring application metrics

### Deployment Configuration
- **Platform**: Python 3.9 running on 64bit Amazon Linux 2
- **Environment Type**: Load balanced environment
- **Instance Type**: t2.micro
- **Health Reporting**: Enhanced

### Auto-scaling Settings
```yaml
aws:autoscaling:asg:
  MinSize: 2
  MaxSize: 5
aws:autoscaling:trigger:
  MeasureName: CPUUtilization
  Statistic: Average
  Unit: Percent
  Period: 300
  BreachDuration: 300
  UpperThreshold: 70
  LowerThreshold: 30
  UpperBreachScaleIncrement: 1
  LowerBreachScaleIncrement: -1
```

### Monitoring Setup
- **CloudWatch Metrics**: CPU Utilization, Network I/O, Request Count
- **Alarms**: Set for high CPU utilization (>80% for 5 minutes)
- **Logs**: Application logs sent to CloudWatch Logs

## Screenshots
### Application Running in Browser
![Application Screenshot](assets/app_screenshot.png)

### AWS Dashboard
![AWS Dashboard](assets/CodePipline/Success.png)

### Monitoring Metrics
![CloudWatch Metrics](assets/cloudwatch_metrics.png)

## Author
Mohammed Alyousif

## Submission Details
- **Course**: SWE-455 Cloud Application Engineering
- **Assignment**: Homework 01
- **Due Date**: February 25, 2025
- **Submission Date**: February 25, 2025

## Deployment Steps

### 1. AWS Account Setup
- Created AWS account and configured IAM permissions
- Set up access keys for local development

### 2. Local Development and Testing
- Developed Flask application with Tailwind CSS
- Tested locally to ensure functionality
- Created necessary configuration files (.ebextensions, buildspec.yml)

### 3. AWS Elastic Beanstalk Setup
- Created a new Elastic Beanstalk application
- Configured environment settings (Python platform, load balancing)
- Set up auto-scaling configuration

### 4. AWS CodePipeline Configuration
- Created a new pipeline connected to GitHub repository
- Configured source, build, and deploy stages
- Set up webhook for automatic deployments on code changes

### 5. Monitoring and Testing
- Enabled CloudWatch monitoring
- Tested the application under load
- Verified auto-scaling functionality
