import streamlit as st

st.set_page_config(page_title="Streamlit App", layout="centered")

st.title("My Streamlit App")
st.write("Hello! If you can see this message, the Streamlit app is successfully connected and deployed.")

user_text = st.text_input("Enter some text:")
if st.button("Submit"):
    st.success(f"You entered: {user_text}")
