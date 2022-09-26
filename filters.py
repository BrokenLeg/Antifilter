from PIL import Image

class Filter:

    def __init__(self, filter_function, h, w):
        self.filt = filter_function
        self.height = h
        self.width = w
        
    def apply(self, img_pixels, new_pixels):

        for x in range(self.height):
            for y in range(self.width):
                new_pixels[x, y] = self.filt(img_pixels[x, y])

class Chain_Filter:

    def __init__(self):
        self.filters = []

    def add(self, new_filter):
        self.filters.append(new_filter)

    def apply(self, img_pixels, new_pixels):

        for filt in self.filters:
            filt.apply(img_pixels, new_pixels)

def f1(pixel):

    r, g, b = pixel

    return (r, g, b//2)

def f2(pixel):

    r, g, b = pixel

    return (r, (g+b), b*10)

def f3(pixel):

    r, g, b = pixel

    return (r//2, g, b)

img = Image.open("img.jpg")
new_img = Image.new('RGB', (img.size[0], img.size[1]))

pixels = img.load()
pixels_processed = new_img.load()

filt1 = Filter(f1, img.size[0], img.size[1])
filt2 = Filter(f2, img.size[0], img.size[1])
filt3 = Filter(f3, img.size[0], img.size[1])

chain = Chain_Filter()

chain.add(filt1)
chain.add(filt2)
chain.add(filt3)

chain.apply(pixels, pixels_processed)

new_img.show();

