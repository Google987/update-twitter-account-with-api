
from PIL import Image, ImageDraw, ImageFont
import urllib.request


def createUpdatedImage(subsCount, instaCount):
    subsCount = "{:,}".format(int(subsCount))
    image = Image.open('new_background.png')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", size=120)
    (x, y) = (420, 120)
    message = str(subsCount) + " Subs"
    color = 'rgb(0, 0, 0)' # black color
    draw.text((x, y), message, fill=color, font=font)
    draw.text((x+1, y+1), message, fill=color, font=font)
    draw.text((x+1, y+1), message, fill=color, font=font)
    draw.text((x+3, y+3), message, fill=color, font=font)

    #instagram
    font = ImageFont.truetype("arial.ttf", size=25)
    draw.text((100, 10), "@beyou7060", fill=color, font=font)
    draw.text((101, 11), "@beyou7060", fill=color, font=font)
    message = str(instaCount) + " Followers"
    font = ImageFont.truetype("arial.ttf", size=40)
    draw.text((100, 50), message, fill=color, font=font)
    draw.text((101, 51), message, fill=color, font=font)
    image.save('banner.png')


def addFollowers(followers): 
    im1 = Image.open('banner.png')
    startPos = 420
    for follower in followers:
        image_url = follower.profile_image_url_https.replace('_normal.jpg', '_400x400.jpg')
        urllib.request.urlretrieve(image_url, "follower.png")
        im2 = Image.open('follower.png')
        im2 = im2.resize((100, 100))
        mask_im = Image.new("L", im2.size, 0)
        draw = ImageDraw.Draw(mask_im)
        draw.ellipse((0, 0, 100, 100), fill=255)
        mask_im.save('mask_circle.png')
        im1.paste(im2, (startPos, 390), mask_im)
        startPos += 130
    im1.save('new_banner.png')


if __name__ == '__main__':
    createUpdatedImage(23418746, 100)
    # addFollowers()

