def generate_qrcode():
    import qrcode
    from PIL import Image  # Import to enable displaying the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data('number:  693201084\n email:   jordannguepi@gmail.com')
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")  # Generate QR code image
    img.show()  # Display the generated QR code

generate_qrcode()

