from shutil import copyfile
from datetime import datetime
from subprocess import call
import configparser

rainmeterini = "C:/Users/Lukas/AppData/Roaming/Rainmeter/Rainmeter.ini"
groupname = "honey_group"

compHeight = 90
compWidth = 74
compCount = 0

#backup file for safety
now = datetime.now()
copyfile(rainmeterini, rainmeterini + "." + now.strftime("%m.%d-%H_%M_%S") + ".back")

config = configparser.ConfigParser()
config.read(rainmeterini, encoding="utf-16")

#Settings for placing the Honeycomp:
# group = 1
# yOffset = 200
# xOffset = 500

# group = 2
# yOffset = 450
# xOffset = 200

group = 3
yOffset = 750
xOffset = 450

# group = 4
# yOffset = 1100
# xOffset = 300

for section in config.sections():
    skingroup = config[section].get(groupname) 
    if skingroup:
        if int(skingroup) == group:
            #windowX = int(config[section].get("WindowX"))
            #windowY = int(config[section].get("WindowY"))

            if compCount == 0:
                windowX = xOffset
                windowY = yOffset
            elif compCount == 1:
                windowX = xOffset - compWidth 
                windowY = yOffset
            elif compCount == 2:
                windowX = xOffset - compWidth * 0.5
                windowY = yOffset - compHeight * 0.75 - 1
            elif compCount == 3:
                windowX = xOffset - compWidth * 0.5
                windowY = yOffset + compHeight * 0.75 + 1
            elif compCount == 4:
                windowX = xOffset + compWidth * 0.5
                windowY = yOffset - compHeight * 0.75 - 1
            elif compCount == 5:
                windowX = xOffset + compWidth
                windowY = yOffset
            elif compCount == 6:
                windowX = xOffset + compWidth * 0.5
                windowY = yOffset + compHeight * 0.75 + 1
            else:
                break

            config.set(section, "WindowX", str(windowX))
            config.set(section, "WindowY", str(windowY))
            compCount = compCount + 1

file = open(rainmeterini, "w", encoding="utf-16")
config.write(file)

call(["C:/Program Files/Rainmeter/Rainmeter.exe", "!RefreshApp"])