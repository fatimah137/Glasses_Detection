import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image

st.title("Klasifikasi Penggunaan Kacamata")
model = load_model('glasses_classifier_fixed.h5')

uploaded_file = st.file_uploader("Upload gambar wajah", type=["jpg", "png", "jpeg"])

if uploaded_file:
    img = Image.open(uploaded_file).convert("RGB").resize((150, 150))
    st.image(img, caption='Gambar yang diunggah', use_column_width=True)
    
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    
    pred = model.predict(img_array)[0][0]
    label = "Dengan Kacamata" if pred >= 0.5 else "Tanpa Kacamata"
    st.write(f"**Prediksi: {label}**")
