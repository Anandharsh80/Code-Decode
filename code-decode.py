# Beginning of the code



#CODE-DECODE
#code by - HARSH ANAND



#import Image module from Pillow(PIL)
from PIL import Image
from termcolor import colored



# Function to convert message into list of binary representation of their ASCII values
def convertBinary(data):
    
    message_chars = []

    for i in data:
        message_chars.append(format(ord(i), '08b'))

    return message_chars



# Function to obtain pixels from an Image
def getPixels(fileName):

    img = Image.open(fileName)
    pixel_list = list(img.getdata())

    return pixel_list



# Function to Encode message into pixels 
def encode(pixel_list, message_chars):

    # Length of string
    length = len(message_chars)  

    # Iterator to traverse through pixels
    pix_iter = 0

    # Iterating through the letter list
    for index in range(0,length):

        # List to obtain the required pixel values according to letter
        req_val = []

        # Adding original pixel values to the list
        for i in range(0,3):
            for j in range(0,3):
                req_val.append(pixel_list[pix_iter+i][j])
        
        # Modifying pixel values inside the list
        for i in range(0,8):
            if (message_chars[index][i] == '0' and req_val[i]%2 != 0):
                req_val[i] = req_val[i] - 1
            elif (message_chars[index][i] == '1' and req_val[i]%2 == 0):
                if (req_val[i] == 0):
                    req_val[i] = req_val[i] + 1
                else:                        
                    req_val[i] = req_val[i] - 1

        # Modification for checking of message end
        if (index == length-1 and req_val[-1]%2 == 0):
            if (req_val[-1] == 0):
                req_val[-1] = req_val[-1] + 1
            else:                        
                req_val[-1] = req_val[-1] - 1
        elif (index != length-1 and req_val[-1]%2 != 0):
            req_val[-1] = req_val[-1] - 1

        # Creating tuples of pixels out of modified list and overwriting them over original pixels
        req_val_iter = 0
        for i in range(0,3):
            var =[]
            for j in range(0,3):
                var.append(req_val[req_val_iter])
                req_val_iter += 1
            pixel_list[pix_iter + i] = tuple(var)

        pix_iter = pix_iter + 3
    
    return pixel_list



# Function to create copy of an image with predetermined value of pixels 
def createImage(pixel_list, fileName, fileName2):

    img = Image.open(fileName)
    encoded_image = Image.new(img.mode, img.size)
    encoded_image.putdata(pixel_list)
    encoded_image.save(fileName2)



# Function to Encode message into pixels 
def decode(pixel_list):

    # Iterator for Pixels
    pix_iter = 0

    # String that will hold Decoded message
    decoded_message = ''
    
    # Iterating through the image's pixels
    while(True):

        # Taking 3 tuples at a time
        req_val = []
        for i in range(0,3):
            for j in range(0,3):
                req_val.append(pixel_list[pix_iter+i][j])

        pix_iter = pix_iter + 3

        # Generating Letter from Pixels
        letter = ''
        for i in range(0,8):
            if (req_val[i]%2 == 0):
                letter = letter + '0'
            else:
                letter = letter + '1'
        
        # Adding letter to the string
        decoded_message += chr(int(letter, base = 2))

        # Checking for end of message 
        if (req_val[-1]%2 != 0):
            return decoded_message


# Function to run driver code
def driverFunc():

    print(colored("Welcome to CODE-DECODE","magenta"))
    print(colored("Enter 1 to Encode message\nEnter 2 to Decode message","green"))

    while(True):

        var = int(input())
        if (var == 1 or var == 2):
            break
        print(colored("Invalid Choice","red"))

    if (var == 1):

        print(colored("ENCODING","magenta"))

        print(colored("Enter the Message:","green"))
        data = input()

        print(colored("Enter the Image name (with extension):","green"))
        fileName = input()

        message_chars = convertBinary(data)
        pixel_list = getPixels(fileName)
        pixel_list = encode(pixel_list,message_chars)
        
        print(colored("Enter the Encoded Image name (with extension):","green"))
        fileName2 = input()

        createImage(pixel_list, fileName, fileName2)
        
        print(colored("Encoded image saved","yellow"))

    else :

        print(colored("DECODING","magenta"))

        print(colored("Enter the Encoded Image name (with extension):","green"))
        fileName = input()

        pixel_list = getPixels(fileName)
        decoded_message = decode(pixel_list)

        print(colored("The Encoded message is:","yellow"))
        print(decoded_message)




# Driver code
if __name__ == "__main__":

    driverFunc()



# End of the code