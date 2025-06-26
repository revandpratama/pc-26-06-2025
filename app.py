import streamlit as st
import cv2

st.title("Web Pengolahan Citra - R8M")

images = cv2.imread("123.png")

option = st.selectbox(
    "Operasi Citra",
    ("kontras", "negasi", "campur")
)

col1, col2 = st.columns(2)

if option == "kontras":

    with col1:
        st.image(images, channels="BGR")

    with col2:
        contrastImg = cv2.addWeighted(images, 5, images, 0, 0)
        st.image(contrastImg, channels="BGR")

elif option == "negasi":
    with col1:
        st.image(images, channels="BGR")

    with col2:
        negasiImg = cv2.bitwise_not(images)
        st.image(negasiImg, channels="BGR")

elif option == "campur":
    with col1:
        st.image(images, channels="BGR")

    with col2:
        col21, col22 = st.columns(2)
        contrastImg = cv2.addWeighted(images, 5, images, 0, 0)
        negasiImg = cv2.bitwise_not(images)
        with col21:
            st.image(contrastImg, channels="BGR")
        with col22:    
            st.image(negasiImg, channels="BGR")
else:
    st.image(images, channels="BGR")

# if __name__ == "__main__": 