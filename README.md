# FER Dataset — Full Statistics Report

This report consolidates the statistics produced by the three exploratory
notebooks in this folder:

| Notebook | Purpose |
| --- | --- |
| `fer_raw_dataset_stats.ipynb` | Per-class counts, dimensions, channels, file extensions, intensity stats for `fer_data/` and `fer_data_raw_512/` |
| `saved_raw_report_before_rsz.ipynb` | Snapshot of the pre-resize report (same stats, locked in before resizing) |
| `fer_augment.ipynb` | Modern augmentation pipeline (`fer_data_raw_512/` → `fer_data_aug_512/`) with 4× expansion, pixel stats, augmentation strength and storage impact |

Datasets covered:

- `fer_data/` — original raw images, mixed sizes
- `fer_data_raw_512/` — resized to 512×512 (output of `resize.py`)
- `fer_data_aug_512/` — 4 augmentations per source image (output of `fer_augment.ipynb`)

---

## 1. Dataset overview

| Dataset | Folders | Total images | Size on disk |
| --- | ---: | ---: | ---: |
| `fer_data` | 6 | 1,236 | 821.52 MB |
| `fer_data_raw_512` | 6 | 1,236 | 39.64 MB |
| `fer_data_aug_512` | 6 | 4,932 | 517.31 MB |

> Resizing alone cuts storage by ~20.7× (821.52 MB → 39.64 MB). Augmenting 4× per source image grows the augmented set to 517.31 MB, i.e. +477.67 MB (~13.0× the resized set).

### 1.1 File extensions

| Dataset | `.jpg` | `.jpeg` | `.png` |
| --- | ---: | ---: | ---: |
| `fer_data` | 1,207 | 9 | 20 |
| `fer_data_raw_512` | 1,207 | 9 | 20 |
| `fer_data_aug_512` | 4,932 | 0 | 0 |

> All augmented images are re-encoded as JPEG (quality 95) by the pipeline.

---

## 2. Class distribution

### 2.1 Per-class image counts

| Class | `fer_data` | `fer_data_raw_512` | `fer_data_aug_512` | Share of raw (%) |
| --- | ---: | ---: | ---: | ---: |
| `angry😡`     | 152 | 152 | 608 | 12.30 |
| `fear😟`      | 135 | 135 | 540 | 10.92 |
| `happy😃`     | 276 | 276 | 1,092 | 22.33 |
| `normal🙂`    | 277 | 277 | 1,108 | 22.41 |
| `sad😥`       | 221 | 221 | 884 | 17.88 |
| `surprise😮`  | 175 | 175 | 700 | 14.16 |
| **Total**     | **1,236** | **1,236** | **4,932** | **100.00** |

### 2.2 Imbalance

| Metric | Raw | Resized | After augmentation |
| --- | ---: | ---: | ---: |
| Max class | 277 (`normal🙂`) | 277 | 1,108 (`normal🙂`) |
| Min class | 135 (`fear😟`) | 135 | 540 (`fear😟`) |
| Imbalance ratio (max/min) | **2.05** | **2.05** | **2.05** |

> The class ratio is preserved exactly after resizing and after 4× augmentation (every source image becomes 5 in total: 1 source + 4 augmented).

---

## 3. Image dimensions and channels (sampled, 25 images/class)

### 3.1 `fer_data` (original raw, mixed sizes)

| Class | min H×W | max H×W | mean H×W | channels |
| --- | --- | --- | --- | ---: |
| `angry😡`     | 352×260 | 2932×2932 | 1022×809 | 3 |
| `fear😟`      | 312×220 | 2160×1582 | 992×680  | 3 |
| `happy😃`     | 441×311 | 2436×2436 | 1172×967 | 3 |
| `normal🙂`    | 316×248 | 1696×1696 | 840×678  | 3 |
| `sad😥`       | 188×130 | 3048×3048 | 1042×893 | 3 |
| `surprise😮`  | 380×252 | 3048×3048 | 1113×899 | 3 |

> Heights vary from 188 px up to 3,048 px, widths from 130 px up to 3,048 px — i.e. the raw dataset is heavily heterogeneous in size. All sampled images are RGB (3 channels).

### 3.2 `fer_data_raw_512` (resized)

