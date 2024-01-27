

import dataclasses
import typing
from . import Data

mode: str = ""

debug: bool = False

language: str = ""

@dataclasses.dataclass
class MMWaveDevice:
  platform: str = ""
  Ctrl_port_name: str = ""
  Data_port_name: str = ""
  log: bool = False
  Config_File_name: str = ""
  CfarRangeThreshold_dB: float = 9.0
  RemoveStaticClutter: bool = False
  FramePeriodicity: int = 1000
device: MMWaveDevice = MMWaveDevice(
  platform              = "", 
  Ctrl_port_name        = "", 
  Data_port_name        = "", 
  log                   = False, 
  Config_File_name      = "", 
  CfarRangeThreshold_dB = 9.0, 
  RemoveStaticClutter   = False, 
  FramePeriodicity      = 1000
)

@dataclasses.dataclass
class User:
  name: str
  email: typing.Optional[str] = None
  lineId: typing.Optional[str] = None
users: typing.List[User] = [
  User(
    name        = "", 
    email       = None, 
    lineId      = None, 
  )
]
zenbot_host: str = None

@dataclasses.dataclass
class EmailBot:
  enabled: bool = False
  host: str = ""
  port: int = 587
  name: str = ""
  user: str = ""
  password: str = ""
@dataclasses.dataclass
class LineBot:
  enabled: bool = False
  name: str = ""
  access_token: str = ""
@dataclasses.dataclass
class ZenBot:
  enabled: bool = False
  start: str = "Millimeter wave radar system started"
  stop: str = "Millimeter wave radar system shutdown"
@dataclasses.dataclass
class Alerter:
  emailBot: EmailBot = dataclasses.field(default_factory=EmailBot)
  lineBot: LineBot = dataclasses.field(default_factory=LineBot)
  zenBot: ZenBot = dataclasses.field(default_factory=ZenBot)
alerter: Alerter = Alerter(
  EmailBot(
    enabled  = False, 
    host     = "", 
    port     = 587, 
    name     = "", 
    user     = "", 
    password = ""
  ), 
  LineBot(
    enabled      = False,
    name         = "",
    access_token = ""
  ), 
  ZenBot(
    enabled = False, 
    start   = "Millimeter wave radar system started", 
    stop    = "Millimeter wave radar system shutdown"
  )
)

@dataclasses.dataclass
class Detection:
  limit: float = 0.75
  TimeToLive: int = 5
  scale: float = 1.0
detection: Detection = Detection(
  limit      = 0.75,
  TimeToLive = 20,
  scale      = 1.0
)

scene: Data.Scene = Data.Scene(
  name    = "",
  area    = Data.Areas(),
  events  = list()
)