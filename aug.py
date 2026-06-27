import os
import cv2
import albumentations as A
import random
import numpy as np

transforms = [
    A.VerticalFlip(p=1),  
    A.HorizontalFlip(p=1),  
    A.Rotate(limit=45, p=1),  
    A.Blur(blur_limit=(3, 7), p=1),  
    A.PadIfNeeded(min_height=512, min_width=512, border_mode=cv2.BORDER_CONSTANT, value=[255, 255, 255], p=1),
    A.HueSaturationValue(hue_shift_limit=5, sat_shift_limit=50, val_shift_limit=1, p=1),  
    A.ToGray(p=1)
]

input_dir = "input_path"
output_dir = "output_path"

os.makedirs(output_dir, exist_ok=True)

image_files = [f for f in os.listdir(input_dir) if f.endswith('.jpg') or f.endswith('.png')]

num_augmentations = 6   # --> chenge as necessery

for filename in image_files:
    image = cv2.imread(os.path.join(input_dir, filename))
    applied_transforms = random.sample(transforms, num_augmentations)  # Randomly select 6 transformations
    
    for i, transform in enumerate(applied_transforms):
        augmented = transform(image=image)
        augmented_image = augmented['image']
        output_path = os.path.join(output_dir, f"augmented_{filename[:-4]}_{i}.jpg")  
        cv2.imwrite(output_path, augmented_image)
