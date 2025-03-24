import qrcode
from PIL import Image

# URL to encode
url = "https://chic-chebakia-ddd1e3.netlify.app/"

# Generate QR code
qr = qrcode.QRCode(
    version=5,  
    error_correction=qrcode.constants.ERROR_CORRECT_H,  
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Create an image of the QR code
qr_img = qr.make_image(fill="black", back_color="white").convert("RGBA")

# Load logo
logo = Image.open("pharmacy/icon.jpeg").convert("RGBA")  # Ensure conversion to RGBA

# Resize logo
logo_size = int(qr_img.size[0] * 0.2)  # Logo should be 20% of QR code size
logo = logo.resize((logo_size, logo_size), Image.LANCZOS)

# Create a new image with transparent background
logo_with_transparency = Image.new("RGBA", logo.size, (0, 0, 0, 0))
logo_with_transparency.paste(logo, (0, 0), mask=logo)

# Calculate positioning
pos = ((qr_img.size[0] - logo_size) // 2, (qr_img.size[1] - logo_size) // 2)

# Paste logo in center
qr_img.paste(logo_with_transparency, pos, mask=logo_with_transparency)

# Save and show the QR code
qr_img.save("qr_with_logo.png")
qr_img.show()
