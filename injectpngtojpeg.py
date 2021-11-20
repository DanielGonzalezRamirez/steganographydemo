# Code by Daniel Gonzalez 

def inject(jpeg, png):
    """
        Opens the JPEG file as bits in append mode and PNG file as bits in read mode, so the PNG can be appended to the JPEG.
        Args:
            jpeg (string): Path to the JPEG file
            png (string): Path to the PNG file
    """
    with open(jpeg, 'ab') as f_target, open(png, 'rb') as f_injection:
        f_target.write(f_injection.read())

def extract(jpeg):
    """
        Opens the JPEG file as bits in read mode so the PNG image can be extracted.
        PNG image is saved as a new file.
        Args:
            jpeg (string): Path to the JPEG file with the injected image
    """
    with open(jpeg, 'rb') as f:
        content = f.read()
        offset = content.index(bytes.fromhex('FFD9'))

        f.seek(offset + 2)
        
        with open('newpng.png', 'wb') as f_retrieved:
            f_retrieved.write(f.read())

def main():
    # Define the path to the JPEG file where the PNG will be hidden and the path to the PNG file to hide
    jpeg_file = 'targetjpeg.jpg'
    png_file = 'hiddenpng.png'
    
    # Injects PNG into JPEG
    inject(jpeg_file, png_file)

    input('Press enter to continue')

    # Retrieves PNG from JPEG
    extract(jpeg_file)

if __name__ == "__main__":
    main()
