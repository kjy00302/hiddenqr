import qrcode
from PIL import Image
from PIL import ImageDraw


qr_outer = qrcode.QRCode(
    box_size=1,
    border=0,
)
qr_outer.add_data("https://github.com/kjy00302/hiddenqr")

qr_inner = qrcode.QRCode(
    box_size=1,
    border=0,
)
qr_inner.add_data("https://youtu.be/dQw4w9WgXcQ")

img_a: Image.Image = qr_outer.make_image()
img_b: Image.Image = qr_inner.make_image()

assert img_a.size == img_b.size

MODULE_SIZE = 16
INNER_SIZE = 1
BORDER_SIZE = MODULE_SIZE * 4

OUTER_SIZE = (MODULE_SIZE - INNER_SIZE) // 2
new_size = (
    img_a.width * MODULE_SIZE,
    img_a.height * MODULE_SIZE)

new_img = Image.new('1', new_size)
d: ImageDraw.ImageDraw = ImageDraw.Draw(new_img)

for y in range(img_a.height):
    for x in range(img_a.width):
        point_outer_a = (x * MODULE_SIZE, y * MODULE_SIZE)
        point_outer_b = ((x+1) * MODULE_SIZE - 1, (y+1) * MODULE_SIZE - 1)
        point_inner_a = (x * MODULE_SIZE + OUTER_SIZE, y * MODULE_SIZE + OUTER_SIZE)
        point_inner_b = ((x+1) * MODULE_SIZE - 1 - OUTER_SIZE, (y+1) * MODULE_SIZE - 1 - OUTER_SIZE)
        d.rectangle((point_outer_a, point_outer_b), img_a.getpixel((x, y)))
        d.rectangle((point_inner_a, point_inner_b), img_b.getpixel((x, y)))

new_size = (
    new_img.width + BORDER_SIZE * 2,
    new_img.height + BORDER_SIZE * 2)

new_img_w_border = Image.new('1', new_size, 1)

new_img_w_border.paste(new_img, (BORDER_SIZE, BORDER_SIZE))
new_img_w_border.save('output.png')
