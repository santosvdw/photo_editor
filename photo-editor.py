# -------------------------------------------------------------------------
# Import

import os
from PIL import Image, ImageEnhance, ImageFilter

# -------------------------------------------------------------------------
# App


def check_for_folders(src_path, dest_path):
    if os.path.exists(src_path):
        imgs = (os.listdir(src_path))
    else:
        os.mkdir(src_path)
    if os.path.exists(dest_path):
        os.chdir(dest_path)
        add_filter(imgs, src_path)
    else:
        os.mkdir(dest_path)


def add_filter(imgs, src_path):
    for im in imgs:
        img = Image.open("../"+src_path+"/"+im)

        # Change size
        width = img.size[0]
        height = img.size[1]

        size = (int(width / 2), int(height / 2))

        SzOutput = img.resize(size)

        # Brightness
        BrEnhancer = ImageEnhance.Brightness(SzOutput)
        BrFactor = 1.05
        BrOutput = BrEnhancer.enhance(BrFactor)

        # Sharpness
        ShEnhancer = ImageEnhance.Sharpness(BrOutput)
        ShFactor = 10
        ShOutput = ShEnhancer.enhance(ShFactor)

        # CC
        ClrEnhancer = ImageEnhance.Color(ShOutput)
        ClrFactor = 1.25
        ClrOutput = ClrEnhancer.enhance(ClrFactor)

        # Contrast
        ConEnhancer = ImageEnhance.Color(ClrOutput)
        ConFactor = 1.4
        ConOutput = ConEnhancer.enhance(ConFactor)

        # Blur
        BlOutput = ConOutput.filter(ImageFilter.BLUR)

        # Save endresult
        img_output = BlOutput

        # Save photo
        file_name = os.path.splitext(im)[0]

        img_output.save(file_name+"_edited.png", "png",
                        optimize=True, quality=80)
    print('Done! Check the "output" folder to see your edited photos.')


check_for_folders('.\import', '.\output')
