import qrcode
serverno=0
for line in open("iLo.txt"): 
  serverno+=1
  qr = qrcode.QRCode(
    version=7,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
  )
  qr.add_data(line)
  qr.make(fit=True)
  img = qr.make_image()
  img.save(str(serverno)+".png")

