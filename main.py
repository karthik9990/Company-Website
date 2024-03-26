import streamlit as st
import pandas

st.set_page_config(layout="wide")

content = """
Company Profile:

Acme Solutions Inc. is a leading innovator in the tech industry. With a commitment to excellence and a mission to 
create the next generation of technological tools, we strive to deliver the best and most convenient digital 
solutions to our clients. Our team of dedicated professionals works tirelessly to ensure that our products are at the 
forefront of the digital revolution. With a focus on creativity, innovation, and efficiency, Acme Solutions Inc. is 
shaping the future of technology, one product at a time. Join us as we continue to push the boundaries of what’s 
possible in the digital world."""

st.title("Acme Solutions Inc.")
st.info(content)
st.subheader("Our Team:")
col1, col2, col3 = st.columns(3)

df = pandas.read_csv("data.csv", sep=",")

with col1:
    for index, row in df[:4].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images/" + row["image"])

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images/" + row["image"])

with col3:
    for index, row in df[8:].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images/" + row["image"])




