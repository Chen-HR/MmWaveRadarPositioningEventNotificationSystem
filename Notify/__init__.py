try:
  from .Email import EmailBot, Email
  from .LineBot import LineBot
  from .ZenBot import ZenBot
  from .ZenBot import RobotFace as ZenBotFace
except ImportError:
  from Email import EmailBot, Email
  from ZenBot import ZenBot
  from ZenBot import RobotFace as ZenBotFace