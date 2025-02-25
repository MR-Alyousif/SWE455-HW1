from flask import Flask, render_template
import os

# Create the Flask application
app = Flask(__name__)

# Create a Flask route for the root URL
@app.route('/')
def index():
    return render_template('index.html')

# Add a simple health check endpoint
@app.route('/health')
def health():
    return 'OK'

# AWS Elastic Beanstalk expects the application to be named 'application'
application = app

# Run the application if this file is executed directly
if __name__ == '__main__':
    # Get port from environment variable or default to 5000
    port = int(os.environ.get("PORT", 5000))
    # In production, listen on all interfaces
    app.run(host='0.0.0.0', port=port)
