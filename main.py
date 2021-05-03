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


if __name__ == '__main__':
    create_qrcode()
    decode_qrcode()
