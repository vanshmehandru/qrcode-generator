import qrcode

user_content = input("Enter the text or URL for the QR code: ")

qr = qrcode.QRCode(version = 1, box_size = 5, border = 5)
qr.add_data(user_content)
qr.make()

img = qr.make_image(fill_color = 'black', back_color = 'white')
img.save('web_qr.png')