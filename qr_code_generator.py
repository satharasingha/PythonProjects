import qrcode

data = input("Enter your URL: ").strip()
filename = input("Enter your filename (with .png): ").strip()

# Create a QRCode object
qr = qrcode.QRCode(box_size=10, border=1)
qr.add_data(data)
qr.make(fit=True)

# Generate and save the QR code image
image = qr.make_image(fill_color="black", back_color="white")
image.save(filename)

print(f"QR Code saved as: {filename}")
