import random

def image():
    imagefile = open('image.ppm', 'w')
    imagefile.write("P3\n")
    imagefile.write("500 500\n")
    imagefile.write("255\n\n")

    for x in range(0,500):
        factor = random.randint(40, 256)
        hmm = random.randint(30, 256)
        if (hmm > 10):
            hmm -= 10
        for y in range(500):
            x = random.randint(1, 30)
            if (x % 2) == 0:
                r = factor
                g = factor
                b = 0
            else:
                r = 0
                g = hmm * random.randint(1, 150)
                b = hmm * random.randint(150, 200)
            imagefile.write("%d %d %d " % (r, g, b))

    imagefile.close()

image()
