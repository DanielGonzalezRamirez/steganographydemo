# Code by Daniel Gonzalez 

def inject(jpeg, message):
    """
        Opens the JPEG file as bits in append mode so the message can be appended.
        Args:
            jpeg (string): Path to the JPEG file
            message (bytes): Message to be injected into the image
    """
    with open(jpeg, 'ab') as f_target:
        f_target.write(message)


def extract(jpeg):
    """
        Opens the JPEG file as bits in read mode so the message can be extracted.
        Args:
            jpeg (string): Path to the JPEG file with the injected message
        Return:
            Returns the message extracted from the JPEG file
    """
    with open(jpeg, 'rb') as f:
        content = f.read()
        offset = content.index(bytes.fromhex('FFD9'))
        # Message was hidden after the closing word 'FFD9' so it is read from there
        f.seek(offset + 2)
        return f.read()

def main():
    # Define the path to the JPEG file where the message will be hidden and the message to hide
    jpeg_file = 'targetjpeg.jpg'
    message = b'Hello world!'
    
    # Injects message into JPEG
    inject(jpeg_file, message)

    input('Press enter to continue')
    
    # Retrieves message from JPEG
    retrieved_message = extract(jpeg_file)
    print(retrieved_message)

if __name__ == "__main__":
    main()
