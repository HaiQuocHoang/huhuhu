import streamlit as st
import base64

st.set_page_config(page_title="🐻 Gấu cute kéo chữ", layout="wide")

st.title("Tặng b Manh xinh gái nè")

with open("Conheo.png", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode()

image_url = f"data:image/png;base64,{encoded_string}"

st.markdown(f"""
<style>
body {{
  background-color: #ffffff !important;
  color: #ff0000 !important;
  margin: 0;
  padding: 0;
  font-family: Arial, sans-serif;
}}

@keyframes move {{
  0% {{ transform: translateX(100%); }}
  100% {{ transform: translateX(-100%); }}
}}

#bear-container {{
  font-size: 36px;
  font-weight: bold;
  color: #ff0000;
  animation: move 10s linear infinite;
  white-space: nowrap;
  overflow: hidden;
  position: relative;
  display: flex;
  align-items: center;
  height: 100px;
}}

#bear-img {{
  height: 70px;
  margin-left: 10px;
}}
</style>

<div id="bear-container">
  <img id="bear-img" src="{image_url}" />
  Hello b Manh~~~
  Chúc b Manh một ngày tốt lành! 
</div>
""", unsafe_allow_html=True)
