"""
File: blur.py
Name:
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    newimg = SimpleImage.blank(300, 300)
    for x in range(300):
        for y in range(300):
            totalr = 0
            totalg = 0
            totalb = 0
            divby = 9
            for x2 in range(-1, 2, 1):
                for y2 in range(-1, 2, 1):
                    if x+x2 < 0 or x+x2 > 299 or y+y2 < 0 or y+y2 > 299:
                        divby -= 1
                    else:
                        pixT = img.get_pix(x+x2, y+y2)
                        r, g, b = pixT
                        totalr += r
                        totalg += g
                        totalb += b
            totalr = round(totalr/divby)
            totalg = round(totalg/divby)
            totalb = round(totalb/divby)
            newimg.set_rgb(x, y, totalr, totalg, totalb)
    return newimg


def main():
    """
    TODO:
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()
    blurred_img = blur(old_img)
    for i in range(4):
        blurred_img = blur(blurred_img)
    blurred_img.show()


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
