import dataclasses
import typing

@dataclasses.dataclass
class Line:
  message: str

@dataclasses.dataclass
class Zenbot:
  message: str

@dataclasses.dataclass
class Email:
  title: str
  content: str

@dataclasses.dataclass
class Notify:
  line: typing.Optional[Line] = None
  zenbot: typing.Optional[Zenbot] = None
  email: typing.Optional[Email] = None