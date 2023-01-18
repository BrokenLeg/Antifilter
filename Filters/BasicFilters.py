from PIL import Image

class IFilter:

    def apply(self, srcImage, dstImage):
        pass

    def getDescription(self):
        pass

    def setDescription(self, description):
        pass

class OnePixelFilter(IFilter):

    def __init__(self, filterFucntion, description):
        self.filterFunction = filterFucntion
        self.description = description
    
    def apply(self, srcImage, dstImage):
        if (srcImage.size != dstImage.size):
            return

        srcImageArray = srcImage.load()
        dstImageArray = dstImage.load()

        for x in range(srcImage.size[0]):
            for y in range(srcImage.size[1]):
                dstImageArray[x, y] = self.filterFunction(srcImageArray[x, y]);

    def getDescription(self):
        return self.description

    def setDescription(self, description):
        self.description = description

class CombineFilter(IFilter):
    def __init__(self, admixedImage, level, description):
        self.admixedImage = admixedImage
        self.level = level
        self.description = description

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

    def getDescription(self):
        return self.description

    def setDescription(self, description):
        self.description = description

class ChainFilter(IFilter):
    def __init__(self):
        self.filters = []

    def addFilter(self, filt):
        self.filters.append(filt)

    def apply(self, srcImage, dstImage):
        for filt in self.filters:
            filt.apply(srcImage, dstImage)
            srcImage = dstImage;

def blackWhite(pixel):
    r, g, b = pixel
    total = (r + g + b)//3
    return (total, total, total)

def onlyRed(pixel):
    r, g, b = pixel
    return (r, 0, 0)

def onlyBlue(pixel):
    r, g, b = pixel
    return (0, 0, b)

def onlyGreen(pixel):
    r, g, b = pixel
    return (0, g, 0)

def removeRed(pixel):
    r, g, b = pixel
    return (0, g, b)

def removeBlue(pixel):
    r, g, b = pixel
    return (r, g, 0)

def removeGreen(pixel):
    r, g, b = pixel
    return (r, 0, b)

blackWhiteFilter = OnePixelFilter(blackWhite, "black and white")
redFilter = OnePixelFilter(onlyRed, "only red")
greenFilter = OnePixelFilter(onlyGreen, "only green")
blueFilter = OnePixelFilter(onlyBlue, "only blue")
remRedFilter = OnePixelFilter(removeRed, "remove red")
remBlueFilter = OnePixelFilter(removeBlue, "remove blue")
remGreenFilter = OnePixelFilter(removeGreen, "remove green")


