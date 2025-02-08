import qrcode

# Input data for QR Code
data = input("Enter the text or URL to generate a QR Code: ")

# Create QR Code
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)

# Generate the QR Code Image
img = qr.make_image(fill="black", back_color="white")

# Save the image
img.save("qrcode.png")

print("QR Code generated and saved as 'qrcode.png'")
