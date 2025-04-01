from flask import Flask, request, jsonify, send_from_directory
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__, static_url_path='')

# Email configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USERNAME = "pingprodigicomm@gmail.com"
SMTP_PASSWORD = "oatd iqpa idxs hghi"  # Updated with App Password
RECIPIENT_EMAIL = "pingprodigicomm@gmail.com"

# Add static file handlers
@app.route('/styles.css')
def serve_css():
    return send_from_directory('.', 'styles.css')

@app.route('/images/<path:filename>')
def serve_image(filename):
    return send_from_directory('images', filename)

def send_email(form_data):
    try:
        # Create message
        msg = MIMEMultipart()
        msg['From'] = SMTP_USERNAME
        msg['To'] = RECIPIENT_EMAIL
        msg['Subject'] = f"New Contact Form Submission from {form_data['name']}"

        # Create email body
        body = f"""
        New Contact Form Submission:
        
        Name: {form_data['name']}
        Email: {form_data['email']}
        Phone: {form_data['phone']}
        Company: {form_data.get('company', 'N/A')}
        Company Size: {form_data.get('company-size', 'N/A')}
        Service: {form_data['service']}
        
        Message:
        {form_data['message']}
        
        Submitted on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        """

        msg.attach(MIMEText(body, 'plain'))

        # Send email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            logger.info("Attempting to login to SMTP server...")
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            logger.info("Successfully logged in to SMTP server")
            server.send_message(msg)
            logger.info("Email sent successfully")

        return True
    except Exception as e:
        logger.error(f"Error sending email: {str(e)}")
        return False

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/about')
def serve_about():
    return send_from_directory('.', 'about.html')

@app.route('/services')
def serve_services():
    return send_from_directory('.', 'services.html')

@app.route('/contact')
def serve_contact():
    return send_from_directory('.', 'contact.html')

@app.route('/thanks')
def serve_thanks():
    return send_from_directory('.', 'thanks.html')

@app.route('/submit-form', methods=['POST'])
def submit_form():
    try:
        form_data = request.form.to_dict()
        logger.info("Received form submission")
        
        # Send email
        if send_email(form_data):
            logger.info("Form processed successfully")
            return jsonify({
                'success': True,
                'message': 'Form submitted successfully'
            })
        else:
            logger.error("Failed to send email")
            return jsonify({
                'success': False,
                'message': 'Failed to send email'
            }), 500
            
    except Exception as e:
        logger.error(f"Error processing form: {str(e)}")
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500

@app.route('/submit-call-form', methods=['POST'])
def submit_call_form():
    try:
        form_data = request.form.to_dict()
        logger.info("Received call form submission")
        
        # Create message for call form
        msg = MIMEMultipart()
        msg['From'] = SMTP_USERNAME
        msg['To'] = RECIPIENT_EMAIL
        msg['Subject'] = f"New Call Request from {form_data['name']}"

        # Create email body for call form
        body = f"""
        New Call Request:
        
        Name: {form_data['name']}
        Phone: {form_data['phone']}
        Preferred Time: {form_data.get('preferred-time', 'N/A')}
        
        Submitted on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        """

        msg.attach(MIMEText(body, 'plain'))

        # Send email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            logger.info("Attempting to login to SMTP server for call form...")
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            logger.info("Successfully logged in to SMTP server")
            server.send_message(msg)
            logger.info("Call form email sent successfully")

        return jsonify({
            'success': True,
            'message': 'Call request submitted successfully'
        })
            
    except Exception as e:
        logger.error(f"Error processing call form: {str(e)}")
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500

if __name__ == '__main__':
    try:
        port = 8080
        logger.info(f"Starting server on port {port}")
        app.run(host='0.0.0.0', port=port, debug=True)
    except Exception as e:
        logger.error(f"Failed to start server: {str(e)}") 