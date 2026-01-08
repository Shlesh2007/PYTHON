import streamlit as st
import random 
# st.sidebar.title("Student Info")
# a=st.sidebar.selectbox("Select Batch",["B1","B2","B3"])
# b=st.sidebar.radio("Select Subject",["PYTHON","FSD"])
# if b=="PYTHON":
#     title=st.text_input("Enter Your Project's Title: ")
#     en=st.number_input("Enter Your Enrollment No: ")
#     des=st.text_area("Enter Your Description: ")
#     st.write(a)
#     st.write(b)
# if b=="FSD":
#     title=st.text_input("Enter Your Project's Title: ")
#     en=st.number_input("Enter Your Enrollment No: ")
#     des=st.text_area("Enter Your Description: ")
#     st.write(a)
#     st.write(b)
# but=st.button("submit")
# if but:
#     st.write(a)
#     st.write(b)
#     st.write(title)
#     st.write(en)
#     st.write(des)
if st.button("Generate Random Number"):
    num=random.randint(0,100)
    st.write(num)
    if num>=1 and num<=30:
        st.image("download.jfif")
    elif num>30 and num<=60:
        st.audio("krish.mp3")
    else:
        st.video("samplevideo.mp4")