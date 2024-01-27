"""
## LineBot

### `LineBot` Class

- **Methods:**
  - `__init__(self, access_token: str)`: Initializes a LineBot instance with the provided Line Messaging API access token.
  - `multicast(self, usersid: list, msg: str)`: Sends a multicast message to the specified user IDs.
    - `usersid` (list): List of user IDs to receive the message.
    - `msg` (str): Message content to be sent.

### LineBot Usage Examples

```python
# Creating a LineBot instance
lineBot = LineBot(access_token="your_line_access_token")

# Sending a multicast message
usersId = ["user1", "user2", "user3"]
message = "Hello from LineBot!"
lineBot.multicast(usersId, message)
```
"""
from linebot import LineBotApi # line-bot-sdk==2.4.2
from linebot.models import TextSendMessage

class LineBot:
  def __init__(self, access_token: str):
    self.API = LineBotApi(access_token)
  def multicast(self, usersid: list, msg: str):
    self.API.multicast(usersid, TextSendMessage(text=msg))

# if __name__ == "__main__":
#   LineBot_API_Access_Tokens: dict[str, str] = {
#     "Name1": "your_line_access_token1", 
#     "Name2": "your_line_access_token2"
#   }
#   usersId = ["user1", "user2", "user3"]
#   for token in LineBot_API_Access_Tokens.values():
#     lineBot = LineBot(access_token=token)
#     lineBot.multicast(usersId, "LineBot.multicast")
