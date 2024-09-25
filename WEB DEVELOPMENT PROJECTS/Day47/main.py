from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv


URL = "https://appbrewery.github.io/instant_pot/"
live_url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"


response = requests.get(live_url, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0",
                                           "Accept-Language":"en-US,en;q=0.9"}).text

soup = BeautifulSoup(response, "html.parser")

getTitle = soup.find(name="span", id="productTitle").text
productTitle = getTitle.strip()
getPriceOfpot = soup.find(name="span", class_="aok-offscreen").text
priceOfpot_withDollars = getPriceOfpot.strip().split(" ")[0]
priceOfpot = float(priceOfpot_withDollars.split('$')[1])


# Load environment variables from .env file
load_dotenv()

# Fetch the environment variables
sender_email = os.getenv('EMAIL_USER')
receiver_email = os.getenv('RECEIVER_EMAIL')
password = os.getenv('EMAIL_PASSWORD')

# Set up the email details
subject = "Amazon Price Alert!"
body = f"{productTitle} is now {priceOfpot_withDollars}\n {live_url}"

# Create the email content
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

# Set up the SMTP server and send the email
try:
    if  priceOfpot < 100:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Secure the connection
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Email sent successfully!")

except Exception as e:
    print(f"Failed to send email: {e}")

finally:
    server.quit()
