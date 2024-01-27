# %% 
import time
import datetime

from MmWaveRadarPositioningSystem.CoordinateSystem_Conversion_3D import Conversion_CoordinateSystem_3D as CoordinateSystem_3D_Convertor
from MmWaveRadarPositioningSystem.CoordinateSystem_Conversion_3D import Rotation as CoordinateSystem_3D_Convertor_RotationMatrix
from MmWaveRadarPositioningSystem.CoordinateSystem_Conversion_3D import Translation as CoordinateSystem_3D_Convertor_TranslationMatrix
from MmWaveRadarPositioningSystem import MmWaveDevice, MmWaveRadarSystem, MmWaveRadarCompositeSystem, MmWaveRadarPositioningSystem
from MmWaveRadarSystem import Timer
import Data
import Notify

try:
  from . import Config
except ImportError:
  import Config

# %%
timer = Timer()
mode = ""
if Config.language == "zh-TW":  
  if Config.mode == "Home Security"   : mode = "居家安全"
  if Config.mode == "Error statistics": mode = "誤差統計"
  if Config.mode == "Area Detection"  : mode = "區域檢測"
if Config.language == "en-US":  
  if Config.mode == "Home Security"   : mode = "Home Security"
  if Config.mode == "Error statistics": mode = "Error statistics"
  if Config.mode == "Area Detection"  : mode = "Area Detection"

timer.start()
mmWaveRadarPositioningSystem = MmWaveRadarPositioningSystem(
  compositeSystem=MmWaveRadarCompositeSystem(
    radarSystems=[
      MmWaveRadarSystem(
        mmWaveDevice=MmWaveDevice(
          platform           = Config.device.platform, 
          Ctrl_port_name     = Config.device.Ctrl_port_name, 
          Data_port_name     = Config.device.Data_port_name, 
          Ctrl_port_baudrate = Config.device.Ctrl_port_baudrate, 
          Data_port_baudrate = Config.device.Data_port_baudrate, 
          log_enable         = Config.device.log,
          log_echo           = Config.device.log
        ),
        mmWaveDevice_profile = Config.device.Profile, 
        threshold_dB=Config.device.CfarRangeThreshold_dB, 
        removeStaticClutter=Config.device.RemoveStaticClutter, 
        framePeriodicity_ms=Config.device.FramePeriodicity_ms, 
        log_enable=Config.device.log
      )
    ],
    converters=[
      CoordinateSystem_3D_Convertor(CoordinateSystem_3D_Convertor_RotationMatrix(0, 0, 0), CoordinateSystem_3D_Convertor_TranslationMatrix(0, 0, 0))
    ],
    log_enabled = Config.device.log
  ),
  clusterRadius = Config.detection.limit,
  interval_ms   = Config.device.FramePeriodicity_ms, 
  log_enabled   = Config.device.log
)
if Config.debug: print(f"[{datetime.datetime.now()}] MmWaveRadarPositioningSystem.init(): Millimeter wave Radar Positioning System configuration completed, used for a total of {timer.now()} second")

timer.start()
if Config.alerter.emailBot.enabled: Notify_EmailBot = Notify.EmailBot(Notify.Email(Config.alerter.emailBot.host, Config.alerter.emailBot.port, Config.alerter.emailBot.name, Config.alerter.emailBot.user, Config.alerter.emailBot.password))
if Config.alerter.lineBot .enabled: Notify_LineBot  = Notify.LineBot(Config.alerter.lineBot.access_token)
if Config.alerter.zenBot  .enabled: 
  Notify_ZenBot= Notify.ZenBot(Config.alerter.zenBot.host)
  Notify_ZenBot.expression(facial = Notify.ZenBotFace.DEFAULT, sentence=f"毫米波雷達定位系統啟動，開啟{mode}模式")
if Config.debug: print(f"[{datetime.datetime.now()}] Alart configuration completed, used for a total of {timer.now()} second")

mmWaveRadarPositioningSystem.start()
try:
  if Config.mode == "Home Security":
    records = list()
    while True:
      timer.start()
      positioningPoints = mmWaveRadarPositioningSystem.positioning()
      if Config.debug: print(f"[{datetime.datetime.now()}] MmWaveRadarPositioningSystem.positioning: {positioningPoints}")
      for positioningPoint in positioningPoints:
        for event in Config.scene.events:
          alert = False
          if event.targetArea.include(Data.Point.parse_tuple(positioningPoint)):
            if event.type == 0: 
              for point in [point for points in records for point in points]:
                if not event.targetArea.include(Data.Point.parse_tuple(point)): alert = True
            if event.type == 1: 
              for point in [point for points in records for point in points]:
                if event.sourcesArea.include(Data.Point.parse_tuple(point)): alert = True
          if alert:
            if Config.alerter.emailBot.enabled: Notify_EmailBot.send([user.email for user in Config.users], event.notify.email.title, event.notify.email.content.format(datetime.datetime.now()))
            if Config.alerter.lineBot .enabled: Notify_LineBot .multicast([user.lineId for user in Config.users], event.notify.line.message.format(datetime.datetime.now()))
            if Config.alerter.zenBot  .enabled: Notify_ZenBot  .expression(facial = Notify.ZenBotFace.DEFAULT, sentence=event.notify.zenbot.message)
            if Config.debug: print(f"[{datetime.datetime.now()}] Notify: {event.notify.zenbot.message}")
      records.append(positioningPoints)
      if len(records) > Config.detection.TimeToLive: records.pop(0)
      while timer.now() < Config.device.FramePeriodicity_ms/1000: pass
except KeyboardInterrupt:
  if Config.alerter.zenBot.enabled: Notify_ZenBot.expression(sentence="毫米波雷達定位系統關閉")