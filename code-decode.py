# Beginning of the code



#CODE-DECODE
#code by - HARSH ANAND



#import Image module from Pillow(PIL)
from tkinter import *
from PIL import Image



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






# Driver code
if __name__ == "__main__":



    # Starting Page of Console
    def StartPage():

        frame = Frame(console)
        frame.config(background='#000000', padx=100, pady=100)

        welcome_label_text = StringVar()
        button_enc_text = StringVar()
        button_dec_text = StringVar()
        welcome_label_text.set("Welcome to CODE-DECODE !!")
        button_enc_text.set("Encode")
        button_dec_text.set("Decode")



        random_label = Label(frame, text='', bg = '#000000')
        random_label.grid(row=0,column=0)
        welcome_label = Label(frame, textvariable = welcome_label_text, bg = '#000000', fg = '#FFFFFF', padx='10px', pady='10px', font=('', 30))
        welcome_label.grid(row=1,column=0)
        random_label = Label(frame, text='', bg = '#000000')
        random_label.grid(row=2,column=0)

        button_enc = Button(frame, textvariable=button_enc_text, command= lambda: EncodePage(), padx='10px', pady='10px', font=('', 20))
        button_enc.grid(row=3,column=0)

        random_label = Label(frame, text='', bg = '#000000')
        random_label.grid(row=4,column=0)

        button_dec = Button(frame, textvariable=button_dec_text, command= lambda: DecodePage(), padx='10px', pady='10px', font=('', 20))
        button_dec.grid(row=5,column=0)

        random_label = Label(frame, text='', bg = '#000000')
        random_label.grid(row=6,column=0)

        random_label = Label(frame, text='', bg = '#000000')
        random_label.grid(row=7,column=0)

        frame.grid(row=0, column=0)


    # Encode Page of Console
    def EncodePage():

        frame = Frame(console)
        frame.config(background='#000000', padx= 80)

        welcome_label_text = StringVar()
        message_label_text = StringVar()
        image_file_label_text = StringVar()
        image_save_label_text = StringVar()
        message = StringVar()
        og_image = StringVar()
        encoded_image = StringVar()
        button_enc_text = StringVar()
        button_home_text = StringVar()
        welcome_label_text.set("ENCODE")
        message_label_text.set("Enter the Message to encrypt")
        image_file_label_text.set("Enter the Image File path (with extension)")
        image_save_label_text.set("Enter the Encoded Image File path (with extension)")
        button_enc_text.set("Encode")
        button_home_text.set("Back to Home")


        welcome_label = Label(frame, textvariable = welcome_label_text, bg = '#000000', fg = '#FFFFFF', padx='10px', pady='10px', font=('', 25))
        welcome_label.grid(row=0,column=0)

        random_label = Label(frame,text='', bg = '#000000')
        random_label.grid(row=1,column=0)

        message_label = Label(frame, textvariable = message_label_text, bg = '#000000', fg = '#FFFFFF', padx='10px', pady='10px', font=('', 15))
        message_label.grid(row=2,column=0)
        message_entry = Entry(frame, textvariable = message, width=60)
        message_entry.grid(row=3,column=0)

        image_file_label = Label(frame, textvariable = image_file_label_text, bg = '#000000', fg = '#FFFFFF', padx='10px', pady='10px', font=('', 15))
        image_file_label.grid(row=4,column=0)
        image_file_entry = Entry(frame, textvariable = og_image, width=60)
        image_file_entry.grid(row=5,column=0)

        image_save_label = Label(frame, textvariable = image_save_label_text, bg = '#000000', fg = '#FFFFFF', padx='10px', pady='10px', font=('', 15))
        image_save_label.grid(row=6,column=0)
        image_save_entry = Entry(frame, textvariable = encoded_image, width=60)
        image_save_entry.grid(row=7,column=0)

        random_label = Label(frame,text='', bg = '#000000')
        random_label.grid(row=8,column=0)

        button_enc = Button(frame, textvariable=button_enc_text, command = lambda: Encode(message.get(), og_image.get(), encoded_image.get()), padx='10px', pady='5px', font=('', 20))
        button_enc.grid(row=9,column=0)

        random_label = Label(frame, text='', bg = '#000000')
        random_label.grid(row=10,column=0)

        button_home = Button(frame, textvariable=button_home_text, command = lambda: StartPage(), padx='10px', pady='5px', font=('', 20))
        button_home.grid(row=11,column=0)

        random_label = Label(frame, text='', bg = '#000000')
        random_label.grid(row=12,column=0)

        frame.grid(row=0, column=0)


    # Decode Page of Console
    def DecodePage():

        frame = Frame(console)
        frame.config(background='#000000', padx= 80, pady=100)

        welcome_label_text = StringVar()
        image_decode_label_text = StringVar()
        encoded_image = StringVar()
        button_dec_text = StringVar()
        button_home_text = StringVar()
        welcome_label_text.set("DECODE")
        image_decode_label_text.set("Enter the Encoded Image File path (with extension)")
        button_dec_text.set("Decode")
        button_home_text.set("Back to Home")

        welcome_label = Label(frame, textvariable = welcome_label_text, bg = '#000000', fg = '#FFFFFF', padx='10px', pady='10px', font=('', 25))
        welcome_label.grid(row=0,column=0)

        random_label = Label(frame, text='', bg = '#000000')
        random_label.grid(row=1,column=0)

        image_decode_label = Label(frame, textvariable = image_decode_label_text, bg = '#000000', fg = '#FFFFFF', padx='10px', pady='10px', font=('', 15))
        image_decode_label.grid(row=2,column=0)
        image_decode_input = Entry(frame, textvariable = encoded_image, width=60)
        image_decode_input.grid(row=3,column=0)

        random_label = Label(frame, text='', bg = '#000000')
        random_label.grid(row=4,column=0)

        button_dec = Button(frame, textvariable=button_dec_text, command = lambda: Decode(encoded_image.get()), padx='10px', pady='5px', font=('', 20))
        button_dec.grid(row=5,column=0)

        random_label = Label(frame, text='', bg = '#000000')
        random_label.grid(row=6,column=0)

        button_home = Button(frame, textvariable=button_home_text, command = lambda: StartPage(), padx='10px', pady='5px', font=('', 20))
        button_home.grid(row=7,column=0)

        random_label = Label(frame, text='', bg = '#000000')
        random_label.grid(row=8,column=0)

        frame.grid(row=0, column=0)


    # Function to run the encode function from user input 
    def Encode(message, og_image, encoded_image):

        root = Tk()
        root.config(background="#000000")
        try:
            root.title("Success")
            root.iconbitmap(r"D:\Python Projects\Steganography\Images\app_icon.ico")
            message_chars = convertBinary(message)
            pixel_list = getPixels(og_image)
            pixel_list = encode(pixel_list,message_chars)
            createImage(pixel_list, og_image, encoded_image)
            Label(root, text="Encoded image saved successfully", bg="#000000", fg="#00FF00", pady=30, padx=20).pack()
        except:
            root.title("Error")
            root.iconbitmap(r"D:\Python Projects\Steganography\Images\error_icon.ico")
            Label(root, text="Invalid Image path or Encoded image path", bg="#000000", fg="#FF0000", pady=30, padx=20).pack()
        root.mainloop()

    
    # Function to run the encode function from user input 
    def Decode(encoded_image):

        root = Tk()
        root.config(background="#000000", width=300)
        try:
            root.title("Encoded Message")
            root.iconbitmap(r"D:\Python Projects\Steganography\Images\app_icon.ico")
            pixel_list = getPixels(encoded_image)
            decoded_message = decode(pixel_list)
            Label(root, text=decoded_message, bg="#000000", fg="#0000FF", pady=30, padx=20).pack()
        except:
            root.title("Error")
            root.iconbitmap(r"D:\Python Projects\Steganography\Images\error_icon.ico")
            Label(root, text="Invalid Encoded image path", bg="#000000", fg="#FF0000", pady=30, padx=20).pack()
        root.mainloop()



    # running our Console
    console = Tk()
    console.title("CODE-DECODE")
    console.iconbitmap(r"D:\Python Projects\Steganography\Images\app_icon.ico")
    console.configure(background='#000000')
    
    StartPage()
    
    console.mainloop()




# End of the code