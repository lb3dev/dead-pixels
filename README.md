dead-pixels
===============

dead-pixels is a simple Python 3 program built to display full screen background colors for monitor dead pixel inspections, using the Tkinter library included with Python 3

Build Notes
-----

### Windows 10

Install pyinstaller dependencies with the requirements.txt in the project, and then build as one executable:

``pyinstaller --onefile --windowed --add-data "icons/dead-pixels.ico;icons" --icon icons/dead-pixels.ico -n dead-pixels main.py``

Convert png to .ico (with ImageMagick):

``magick convert dead-pixels.png ( -clone 0 -resize 64x64 ) ( -clone 0 -resize 48x48 ) ( -clone 0 -resize 32x32 ) ( -clone 0 -resize 16x16 ) dead-pixels.ico``


Controls
---------

``Left Arrow`` or ``A`` key to cycle backgrounds to the left

``Right Arrow`` or ``D`` key or ``Left Mouse Click`` to cycle backgrounds to the right

``Escape`` key or ``Right Mouse Click`` to exit the program immediately

