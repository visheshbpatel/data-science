import qrcode
import cv2
import os


# Generate qr code
def generate_qr(data, filename="qr-img.png"):

    """
    Generate a QR Code for the give data
    """

    try:

        if not data:
            raise ValueError("Data Cannot be Empty")
        qr = qrcode.QRCode(
            version=2,
            box_size=10,
            border=5
        )
        
        qr.add_data(data)           
        qr.make(fit=True)           # if box size small for the give output automatically increase it

        img = qr.make_image(fill_color="Black", back_color="white")
        img.save(filename)


        return filename

    except Exception as e:
        print("Error Generating QR code",e)
        return None
    

# show qr code dirrectly on screen
def show_qr(file):

    path = os.path.abspath(file)
    os.startfile(path)

    

# Decode the qr code
def decode_qr(filename):

    """"
    Decode Qr code using OpenCV
    """

    img = cv2.imread(filename)
    
    if img is None:
        print("Image Not Found")
        return None
    
    decoder = cv2.QRCodeDetector()

    data, bbox, _ = decoder.detectAndDecode(img)


    # returning the generated image
    if bbox is not None:
        return data

    return  None



def main():

    data = input("Enter the data or URL to generate QR Code:")
    filename = input("Enter the file name of QR code you want: ").lower().strip()
    if not filename.endswith(".png"):
        filename+=".png"

    file = generate_qr(data , filename)
    print("QR Code generated successfully")
    print("Saved as:", file)
    print("Saved at:", os.path.abspath(file))
    if file:
        show_qr(file)


    result = decode_qr(file)
    if result:
        print("Decode Data:",result)
    else:
        print("No QR code Found!!!")



if __name__ == "__main__":
    main()