import qrcode as qr
from pyzbar.pyzbar import decode
from PIL import Image


def generate_qr(data, filename="qr-img.png"):
    qr_code = qr.make(data)
    qr_code.save(filename)
    return filename


def decode_qr(filename):
    
    img = Image.open(filename)
    decoded_data = decode(img)

    if not decoded_data:
        return None
    
    return decoded_data[0].data.decode("ascii")


def main():
    url = "https://github.com/visheshbpatel"

    file = generate_qr(url)
    print("QR Code generated successfully")
    print("Saved as:", file)

    decode_result = decode_qr(file)

    if decode_result:
        print("Decode Data:",decode_result)
    else:
        print("No QR code Found!!!")



if __name__ == "__main__":
    main()