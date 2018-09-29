# HoneycompPlacer
Simple Script to place Honeycomp-Skins for Rainmeter

In order to use the Script and apply it to your Skins you need to add an extra option to each Skin that should be placed by my script. 
The name of the option can be configured in the Script and the value needs to be a number.
This number is later used to create groups so you can have multiple comps.

Images need to be in 512x512 and then need to be cropped by imageCropper.py.
In order for the Script to run, you will need to insall `pillow`

```$ pip install pillow```

imageCropper will cut the borders and makes it easyer to align the comps

If your comps are not 90px high (set in the Skin itself, not the image height) you will need to change that in the Script, same goes for the width.

## Editing the Script

After your images are cropped and you set the group for all your Skins you will need to edit the Script.
- Open placer.py:

Set the path to your rainmeter.ini (the file will be backedup by the script, every time it runs)
``` python
rainmeterini = "C:/Users/Lukas/AppData/Roaming/Rainmeter/Rainmeter.ini"
```
Set the name you used for your grouping
``` python
groupname = "honey_group"
```
Change the sizes if your skins don't use the 90px height
``` python
compHeight = 90
compWidth = 74
```

