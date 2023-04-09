import pyqrcode
content="this is generated be me"
url = pyqrcode.create(content)
url.png("myqr.png",scale=10)
print("QR code generated successfully")
