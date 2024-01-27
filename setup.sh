pip3 install pyserial==3.5 numpy==1.26.0 matplotlib==3.8.1 line-bot-sdk==2.4.2

git clone https://github.com/Chen-HR/Ti_MmWave_Demo_Driver.git
git clone https://github.com/Chen-HR/MmWaveRadarSystem.git
git clone https://github.com/Chen-HR/HAClusteringTool.git
git clone https://github.com/Chen-HR/MmWaveRadarPositioningSystem.git

unzip "Packages\pyzenbo_v1.0.46.2220.zip" -d "Packages\pyzenbo_v1.0.46.2220"
cd Packages/pyzenbo_v1.0.46.2220/pyzenbo
python setup.py install
cd ../../..
