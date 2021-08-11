
from PIL import Image, ImageDraw, ImageFont


def createUpdatedImage(subsCount):
    subsCount = "{:,}".format(int(subsCount))
    image = Image.open('background.png')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", size=120)
    (x, y) = (420, 120)
    message = str(subsCount) + " Subs"
    color = 'rgb(0, 0, 0)' # black color
    draw.text((x, y), message, fill=color, font=font)
    draw.text((x+1, y+1), message, fill=color, font=font)
    draw.text((x+1, y+1), message, fill=color, font=font)
    draw.text((x+3, y+3), message, fill=color, font=font)
    image.save('banner.png')


if __name__ == '__main__':
    createUpdatedImage(23418746)
