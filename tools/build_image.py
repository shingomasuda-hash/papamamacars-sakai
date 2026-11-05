"""design/original-b-v3.jpg（承認済み完成デザイン）から公開用画像を生成する。

1. 最下部の注記「※予約先URLは設定前のデザインです。」(x132-446, y11481-11504) を、
   直下の同じ黄色テクスチャ背景で置き換えて消す（他の部分は一切変更しない）
2. 品質90・4:4:4・プログレッシブJPEGで再圧縮（9.6MB → 約2.7MB）

使い方: python3 tools/build_image.py

LINE予約ボタンのクリック領域（元画像ピクセル座標、index.html に%で設定済み）
  first_view : x36-548  y1188-1338
  middle     : x36-548  y5270-5420
  bottom     : x63-527  y11220-11357
"""
from PIL import Image

SRC = "design/original-b-v3.jpg"
DST = "public/images/lp-sakai.jpg"
X0, X1, Y0, Y1 = 132, 446, 11481, 11504
FEATHER = 8

im = Image.open(SRC).convert("RGB")
h = Y1 - Y0
patch = im.crop((X0, Y1 + 1, X1, Y1 + 1 + h))
mask = Image.new("L", (X1 - X0, h), 255)
for i in range(FEATHER):
    v = int(255 * (i + 1) / (FEATHER + 1))
    for y in range(h):
        mask.putpixel((i, y), v)
        mask.putpixel((X1 - X0 - 1 - i, y), v)
im.paste(patch, (X0, Y0), mask)
im.save(DST, quality=90, subsampling=0, progressive=True, optimize=True)
print("wrote", DST)
