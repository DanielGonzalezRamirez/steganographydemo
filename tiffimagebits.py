# Code by Daniel Gonzalez 

from PIL import Image
import numpy as np

def main():
    # Opens TIFF image as an Image object and displays it
    im = Image.open('targettiff.tif')
    im.show()
    
    input('Press enter to continue')

    # Image is stored as a NumPy array
    array = np.array(im)
    print(array)

    input('Press enter to continue')

    # Message to hide is defined
    message = 'Hello world!'

    # The integer of the ASCII representation of each letter of the message replaces a position on the image array
    i = 0
    for letter in bytearray(message,'ascii'):
        array[i][0][0] = letter
        i += 1

    # The image with the hidden message is built and displayed
    im_and_message = Image.fromarray(array)
    im_and_message.show()

    input('Press enter to continue')
    
    # The hidden message is recovered from the image
    recovered = np.array(im_and_message)

    for i in range(0,len(recovered)):
        print(chr(recovered[i][0][0]))


if __name__ == "__main__":
    main()
