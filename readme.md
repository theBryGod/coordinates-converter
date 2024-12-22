
<h1 align="center">
  <br>
  <img src=https://i.imgur.com/9Yo2UH3.png alt="CBA" width="200">
  <br>
  CBA's Coordinates Converter
  <br>
</h1>

<h4 align="center">A command-line interface application that converts multiple coordinates<br> from PRS92 to WGS84 and vice-versa.</h4>

<p align="center">
  <a href="#features">Features</a> •
  <a href="#user-instructions">User Instructions</a> •
  <a href="#download">Download</a> •
  <a href="#credits">Credits</a> •
  <a href="#license">License</a>
</p>

## Features

* Allows the conversion of multiple coordinates at once for the geodetic reference systems used in the Philippines. <br>
(Supports the conversion of PRS92 coordinates to WGS84 and vice-versa as of the latest release.)
* It also allows the conversion of coordinates within the same geodetic reference system from one format to another (such as the conversion of WGS84 coordinates from degrees to UTM format).
* TO-DO: Implement a Graphical User Interface (GUI) to enchance user experience and accessibility.
* TO-DO: Implement the usage of coordinates in degrees using the Degrees, Minutes, Seconds format.<br>
(The application only supports the usage of Decimal Degrees as of the latest release.)

## User Instructions

To use this program, you must prepare the input coordinates in a comma-separated values (CSV) file in X, Y (Easting, Northing or Longitude, Latitude) format.

As of the current release, the CSV file must then be placed in the same directory as the executable in order for the application to detect the file.

> **Screenshots:**
> <br>The sample input CSV file in the same directory as the executable:
<br><img src="https://i.imgur.com/1IEFruX.png">
<br>The format that the coordinates should be in inside the CSV file (without the comments):
<br><img src="https://i.imgur.com/6QRWhVP.png">

## Download

You can [download](https://github.com/theBryGod/coordinates-converter/releases) the latest version of the application from the releases page.


## Credits

This application uses the following programming languages and packages:

* [Python 3](https://www.python.org/)
* [pyproj - Python interface to PROJ (cartographic projections and coordinate transformations library)](https://pyproj4.github.io/pyproj/stable/)
* [PyInstaller - Bundles a Python application and all its dependencies into a single package](https://pyinstaller.org/en/stable/)

Special thanks to [amitmerchant1990](https://github.com/amitmerchant1990), as I used his README file as a template for my own.
## License

MIT