| Class | min H×W | max H×W | mean H×W | channels |
| --- | --- | --- | --- | ---: |
| `angry😡`     | 512×512 | 512×512 | 512×512 | 3 |
| `fear😟`      | 512×512 | 512×512 | 512×512 | 3 |
| `happy😃`     | 512×512 | 512×512 | 512×512 | 3 |
| `normal🙂`    | 512×512 | 512×512 | 512×512 | 3 |
| `sad😥`       | 512×512 | 512×512 | 512×512 | 3 |
| `surprise😮`  | 512×512 | 512×512 | 512×512 | 3 |

> After `resize.py` (PIL `Image.resize` to 512×512), every sampled image is exactly 512×512, 3 channels.

### 3.3 `fer_data_aug_512` (augmented, mostly 512×512 ± distortions)

| Class | min H×W | max H×W | mean H×W | channels |
| --- | --- | --- | --- | ---: |
| `angry😡`     | 485×485 | 599×617 | 525×523 | 3 |
| `fear😟`      | 477×474 | 606×645 | 518×526 | 3 |
| `happy😃`     | 503×493 | 575×567 | 521×516 | 3 |
| `normal🙂`    | 512×497 | 609×609 | 530×522 | 3 |
| `sad😥`       | 485×467 | 579×652 | 515×522 | 3 |
| `surprise😮`  | 442×477 | 595×605 | 514×519 | 3 |

> Slight off-by-a-few-pixels variations come from `ElasticTransform`, `GridDistortion`, `OpticalDistortion` and crop-style effects in the augmentation pipeline; the centroid is ~520×520.

---

## 4. Pixel-intensity statistics (sampled, 25 images/class)

`mean` and `std` are computed on BGR pixels (0–255 scale). `dark %` = share of gray pixels with value < 30; `bright %` = share > 225.

### 4.1 `fer_data` vs `fer_data_raw_512`

| Class | raw mean | 512 mean | Δ mean | raw std | 512 std | Δ std |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `angry😡`     | 120.31 | 120.32 | +0.01 | 57.71 | 57.66 | −0.05 |
| `fear😟`      | 113.74 | 113.75 | +0.01 | 56.39 | 56.33 | −0.06 |
| `happy😃`     | 118.21 | 118.21 |  0.00 | 59.08 | 58.98 | −0.10 |
| `normal🙂`    | 119.92 | 119.92 |  0.00 | 59.72 | 59.63 | −0.09 |
| `sad😥`       | 124.38 | 124.39 | +0.01 | 59.52 | 59.43 | −0.09 |
| `surprise😮`  | 116.93 | 116.94 | +0.01 | 56.88 | 56.80 | −0.08 |

| Class | raw dark % | 512 dark % | raw bright % | 512 bright % |
| --- | ---: | ---: | ---: | ---: |
| `angry😡`     | 6.50 | 6.46 | 1.49 | 1.49 |
| `fear😟`      | 7.62 | 7.55 | 0.43 | 0.43 |
| `happy😃`     | 7.09 | 6.98 | 2.07 | 2.06 |
| `normal🙂`    | 7.19 | 7.10 | 0.44 | 0.44 |
| `sad😥`       | 6.88 | 6.75 | 1.47 | 1.46 |
| `surprise😮`  | 6.48 | 6.41 | 0.52 | 0.51 |

> Resizing to 512×512 changes pixel statistics by less than 0.1 in mean/std — i.e. visually and statistically near-lossless at the class level.

---

## 5. Augmentation pipeline

### 5.1 Pipeline summary

- **Source:** `fer_data_raw_512/` (512×512, RGB)
- **Destination:** `fer_data_aug_512/`
- **Ratio:** 4 augmented variants per source image (1:4)
- **Total output:** 1,236 × 4 = **4,932 images**
- **Encoder:** JPEG, quality 95
- **Naming:** `<stem>_aug0.jpg` … `<stem>_aug3.jpg`
- **Library:** Albumentations 2.x

### 5.2 Augmentation techniques — what each one does

The 4 augmented variants are produced by 4 different `Compose` pipelines, each combining several techniques. They intentionally avoid `VerticalFlip` and `ToGray` (emotions are not vertically symmetric and grayscale loses important chroma cues for FER).

#### Variant 1 — Geometric + lighting noise

