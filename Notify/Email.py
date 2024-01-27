"""
## EmailBot

### `Email` Class

- **Attributes:**
  - `host` (str): The email server host.
  - `port` (int): The port number for the email server.
  - `name` (str): The name associated with the email.
  - `user` (str): The username for authentication.
  - `password` (str): The password for authentication.

### `EmailBot` Class

- **Methods:**
  - `__init__(self, email: Email)`: Initializes an EmailBot instance with the provided `Email` object.
  - `send(self, receivers: list[str], title: str, content: str) -> bool`: Sends an email to the specified receivers with the given title and content.
    - `receivers` (list[str]): List of email addresses to receive the email.
    - `title` (str): Subject of the email.
    - `content` (str): Body/content of the email.
    - Returns `True` if the email is sent successfully; otherwise, `False`.

### EmailBot Usage Examples

```python
# Creating an EmailBot instance
email = EmailBot(Email(host="smtp.example.com", port=587, name="John Doe", user="john@example.com", password="password"))

# Sending an email
receivers = ["recipient1@example.com", "recipient2@example.com"]
title = "Sample Subject"
content = "This is a sample email content."
result = email.send(receivers, title, content)

if result:
    print("Email sent successfully.")
else:
    print("Failed to send email.")
```
"""
import dataclasses

import smtplib
from email.message import EmailMessage

@dataclasses.dataclass
class Email:
  host: str
  port: int
  name: str
  user: str
  password: str
class EmailBot:
  def __init__(self, email: Email):
    self.email = email
  def send(self, receivers: list[str], title: str, content: str):
    # if self.state_isLogin is not: return False
    smtpServer = smtplib.SMTP(self.email.host, self.email.port)
    smtpServer.starttls()
    smtpServer.login(f"{self.email.user}", self.email.password)
    data = EmailMessage()
    data.set_content(content)
    data['subject'] = title
    data['from'] = f"{self.email.user}@{self.email.host}"
    data['to'] = receivers
    smtpServer.login(f"{self.email.user}", self.email.password)
    return smtpServer.send_message(data)

# if __name__ == "__main__":
#   senders = [
#     {
#       "host": "smtp.example.com", 
#       "port": 587, 
#       "name": "John Doe", 
#       "user": "john@example.com", 
#       "password": "password"
#     }
#   ]
#   receivers = [
#     "recipient1@example.com", 
#     "recipient2@example.com"
#   ]
#   for sender in senders:
#     email = EmailBot(Email(host = sender["host"], port = sender["port"], name = sender["name"],  user = sender["user"],  password = sender["password"]))
#     email.send(receivers, "Email().send()", "EmailBot(Email(host, port, name,  user,  password)).send(receivers, title, content)")