from BasicFilters import *

img = Image.open("img.jpg")
mix = Image.open("mix.jpg")

properties = (img.size[0], img.size[1])
result = Image.new('RGB', properties)

level = float(input("Enter level: "))
combineFilter = CombineFilter(mix, level)
secondFilter = blackWhiteFilter

combineFilter.apply(img, result)
secondFilter.apply(result, result)
result.save("result.jpg")