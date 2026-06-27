import os
from PIL import Image
from IPython.display import Image


def rename_images(directory):
    image_files = [f for f in os.listdir(directory) if f.endswith(('.jpg', '.jpeg', '.png', '.gif'))]

    image_files.sort()

    for i, filename in enumerate(image_files, start=1):
        _, ext = os.path.splitext(filename)

        # -> replace as desired name like "mango"
        # ->output will be like mango1,mango2,....
        new_filename =  "image_name"+ str(i) + ext  

        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))

directory_path = "input_path"

rename_images(directory_path)


