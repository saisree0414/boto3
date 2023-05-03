import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Set up the JFrog Artifactory URL and token
artifactory_url = 'https://example.com/artifactory'
access_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

# Define the expiry date for the identity token
expiry_date = '2023-06-01'

# Define the email parameters
sender_email = 'sender@example.com'
sender_password = 'password'
recipient_email = 'recipient@example.com'
subject = 'JFrog Artifactory Identity Token Expiry'

# Check if the token has expired
response = requests.get(f'{artifactory_url}/api/security/token', headers={'Authorization': f'Bearer {access_token}'})
if response.status_code == 200:
    data = response.json()
    if data.get('validUntil', '') < expiry_date:
        # Build the email message
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject
        body = f'Your JFrog Artifactory identity token will expire on {expiry_date}. Please renew the token before then.'
        message.attach(MIMEText(body, 'plain'))

        # Set up the SMTP server and send the email
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        text = message.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()
else:
    print(f'Error checking token expiry: {response.status_code} - {response.text}')
