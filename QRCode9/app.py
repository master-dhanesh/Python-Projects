import qrcode
# pip install pillow
data = "Surprise Motherfucker 😊"

img = qrcode.make(data)

# img.save(f"E:\Working_Material\python_dev\DoingPython\QRCode9\{data.split()[0]}.png")
img.save(f"./{data.split()[0]}.png")
# E:\Working_Material\python_dev\DoingPython\QRCode9

print("Done!")
