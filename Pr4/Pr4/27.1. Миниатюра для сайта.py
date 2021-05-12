from PIL import Image

def make_preview(size, n):
    image = Image.open("image27.1.jpg")
    img_color = image.convert("P", palette=Image.ADAPTIVE, colors=n)
    img_resized = img_color.resize(size)

    img_resized.save("done.bmp")
make_preview((400, 200), 64)
