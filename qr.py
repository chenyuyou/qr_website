import qrcode
from MyQR import myqr
from PIL import Image

def QR_With_Central_Img(link="http://192.168.50.126:8000", central_picture="BackgroudIMG.png", output_file="output_code.png"):
	qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=2)
	content = link
	qr.add_data(content)
	qr.make(fit=True)
	img=qr.make_image()
	img=img.convert("RGBA")
	icon = Image.open(central_picture)

	img_w, img_h = img.size
	factor = 4
	size_w = int(img_w / factor)
	size_h = int(img_h / factor)

	icon_w, icon_h = icon.size
	if icon_w > size_w:
		icon_w = size_w
	if icon_h > size_h:
		icon_h = size_h
	icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)

	w = int((img_w - icon_w)/2)
	h = int((img_h - icon_h)/2)
	icon = icon.convert("RGBA")
	img.paste(icon, (w,h), icon)
	img.save(output_file)

def QR_With_FullBackgroud_Img(link="http://192.168.50.126:8000", backgroud_picture="BackgroudIMG.png", output_file="output_code.png"):
	myqr.run(
		words = link,
		version=1,
		level="H",
		picture=backgroud_picture,
		colorized=True,
		contrast=1.0,
		brightness=1.0,
		save_name=output_file
	)	



def QR_Single_Code(link="http://192.168.50.126:8000", output_file="output_code.png"):
	
	qr = qrcode.QRCode(version=1, box_size=10, border=2)
	content = link
	qr.add_data(content)
	qr.make(fit=True)
	img=qr.make_image()
	img.save(output_file)





if __name__ == '__main__':
#	QR_Single_Code(link="http://192.168.50.126:8000",output_file="output_file.png")
#	QR_With_Central_Img(link="http://192.168.50.126:8000", central_picture="1.jpg", output_file="output_file.png")
	QR_With_FullBackgroud_Img(link="http://192.168.50.126:8000", backgroud_picture="1.jpg", output_file="output_file.png")