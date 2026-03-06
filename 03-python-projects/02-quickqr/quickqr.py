import qrcode
import cv2
import os
import webbrowser



# Generate qr code
def generate_qr(data, filename="qr-img.png"):

    """
    Generate a QR Code for the given data
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

        img = qr.make_image(fill_color="black", back_color="white")
        img.save(filename)


        return filename

    except Exception as e:
        print("Error Generating QR code",e)
        return None
    

# show qr code dirrectly on screen
def show_qr(file):

    path = os.path.abspath(file)
    os.startfile(path)            # this shows the file

    

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
    if bbox is not None and data:
        return data

    return  None



def scan_qr_camera():

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    detector = cv2.QRCodeDetector()

    qr_code = None

    print("press 'o' to open link")
    print("press 'q' to quit")

    try:
        while True:

            ret, frame = cap.read()

            if not ret:
                continue

            data, bbox, _ = detector.detectAndDecode(frame)

            qr_data = None

            if bbox is not None:

                for i in range(len(bbox)):
                    pt1 = tuple(bbox[i][0].astype(int))
                    pt2 = tuple(bbox[(i+1) % len(bbox)][0].astype(int))
                    cv2.line(frame, pt1, pt2, (0,255,0), 2)

                if data:
                    qr_data = data

                    # show instructions 
                    cv2.putText(frame,
                        "Press O to open | Q to quit",
                        (20,450),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6,
                        (255,255,255),
                        2)

                    # show decoded QR data
                    if data:
                        cv2.putText(frame,
                            data,
                            (40,50),
                            cv2.FONT_HERSHEY_DUPLEX,
                            0.9,
                            (0,255,0),
                            2)
                    
            cv2.imshow("QR Scanner", frame)

            key = cv2.waitKey(1)

            if key==ord("q"):
                break
            
            if key==ord("o") and qr_data:
                try:
                    print("opening: ", qr_data)
                    webbrowser.open(qr_data)
                except:
                    print("No Link present")

    finally:
        cap.release()
        cv2.destroyAllWindows()



def main():


    while True:

        os.system("cls")
        
        print("\n=== QR Code Tools ===")
        print("1. Generate QR code")
        print("2. Decode QR Code")
        print("3. Scan QR Code")
        print("4. Exit")

        choice = input("Ente your choice: ")

        if choice=='1':

            data = input("Enter the data or URL to generate QR Code:")
            filename = input("Enter the file name of QR code you want: ").lower().strip()
            if not filename.endswith(".png"):
                filename+=".png"


            file = generate_qr(data , filename)
            if file:
                print("QR Code generated successfully")
                print("Saved as:", file)
                print("Saved at:", os.path.abspath(file))
                show_qr(file)

            else:
                print("QR generation failed")

            input("\nPress Enter to continue...")

        elif choice=='2':

            file_path = input("Enter Qr File path: ")

            result = decode_qr(file_path)
            if result:
                print("Decode Data:",result)
            else:
                print("No QR code Found!!!")

            input("\nPress Enter to continue...")
        
        elif choice=='3':

            scan_qr_camera()

            input("\nPress Enter to continue...")
        
        elif choice=='4':

            print("Thanks for using the service")
            print("Exiting the program...")
            break

        else:
            print("Invalid Choice")
            print("Try Again...")
            input("\nPress Enter to continue...")



if __name__ == "__main__":
    main()