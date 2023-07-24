import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import qrcode
import io

def create_qr_code(url, scale=6):
    # Generate QR code
    qr = qrcode.QRCode(
        version=3,
        error_correction=qrcode.constants.ERROR_CORRECT_L, 
        box_size=10, # Increase box_size instead of scaling later
        border=0,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white').get_image().convert("RGB")

    byte_arr = io.BytesIO()
    img.save(byte_arr, format='PNG')
    byte_arr.seek(0)  # Seek back to the beginning of the BytesIO object
    return byte_arr


def add_qr_code(fig, ax, url):
    qr_code = create_qr_code(url)
    imagebox = OffsetImage(plt.imread(qr_code), zoom=0.2)
    ab = AnnotationBbox(imagebox, (0.84, 0.12))
    ax.add_artist(ab)