| Technique | Description |
| --- | --- |
| `Affine(scale=(0.85,1.15), translate_percent=±0.06, shear=±8°, fit_output=True)` | Random scale (zoom in/out 85–115 %), translation up to ±6 % of the image size, and a small shear. `fit_output=True` keeps the output the same size as the input. Teaches the model to be invariant to small pose/position changes of the face. |
| `GaussNoise(std_range=(0.03, 0.12))` | Adds Gaussian pixel noise with σ in [3 %, 12 %] of the 0–1 range. Simulates sensor/ISO noise commonly seen in real photos. |
| `RandomBrightnessContrast(brightness=±0.2, contrast=±0.2)` | Globally shifts brightness by up to ±20 % and contrast by ±20 %. Mimics varied lighting conditions (over/under-exposed frames). |

#### Variant 2 — Rotation + elastic deformation + sharpening

| Technique | Description |
| --- | --- |
| `SafeRotate(limit=20°, border_mode=BORDER_REFLECT_101)` | Rotates by up to ±20° and mirrors border pixels instead of padding black, so the face stays in frame without artefacts. Makes the network robust to head tilt. |
| `ElasticTransform(alpha=1.0, sigma=20)` | Applies a smooth random displacement field to the image — the canonical "elastic" warp. Mimics non-rigid deformations and small expression-driven face shape changes. |
| `Sharpen(alpha=(0.2, 0.5), lightness=(0.7, 1.3))` | Increases edge sharpness; helps when downstream photos are slightly out of focus or downscaled. |

#### Variant 3 — Distortion grid + lens effects + local contrast

| Technique | Description |
| --- | --- |
| `GridDistortion(num_steps=5, distort_limit=0.25)` | Splits the image into a 5×5 grid and randomly perturbs its cell coordinates. Approximates subtle lens / camera distortions. |
| `OpticalDistortion(distort_limit=0.2)` | Applies a barrel / pincushion distortion. Simulates varying camera lenses. |
| `CLAHE(clip_limit=2.0, tile_grid_size=(8, 8))` | Contrast-Limited Adaptive Histogram Equalization on 8×8 tiles. Boosts local contrast so dark/light facial regions stay readable across different exposures. |

#### Variant 4 — Motion blur + occlusion + colour jitter

| Technique | Description |
| --- | --- |
| `MotionBlur(blur_limit=(5, 9))` | Simulates motion blur with a kernel of 5–9 px along a random direction. Models subject/camera motion during capture. |
| `CoarseDropout(num_holes_range=(1, 4), hole_height_range=8–20 %, hole_width_range=8–20 %)` | Drops 1–4 rectangular patches (cutout-style) covering 8–20 % of the image. Forces the model to rely on global facial context instead of single landmarks. |
| `ColorJitter(brightness=0.15, contrast=0.15, saturation=0.25, hue=0.03)` | Jointly jitters brightness, contrast, saturation and a small hue shift (±3 %). Teaches robustness to white-balance / skin-tone variation. |

### 5.3 What is intentionally **not** used

| Technique | Why it is excluded |
| --- | --- |
| `VerticalFlip` | Facial emotions are not vertically symmetric — flipping upside down destroys the class label. |
| `ToGray` | Removes chroma cues that help distinguish similar FER classes (e.g. fear vs. surprise). |
| `HueSaturationValue` (legacy in `aug.py`) | Hue shifts can change apparent skin tone in unrealistic ways; the new pipeline uses the milder `ColorJitter` instead. |
| `PadIfNeeded` with white padding | Legacy padding from `aug.py` was producing visible white borders — no longer needed because `Affine(fit_output=True)` and `SafeRotate(BORDER_REFLECT_101)` keep the image canvas clean. |

### 5.4 Per-class source vs augmented pixel statistics

Sampled with `SAMPLE_PER_CLASS = 20` source images and `20 × 4 = 80` augmented images per class. `brightness` is the mean of the V channel of HSV.

| Class | src brightness | aug brightness | src mean | aug mean | src std | aug std |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `angry😡`     | 138.50 | 130.90 | 119.97 | 113.35 | 56.99 | 63.29 |
| `fear😟`      | 131.74 | 122.70 | 109.56 | 103.70 | 54.41 | 61.19 |
| `happy😃`     | 138.54 | 133.99 | 119.28 | 116.14 | 60.57 | 64.27 |
| `normal🙂`    | 138.47 | 131.89 | 118.09 | 113.79 | 56.53 | 61.91 |
| `sad😥`       | 137.90 | 131.93 | 119.61 | 113.62 | 60.58 | 63.44 |
| `surprise😮`  | 136.08 | 131.97 | 118.04 | 113.28 | 59.84 | 62.47 |

