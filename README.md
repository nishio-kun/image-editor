# image-editor

"image-editor" changes color of images.

# How to use

To check a color code of a pixel: `python src/main.py show [path]`.

To change color: `python src/main.py change [path] -f [color_code] -t [color_code]`.
You can save changed image by adding `-s [path]`

To mask an image: `python src/main.py mask [path] -m [path]`.
You can save changed image by adding `-s [path]`
