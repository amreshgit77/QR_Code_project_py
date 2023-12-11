# darkblue_qrcode.py
#import segno
import segno

qrcode = segno.make_qr("Hello, World")
qrcode.save(
    "darkblue_qrcode.png",
    scale=5,
    dark="darkblue",
)
