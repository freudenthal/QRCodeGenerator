import qrcode
import qrcode.image.svg
import sys
import argparse

# define a method to choose which factory metho to use
# possible values 'basic' 'fragment' 'path'

method = "png"

data = "https://actionnetwork.org/events/portland-dsa-ecosocialist-working-group-monthly-meeting/"
outputfilename = "EcoSocialistWG_qrcode"


def GenerateQRCodeFile(method, outputfilename, data):
    if method == "png":
        factory = qrcode.image.pure.PyPNGImage
        extension = ".png"
    elif method == 'basic':
        # Simple factory, just a set of rects.
        factory = qrcode.image.svg.SvgImage
        extension = ".svg"
    elif method == 'fragment':
        # Fragment factory (also just a set of rects)
        factory = qrcode.image.svg.SvgFragmentImage
        extension = ".svg"
    elif method == 'path':
        # Combined path factory, fixes white space that may occur when zooming
        factory = qrcode.image.svg.SvgPathImage
        extension = ".svg"

    # Set data to qrcode
    img = qrcode.make(data, image_factory = factory)

    # Save svg file somewhere
    fullfilname = outputfilename + extension
    img.save(fullfilname)

parser = argparse.ArgumentParser()
parser.add_argument("file", type=str, help="Output file name without extension.")
parser.add_argument("text", type=str, help="The text to encode in the QR code.")
parser.add_argument("-m", "--method", type=str, choices=["png", "basic", "fragment", "path"], help="Method of png, basic, fragment or path.", default="png")

if __name__ == '__main__':
    parsedarguments = parser.parse_args()
    GenerateQRCodeFile(parsedarguments.method,parsedarguments.file,parsedarguments.text)