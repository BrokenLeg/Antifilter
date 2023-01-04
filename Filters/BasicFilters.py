from PIL import Image

class IFilter:

    def apply(self, srcImage, dstImage):
        pass

class OnePixelFilter(IFilter):

    def __init__(self, filterFucntion):
        self.filterFunction = filterFucntion
    
    def apply(self, srcImage, dstImage):
        if (srcImage.size != dstImage.size):
            return

        srcImageArray = srcImage.load()
        dstImageArray = dstImage.load()

        for x in range(srcImage.size[0]):
            for y in range(srcImage.size[1]):
                dstImageArray[x, y] = self.filterFunction(srcImageArray[x, y]);

class CombineFilter(IFilter):
    def __init__(self, admixedImage, level):
        self.admixedImage = admixedImage
        self.level = level

    def apply(self, srcImage, dstImage):
        if (srcImage.size != dstImage.size):
            return

        if (srcImage.size != self.admixedImage.size):
            return

        srcImageArray = srcImage.load()
        dstImageArray = dstImage.load()
        admixImageArray = self.admixedImage.load()

        for x in range(srcImage.size[0]):
            for y in range(srcImage.size[1]):

                currentLevel = y/srcImage.size[1];

                if (currentLevel < self.level):
                    dstImageArray[x, y] = admixImageArray[x, y]
                else:
                    dstImageArray[x, y] = srcImageArray[x, y]

def blackWhite(pixel):
    r, g, b = pixel

    total = (r + g + b)//3

    return (total, total, total)

def onlyRed(pixel):
    r, g, b = pixel

    total = (r + g + b) // 3

    return (r, 0, 0)

def onlyBlue(pixel):
    r, g, b = pixel

    total = (r + g + b) // 3

    return (0, 0, b)

def onlyGreen(pixel):
    r, g, b = pixel

    total = (r + g + b) // 3

    return (0, g, 0)

blackWhiteFilter = OnePixelFilter(blackWhite)
redFilter = OnePixelFilter(onlyRed)
greenFilter = OnePixelFilter(onlyGreen)
blueFilter = OnePixelFilter(onlyBlue)


