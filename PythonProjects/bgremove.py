from rembg import remove
from PIL import Image
import easygui as eg
inputPath= eg.fileopenbox(title="Select image file")
outputPath= eg.filesavebox(title="Save file to..")
input = Image.open(inputPath)
output =remove(input)
output.save(outputPath)

