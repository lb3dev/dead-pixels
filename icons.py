from PIL import Image

icon = Image.open('icons/dead-pixels.png')
icon.save('icons/dead-pixels.ico', sizes=[(255, 255)])
