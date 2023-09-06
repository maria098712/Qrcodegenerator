import qrcode
from PIL import Image
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=5,
    border=3,
)
data = "https://www.youtube.com/"

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color="red", back_color="blue")
img.save("youtube_qr.png")
img.show()
