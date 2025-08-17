# Autoclicker
An autoclicker I made after getting paranoid over malware with the ones you can just download.

## Usage
CONTROL + ALT + C to start the autoclicking and vice versa.

Click Speed - Pretty self-explanatory; The speed at which the program clicks at (measured in milliseconds)
Click Vary - Random variance between clicks, for example: 1000ms click speed with 100ms click vary will click with a delay of 1000-1100ms. 
## Download
In the releases tab on the right (on PC).

## "Compiling"
1. Install pyinstaller with the commandline using `pip install pyinstaller`
2. Open the directory in the commandline and paste this line: `pyinstaller --onefile --noconsole --icon icon0.ico main.py`
