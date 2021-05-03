import os
import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

current_path = os.path.abspath(os.getcwd())


def create_qrcode():
    while True:
        try:
            qrcode_data = input("Enter data to encode in the qrcode:\n>>")
            img = qrcode.make(qrcode_data)
            img.save(f"{current_path}\myqrcode.png")
            break
        except FileNotFoundError:
            print("Please enter a valid data")


def decode_qrcode():
    while True:
        try:
            image_name = input("What qrcode you wish to decode?\n>>")
            img = Image.open(f"{current_path}\{image_name}")
            result = decode(img)
            print(result)
            break
        except FileNotFoundError:
            print("Please enter a valid name")
            decode_qrcode()


def main():
    while True:
        try:
            option = input("Please choose an option:\n"
                           "[1] Encode data to a QR code \n"
                           "[2] Decode data from a QR code \n"
                           "[Q] Quit \n"
                           ">>")
            print(" ")
            if option.lower() == "q" or option.lower() == "quit":
                break
            elif int(option) < 1 or int(option) > 2:
                raise ValueError
            elif int(option) == 1:
                create_qrcode()
            elif int(option) == 2:
                decode_qrcode()
        except ValueError:
            print("Please choose a valid option")


if __name__ == '__main__':
    main()
