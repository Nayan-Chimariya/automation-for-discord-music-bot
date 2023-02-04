import mss
import mss.tools
import time
from PIL import Image
import pytesseract
import numpy as np

pytesseract.pytesseract.tesseract_cmd = "C:\\Users\\is\\tesseract.exe"

def screenshot():
    with mss.mss() as sct:
        monitor = {"top": 45, "left": 135, "width": 700, "height": 30}
        output = "sct-{top}x{left}_{width}x{height}.jpeg".format(**monitor)
        time.sleep(5)
        sct_img = sct.grab(monitor)
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
        print(output)

    im = Image.open(output)
    im = im.resize((3500,150),Image.Resampling.LANCZOS)
    im.save(fp="resize.png",dpi=(600,600))

def ocr():
    filename = 'resize.png'
    img = np.array(Image.open(filename))
    text = pytesseract.image_to_string(img)
    link = text.replace(" ", "")
    return link
    

    