!pip install pyshorteners
import streamlit as st
import pyshorteners
import time

st.set_page_config(page_title="URL Shortner",     page_icon="🧊")
s = pyshorteners.Shortener()
st.title('🧊 URL Shortner')
st.header("Enter a long URL to get a shortened version")
st.sidebar.empty()
st.sidebar.write("Pick a Color for Background")
st.toast("Welocme to My link Shortner Project",icon="👋")
color = st.sidebar.color_picker('')
st.markdown(
    f"""
    <style>
    .stApp {{
        background-color : {color}
    }}
    </style>
    """,
    unsafe_allow_html=True
)
long = st.text_input("",placeholder="https://google.com")
if st.button("Shorten URL"):
    if long:
        with st.spinner("Shortening URL..."):
            time.sleep(2)
            try:
                short = s.tinyurl.short(long)
                st.success("URL successfullr shortened!")
                # st.markdown(f"shortened URL {short}")
                # st.write("Copt the button to copy the shortened URL.")
                st.code(short)
                
            except Exception as e:
                st.error(f"Error: {str(e)}")
                
    else:
        
        st.warning("Please enter a valid URL.")
