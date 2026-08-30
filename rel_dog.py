



from PIL import Image
import numpy as np

# =========================
# Settings
# =========================
input_file = "dog_miniature_dachshund.png"
output_file = "dog_relativistic_0999.png"

beta = 0.999  # v/c
motion_direction = "x"   # "x" or "y"


# =========================
# Lorentz contraction
# =========================
if not (0 <= beta < 1):
    raise ValueError("beta must satisfy 0 <= beta < 1")

gamma = 1.0 / np.sqrt(1.0 - beta**2)
contraction = 1.0 / gamma

print(f"beta = {beta:.3f}")
print(f"gamma = {gamma:.3f}")
print(f"L/L0 = {contraction:.3f}")


# =========================
# Load image
# =========================
img = Image.open(input_file)

w, h = img.size

if motion_direction == "x":
    new_w = max(1, int(w * contraction))
    new_h = h

elif motion_direction == "y":
    new_w = w
    new_h = max(1, int(h * contraction))

else:
    raise ValueError('motion_direction must be "x" or "y"')


# High-quality resize
img_contracted = img.resize(
    (new_w, new_h),
    Image.Resampling.LANCZOS
)

img_contracted.save(output_file)

print(f"original size : {w} x {h}")
print(f"contracted size: {new_w} x {new_h}")
print(f"saved to {output_file}")