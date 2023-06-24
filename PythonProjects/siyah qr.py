import qrcode

url= 'https://www.instagram.com/halprn.kurt/'

image = qrcode.make(url)
image.save("QRcode.png")
