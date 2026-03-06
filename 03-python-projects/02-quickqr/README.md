# QuickQR - QR Code CLI Tool

A simple Python command line tool to generate, decode, and scan QR codes
using OpenCV.

---

## Features

1.  Generate QR codes from text or URLs
2.  Decode QR codes from image files
3.  Scan QR codes using your webcam
4.  Open detected links directly in your browser

---

## Technologies Used

-   Python
-   OpenCV (opencv-python)
-   qrcode
-   Pillow

---

## Installation

### 1. Clone the repository

``` bash
git clone https://github.com/visheshbpatel/data-science.git
```

### 2. Move into the project folder

``` bash
cd data-science/03-python-projects/02-quickqr
```

### 3. Install required dependencies

``` bash
pip install -r requirements.txt
```

---

## How to Run

Run the program using:

``` bash
python quickqr.py
```

You will see the following menu:

    === QR Code Tools ===
    1. Generate QR code
    2. Decode QR Code
    3. Scan QR Code
    4. Exit

---

## Usage

### Generate QR Code

Enter the data or URL when prompted.

Example:

    Enter the data or URL to generate QR Code: https://google.com
    Enter the file name of QR code you want: google

The QR image will be saved and opened automatically.

---

### Decode QR Code

Provide the path of the QR image.

Example:

    Enter Qr File path: qr-img.png

The decoded data will be printed in the terminal.

---

### Scan QR Code with Webcam

The webcam window will open.

Controls:

-   Press **O** to open detected link in browser
-   Press **Q** to quit scanner

---

## Project Structure

    data-science/
    │
    └── 03-python-projects/
        │
        └── 02-quickqr/
            ├── quickqr.py
            ├── requirements.txt
            ├── README.md
            ├── vbp-github-qr.png
            └── zplz-don't-open-it.png

---

## Requirements

`requirements.txt`

    qrcode
    opencv-python
    Pillow

---

## Demo

![QuickQR Demo](zplz-don't-open-it.png)

---

## Author

Vishesh Patel