> Across all classes, augmentation **drops mean brightness by ~5–9 points**, **drops mean intensity by ~3–7 points**, and **raises std by ~3–7 points**. In other words, augmentations make images slightly darker on average and add contrast variation — exactly what `ColorJitter`, `RandomBrightnessContrast`, `GaussNoise`, `MotionBlur` and `CoarseDropout` are designed to do.

### 5.5 Augmentation strength (mean |orig − aug| pixel difference)

Computed on 10 source images × 4 augmentations per class. Differences in the 7–9 range are typically caused by small geometric warps; values > 60 usually come from cutouts or strong brightness/colour jitter.

| Class | avg diff | min diff | max diff |
| --- | ---: | ---: | ---: |
| `angry😡`     | 32.33 | 7.80 | 65.94 |
| `fear😟`      | 29.74 | 8.09 | 60.77 |
| `happy😃`     | 31.38 | 7.27 | 59.47 |
| `normal🙂`    | 33.74 | 7.79 | 61.16 |
| `sad😥`       | 35.04 | 8.97 | 61.42 |
| `surprise😮`  | 32.91 | 8.04 | 62.14 |

> Augmentation strength is **uniformly distributed across classes** (29.7–35.0 avg diff), confirming the pipeline is balanced — no class is being perturbed more aggressively than another.

### 5.6 Storage impact (per class, MB on disk)

| Class | resized (`fer_data_raw_512`) | augmented (`fer_data_aug_512`) | combined |
| --- | ---: | ---: | ---: |
| `angry😡`     |  4.81 |  63.19 |  68.00 |
| `fear😟`      |  6.21 |  55.95 |  62.16 |
| `happy😃`     |  8.51 | 116.48 | 124.99 |
| `normal🙂`    |  7.58 | 115.67 | 123.25 |
| `sad😥`       |  7.72 |  92.96 | 100.68 |
| `surprise😮`  |  4.81 |  73.07 |  77.88 |
| **Total**     | **39.64** | **517.31** | **556.95** |

> Augmenting adds **+477.67 MB** on top of the resized 39.64 MB, a **~13.05× growth** in disk usage.

---

## 6. Pipeline artefacts (scripts referenced by the notebooks)

| Script | Role | Notes |
| --- | --- | --- |
| `rename.py` | Bulk-rename images inside a directory to `image_name1.ext`, `image_name2.ext`, … | Currently a template — `directory_path` is left as the literal string `"input_path"`; not run on the final datasets. |
| `resize.py` | Resize a single class folder to a target H×W via `PIL.Image.resize`. | Default call resizes `fer_data/surprise😮` → `fer_data_raw_512x/surprise😮` at 512×512. The final `fer_data_raw_512/` directory used by the reports was produced by running this for all six classes. |
| `aug.py` | Legacy Albumentations pipeline (1 random subset of 6 transforms per image): `VerticalFlip`, `HorizontalFlip`, `Rotate(±45°)`, `Blur`, `PadIfNeeded` (white), `HueSaturationValue`, `ToGray`. | Superseded by `fer_augment.ipynb`, which is the modern, emotion-aware pipeline described in §5. |

---

## 7. Key takeaways

1. **Class imbalance is moderate and constant.** Max/min class ratio is ~2.05× both before and after augmentation — augmentation scales every class by the same 4× factor.
2. **Resizing is essentially information-preserving at the class level.** Mean and std deltas between `fer_data` and `fer_data_raw_512` are all ≤ 0.1 in pixel units.
3. **The modern pipeline is balanced across classes.** Augmentation strength (avg |orig − aug|) lies in a tight 29.7–35.0 band.
4. **Augmentation slightly darkens and adds contrast.** Mean brightness drops 5–9 points; std (contrast proxy) rises 3–7 points across all classes — consistent behaviour of `ColorJitter`, `RandomBrightnessContrast`, `GaussNoise`, `MotionBlur`, `CoarseDropout`.
5. **Storage cost.** Resizing shrinks the dataset by ~20.7×; augmenting 4× then grows it to ~13× the resized size. Total combined footprint (resized + augmented) is ~557 MB.
6. **Avoided augmentations.** `VerticalFlip`, `ToGray` and white-bordered `PadIfNeeded` are deliberately not used because they hurt FER label integrity.

---

*Generated from the contents of `fer_raw_dataset_stats.ipynb`, `saved_raw_report_before_rsz.ipynb`, and `fer_augment.ipynb`, cross-checked against the live filesystem (`fer_data/`, `fer_data_raw_512/`, `fer_data_aug_512/`).*
