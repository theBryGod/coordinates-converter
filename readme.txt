CBA's COORDINATES CONVERTER
-   A command-line interface application that converts multiple coordinates from PRS92 to WGS84 and vice-versa.

* FEATURES
-   Allows the conversion of multiple coordinates at once for the geodetic reference systems used in the Philippines. (Supports the conversion of PRS92 coordinates to WGS84 and vice-versa as of the latest release.)
-   It also allows the conversion of coordinates within the same geodetic reference system from one format to another (such as the conversion of WGS84 coordinates from degrees to UTM format).
-   TO-DO: Implement a Graphical User Interface (GUI) to enchance user experience and accessibility.
-   TO-DO: Implement the usage of coordinates in degrees using the Degrees, Minutes, Seconds format. (The application only supports the usage of Decimal Degrees as of the latest release.)

* USER INSTRUCTIONS
-   To use this program, you must prepare the input coordinates in a comma-separated values (CSV) file in X, Y (Easting, Northing or Longitude, Latitude) format.
-   As of the current release, the CSV file must then be placed in the same directory as the executable in order for the application to detect the file.

* CREDITS
-   This application uses the following programming languages and packages:
    >   Python 3
    >   pyproj - Python interface to PROJ (cartographic projections and coordinate transformations library)
    >   PyInstaller - Bundles a Python application and all its dependencies into a single package

* LICENSE
-   MIT