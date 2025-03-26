# OTP-Validation-Console-Based-Project
Here’s a `README.md` file description for your OTP Validation Console-Based Project:  

---

# OTP Validation Console-Based Project  

## Description  
This is a simple Python-based console application for OTP (One-Time Password) validation using email. The script generates a random OTP, sends it to a predefined list of email addresses, and verifies the OTP entered by the user.  

## Features  
- Generates a random 4-digit OTP.  
- Sends the OTP via email using SMTP.  
- Verifies the OTP entered by the user.  
- Ensures security by validating the received OTP.  

## Requirements  
- Python 3.x  
- `smtplib` (Built-in module)  
- `email.mime` (Built-in module)  

## Setup & Usage  
1. Clone this repository:  
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```  
2. Ensure you have an SMTP-enabled Gmail account. Enable **Less Secure Apps** or **App Passwords** for authentication.  
3. Modify the script with your email credentials and recipient list.  
4. Run the script:  
   ```bash
   python OTP-Validation-Console-Based-Project.py
   ```  
5. Enter the OTP received in the email when prompted.  

## Security Note  
- Avoid hardcoding credentials in the script. Instead, use environment variables or configuration files.  
- App Passwords are recommended instead of using your direct Gmail password.  

