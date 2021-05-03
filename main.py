import qrcode
import os


def create_qrcode(data):
    img = qrcode.make(data)
    current_path = os.path.abspath(os.getcwd())
    img.save(f"{current_path}\myqrcode.png")


if __name__ == '__main__':
    qrcode_data = input("Enter data to encode in the qrcode:\n>>")
    create_qrcode(qrcode_data)
