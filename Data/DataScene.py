import dataclasses
import typing

try:
  from .DataArea import Areas
  from .DataNotify import Notify
except ImportError:
  from DataArea import Areas
  from DataNotify import Notify

@dataclasses.dataclass
class Event:
  type: int
  targetArea: Areas = dataclasses.field(default_factory=Areas)
  sourcesArea: typing.Optional[Areas] = None
  notify: Notify = dataclasses.field(default_factory=Notify)

@dataclasses.dataclass
class Scene:
  name: str = ""
  area: Areas = dataclasses.field(default_factory=Areas)
  events: typing.List[Event] = dataclasses.field(default_factory=list)