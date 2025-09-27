import qrcode

# Data to encode
data = "https://samiksha-627.github.io/product-information/"   # You can replace this with any text or link

# Generate QR code
qr = qrcode.QRCode(
    version=1,  # controls the size of the QR Code (1 = 21x21)
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,  # size of each box in pixels
    border=4,     # thickness of the border (minimum is 4)
)

qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code as an image
img.save("qrcode.png")

print("QR code generated and saved as 'qrcode.png'")
