# SWE-455 Homework 1: Cloud Application Deployment

This repository contains a Flask web application that serves as both the deployed application and the homework documentation.

## Live Demo
[Deployed Application URL] - *To be updated after AWS deployment*

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
*To be updated after deployment with:*
- Chosen cloud platform and services
- Deployment configuration
- Auto-scaling settings
- Monitoring setup and metrics

## Screenshots
*To be added after deployment:*
- Application running in browser
- Cloud platform dashboard
- Monitoring metrics

## Author
Mohammed Alyousif

## Submission Details
- **Course**: SWE-455 Cloud Application Engineering
- **Assignment**: Homework 01
- **Due Date**: February 23, 2025
- **Submission Date**: February 25, 2025
