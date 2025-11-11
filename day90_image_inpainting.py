# day90_image_inpainting.py
# 🎨 Image Inpainting – Remove Objects from Photos (Day 90)

import cv2
import numpy as np
import streamlit as st
from PIL import Image

st.set_page_config(page_title="🖼️ Image Inpainting", layout="wide")
st.title("🎨 Image Inpainting – Remove Objects from Photos")
st.write("Upload an image and a mask to remove unwanted objects using OpenCV.")

# ------------------------------
# 📤 Upload Section
# ------------------------------
uploaded_img = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])
uploaded_mask = st.file_uploader("Upload Mask (White = Remove area)", type=["jpg", "png", "jpeg"])

method = st.selectbox("Choose Inpainting Method", ["Telea", "Navier-Stokes"])
radius = st.slider("Inpainting Radius", 1, 10, 3)

# ------------------------------
# 🧠 Inpainting Function
# ------------------------------
def inpaint_image(image, mask, radius, method):
    flag = cv2.INPAINT_TELEA if method == "Telea" else cv2.INPAINT_NS
    inpainted = cv2.inpaint(image, mask, radius, flag)
    return inpainted

# ------------------------------
# 🚀 Processing
# ------------------------------
if uploaded_img and uploaded_mask:
    image = np.array(Image.open(uploaded_img).convert("RGB"))
    mask = np.array(Image.open(uploaded_mask).convert("L"))

    st.image([image, mask], caption=["Original Image", "Mask"], width=300)

    if st.button("🧹 Remove Object"):
        inpainted = inpaint_image(image, mask, radius, method)
        st.image(inpainted, caption="✨ Inpainted Result", use_container_width=True)
        st.success("✅ Object removed successfully!")

else:
    st.info("👆 Please upload both an image and a mask to proceed.")

st.markdown("---")
st.caption("Developed by Vaishnavi • Day 90 of 100 Days of ML Challenge")
