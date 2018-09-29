# HoneycompPlacer
Simple Script to place Honeycomp-Skins for Rainmeter

<p align="center">
  <img src="./honeycomp.JPG" alt="Example"
       width="787" height="576">
</p>

Currently only uses up to 7 Comps per Honeycomp this is due to me not beeing able to see a pattern in the creation of the Honeycomps :S For now the locations are kind of hardcoded. If you have an idea how to create a dynamic Honeycomp-Pattern feel free to open up a pull request.

Images need to be in 512x512 and then need to be cropped by imageCropper.py.
In order for the Script to run, you will need to insall `pillow`

```$ pip install pillow```

imageCropper will cut the borders and makes it easyer to align the comps

If your comps are not 90px high (set in the Skin itself, not the image height) you will need to change that in the Script, same goes for the width.

## Editing Rainmeter.ini
In order to use the Script and apply it to your Skins you need to add an extra option to each Skin that is supposed to be placed by my script. 
The name of the option can be configured in the Script and the value needs to be a number.
This number is later used to create groups so you can have multiple comps.
``` ini
[Authentic Weather]
active = 1
windowx = 2632
windowy = 466
clickthrough = 1
draggable = 0
snapedges = 1
keeponscreen = 1
alwaysontop = 0

[Honeycomb\word]
active = 1
windowx = 300
windowy = 1100
clickthrough = 0
draggable = 1
snapedges = 1
keeponscreen = 1
alwaysontop = 0
honey_group = 1
```
Here you can see, only Honeycomp\word has the group 1 and Authentic Weather has no group.
All Skins with the same groupnumber will form a Honeycomp

## Editing the Script

- Open imageCropper.py:

Set the path to your images use a wildcard e.g.: `*.png` to ensure only the right images are cropped
``` python
imagesPath = "C:/Users/Lukas/Documents/Rainmeter/Skins/Honeycomb/@Resources/Images/*.png"
```
Now backup all your images (just in case :D) and run the script. This Script kinda only works if your images use the template provided by honeycomp-Skin and are 512x512 in size.

After your images are cropped and you set the group for all your Skins you will need to edit the main Script.
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
Now the important part. Set the x and y offset for the center Comp. All other Comps will be build arround that one.
``` python
group = 3 # the group that will be changed
yOffset = 750
xOffset = 450
```
On the end of the Script set the path to your rainmeter installation. This will automatically refresh all Skins after the Script ran.
``` python
call(["C:/Program Files/Rainmeter/Rainmeter.exe", "!RefreshApp"])
```
And now run the script and see all your set Skins to get Honeycomped :)
