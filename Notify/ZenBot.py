"""
## ZenBot

### `ZenBot` Class

- **Methods:**
  - `__init__(self, host: str, timeout: int | float = 10)`: Initializes a ZenBot instance with the specified IP address (host) and optional connection timeout.
  - `connect(self, timeout: int | float = 10)`: Connects to the ZenBot with an optional timeout for the connection.
  - `disconnect(self, timeout: int | float = 10)`: Disconnects from the ZenBot with an optional timeout.
  - `expression(self, facial = RobotFace.DEFAULT, sentence: str | None = None, config = None, sync: bool = True, timeout: int | float = None)`: Sets the facial expression of the ZenBot.
    - `facial`: Facial expression to set (default is `RobotFace.DEFAULT`).
    - `sentence` (str | None): Optional sentence associated with the expression.
    - `config`: Additional configuration for expression.
    - `sync` (bool): Whether to synchronize the expression (default is `True`).
    - `timeout` (int | float): Optional timeout for the expression.

  - `__del__(self)`: Releases resources when the ZenBot instance is deleted.

### ZenBot Usage Examples

```python
# Creating a ZenBot instance
zenBot = ZenBot(host="192.168.31.27")

# Setting expressions
zenBot.expression(facial=RobotFace.DEFAULT, sentence="Testing ZenBot expressions")
```
"""
import time

import pyzenbo # 1.0.46.2220
from pyzenbo.modules.dialog_system import RobotFace

class ZenBot:
  def __init__(self, host: str, timeout: int | float = 10, log: bool = False):
    self.host = host
    self.isConnected = False
    self.timeout = timeout
    self.zenBot = None
    self.log = log
    if self.log: print("self.__init__")
    # self.connect()
  def connect(self):
    if self.log: print("| | self.connect().start")
    if self.isConnected and self.zenBot.get_connection_state() == (1, 1): return
    self.zenBot = pyzenbo.connect(self.host)
    if self.log and self.zenBot.get_connection_state() == (1, 1): print("| | |", self.zenBot.get_connection_state(), "vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv")
    if self.zenBot.get_connection_state() == (1, 1): self.isConnected = True
    # delayedTrigger(self.timeout, self.disconnect)
    if self.log: print("| | self.connect().end")
  def disconnect(self, wait: int | float = 0.5):
    if self.log: print("| | self.disconnect().start")
    if not self.isConnected and self.zenBot.get_connection_state() == (7, 7): return
    self.isConnected = False
    try:
      _ = self.zenBot.release()
      # del self.zenBot
      # self.zenBot = None
      time.sleep(wait)
    except:
      pass
    if self.log and self.zenBot.get_connection_state() == (7, 7): print("| | |", self.zenBot.get_connection_state(), "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    if self.log: print("| | self.disconnect().end")
  def expression(self, facial = RobotFace.DEFAULT, sentence: str | None = None, config = None, sync: bool = True, timeout: int | float = 10, wait: int | float = 1):
    if self.log: print("| self.expression().start")
    if not self.isConnected or self.zenBot == None or self.zenBot.get_connection_state() != (1, 1): self.connect()
    if self.log: print("| | ", self.zenBot)
    return self.zenBot.robot.set_expression(facial, sentence, config, sync, timeout)
    time.sleep(wait)
    # if self.isConnected or self.zenBot != None or self.zenBot.get_connection_state() != (7, 7): self.disconnect()
    if self.log: print("| self.expression().end")
  def speak(self, facial = RobotFace.DEFAULT, sentence: str | None = None, config = None, sync: bool = True, timeout: int | float = 10, wait: int | float = 1):
    if self.log: print("| self.speak().start")
    if not self.isConnected or self.zenBot == None or self.zenBot.get_connection_state() != (1, 1): self.connect()
    if self.log: print("| | ", self.zenBot)
    return self.zenBot.robot.speak( sentence, config, sync, timeout)
    time.sleep(wait)
    # if self.isConnected or self.zenBot != None or self.zenBot.get_connection_state() != (7, 7): self.disconnect()
    if self.log: print("| self.speak().end")
  def __del__(self):
    if self.log: print("self.__del__().start")
    try:
      # if self.isConnected or self.zenBot.get_connection_state() == (7, 7): self.zenBot.release()
      self.disconnect()
    except AttributeError:
      pass

if __name__ == "__main__":
  timeout = 5
  host = "192.168.*.*"
  zenBot = ZenBot(host, timeout)
  zenBot.connect()
  print(zenBot.zenBot.robot.set_expression(facial=RobotFace.HAPPY, sentence="expression")) # have thread and can't auto stop
  print(zenBot.zenBot.robot.speak(sentence="speak")) # have thread and can't auto stop
  time.sleep(1)
  print(zenBot.zenBot.robot.stop_speak())
  time.sleep(1)
  print(zenBot.zenBot.cancel_command_all())

  print(zenBot.expression(sentence="expression", sync=False))
  print(zenBot.expression(facial=RobotFace.HAPPY, sentence="expression", sync=False)) # recall when zenBot not yet disconnect
  print(zenBot.speak(sentence="speak", sync=False))
  time.sleep(timeout*1.5) # wait for zenBot disconnect
  print(zenBot.expression(sentence="expression", sync=False))
  print(zenBot.speak(sentence="speak", sync=False))