import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email details
sender_email = "fidelia.100daysofcode@gmail.com"
receiver_email = "godwinjoseph693@gmail.com"
subject = "Test Email"
body = "Hello, this is a test email sent using SMTP in Python."

# Set up the MIME structure
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject

# Attach the body to the email
msg.attach(MIMEText(body, 'plain'))

# SMTP server setup (for Gmail, use 'smtp.gmail.com' and port 587 for TLS)
smtp_server = 'smtp.gmail.com'
smtp_port = 587
password = 'aibl ubyq klkp xkrg'  # Note: use an app-specific password for security

server = None
# Sending the email
try: 
    # Create the SMTP connection
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Secure the connection with TLS
    
    # Log in to your email account
    server.login(sender_email, password)
    
    # Send the email
    server.sendmail(sender_email, receiver_email, msg.as_string())
    
    print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")
finally:
    # Close the connection
    if server:
        server.quit()
