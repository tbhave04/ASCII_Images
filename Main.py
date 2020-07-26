from PIL import Image, ImageDraw, ImageFont
from PIL import ImageOps

# returns given image converted to grayscale
def openImage(img):
    image = Image.open(img).convert(grayscale)
    return image

# returns width and height of the image
def getSize(image):
    size = image.size
    width = size[0]
    height = size[1]
    return width, height

# returns the brightness of the pixel
def calculateBrightness(r,g):
    return (r+g)//2

# returns an array of the brightness of each pixel
def getBrightness(image, width, height):
    imageArray = []
    for i in range(height):
        rowPixels = []
        for j in range(width):
            colors = image.getpixel((j,i))
            average = calculateBrightness(colors[0], colors[1])
            rowPixels.append(average)
        imageArray.append(rowPixels)
    return imageArray

# returns a symbol given a brightness value
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

# returns the corresponding ASCII value from the brightness level of the pixel
def getAscii(pixels):
    symbolArray = []
    for i in range(len(pixels)):
        rowSymbols = []
        for j in range(len(pixels[0])):
            value = binSearch(pixels[i][j])
            rowSymbols.append(value)
        symbolArray.append(rowSymbols)
    return symbolArray

# creates the ASCII image given the ASCII symbol array
def createImage(width, height, symbols):
    line = ''.join(symbols[0])
    font = ImageFont.load_default()
    maxHeight = font.getsize(line)[0]
    maxWidth = font.getsize(line)[1]
    img = Image.new('L', (maxWidth*len(line), maxHeight), color = 255)
    d = ImageDraw.Draw(img)
    vertical = 5
    horizontal = 5
    spacing = 5
    for line in symbols:
        line = ''.join(line)
        d.text((horizontal, vertical), line, fill = 0)
        vertical = vertical + spacing
    image = ImageOps.invert(img)
    coordinates = image.getbbox()
    img = img.crop(coordinates)
    img.save(outputImage)

# converts image to ascii image
def main():
    global grayscale
    grayscale = "LA"
    s = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
    global characters
    characters = [char for char in s]
    increment = 255/len(s)
    # creates the ASCII to brightness map
    global values
    values = []
    valToAdd = 0
    for i in range(len(s)):
        values.append(valToAdd)
        valToAdd += increment
    # creates output image name
    userinput = input("Enter an image: ")
    index = userinput.find(".")
    global outputImage
    outputImage = userinput[:index] + "Output.png"
    # converts given image to ascii image
    image = openImage(userinput)
    width, height = getSize(image)
    brightness = getBrightness(image, width, height)
    symbols = getAscii(brightness)
    createImage(width,height,symbols)

if __name__ == '__main__':
    main()
