from PIL import Image

def openImage(img):
    image = Image.open(img)
    return image

def getSize(image):
    size = image.size
    width = size[0]
    height = size[1]
    return width, height

def calculateBrightness(r,g,b):
    return (r+g+b)//3

def getBrightness(image, width, height):
    imageArray = []
    for i in range(height):
        rowPixels = []
        for j in range(width):
            colors = image.getpixel((j,i))
            average = calculateBrightness(colors[0], colors[1], colors[2])
            rowPixels.append(average)
        imageArray.append(rowPixels)
    return imageArray

def binSearch(val):
    lo = 0
    hi = len(values)
    while (lo != hi):
        mid = (lo + hi)//2
        if (values[mid] >= val):
            hi = mid
        else:
            lo = mid + 1
    if mid == 0:
        return characters[0]
    else:
        return characters[mid - 1]

def getAscii(pixels):
    symbolArray = []
    for i in range(len(pixels)):
        rowSymbols = []
        for j in range(len(pixels[0])):
            value = binSearch(pixels[i][j])
            rowSymbols.append(value)
        symbolArray.append(rowSymbols)
    return symbolArray

def main():
    s = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
    global characters
    characters = [char for char in s]
    increment = 255/len(s)
    global values
    values = []
    valToAdd = 0
    for i in range(len(s)):
        values.append(valToAdd)
        valToAdd += increment
    image = openImage("./Chick-fil-A.jpg")
    width, height = getSize(image)
    pixels = getBrightness(image, width, height)
    brightness = getAscii(pixels)
    print(width,height)
    for i in range(height):
        for j in range(width):
            print(brightness[i][j], end = " ")
        print('-----------')

if __name__ == '__main__':
    main()
