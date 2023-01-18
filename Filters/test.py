from BasicFilters import *

img = Image.open("img.jpg")

properties = (img.size[0], img.size[1])
result = Image.new('RGB', properties)

firstFilter = blueFilter
secondFilter = redFilter

chain = ChainFilter();
chain.addFilter(firstFilter)
chain.addFilter(secondFilter)

chain.apply(img, result)

result.save("result.jpg")