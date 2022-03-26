from PIL import Image as pillow
from datetime import datetime
import glob, os

size = 384, 128

newimage = pillow.new(pillow.getmodetype('L'), size, "#FFF")

newimage.save("daily " + datetime.today().strftime('%Y-%m-%d') + ".png", "PNG")