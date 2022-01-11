from PIL import Image

def bilde():

  datne = "15.11./download.jpeg"

  with Image.open(datne) as im:
    print(datne, im.format, f"{im.size}x{im.mode}")
    im.show()
    izmers = (50,50)
    im.thumbnail(izmers)
    im.save("15.11./maza_bilde.jpg", im.format)
    im.show()

bilde()
    
