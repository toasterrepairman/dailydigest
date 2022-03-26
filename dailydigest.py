from PIL import Image as pillow
from datetime import datetime
import glob, os

# size notes:
# width of the image should not exceed 384 pixels (max width of thermal printer)
# height should allow for a 128-pixel header and footer file on either end
# height should also reserve space for tasks (todo)
size = 384, 128

newimage = pillow.new(pillow.getmodetype('L'), size, "#FFF")

newimage.save("daily " + datetime.today().strftime('%Y-%m-%d') + ".jpg", "JPEG")