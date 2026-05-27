import streamlit as st
st.title(" Ankitha super market sales analysis")
col1,col2,col3 = st.columns(3)
with col1:
    st.metric(label="Total sales",value='$1,000,000',delta="+18%")
with col2:
    st.metric(label="Total customers",value="$10,000",delta="-5%")
with col3:
    st.metric(label="Average order value",value="$100",delta="+10%")

import streamlit as st
st.title("visualization Analysis")
st.header("Montly Analysis")
st.subheader("Day-wise Analysis")
st.text(" This is Plain Text")
name = st.text_input("Enter Name")

password = st.text_input("Enter Password",type="password")

st.write(f"Name: {name}")
st.write(f"Password: {password}")
age = st.number_input("Enter Age")
st.write(f"Age: {age}")


salary =st.slider("Select Salary",10000,100000,500000)

st.write(f"Salary: {salary}")
gender = st.radio("Select Gender",["Male","Female"])

st.write(f"Gender: {gender}")

skills = st.multiselect("Select skills",["Python","Sql","Power BI"])

Agree = st.checkbox("Accept Terms")
st.write(Agree)
submit = st.button("Submit")
st.write(submit)

date = st.date_input("Select Date")

time = st.time_input("Select Time")

file = st.file_uploader("Upload File")

color = st.color_picker("pick Color")

st.write(f"Selected Date: {date}")
st.write(f"Selected Time: {time}")
st.write(f"Uploaded File: {file}")
st.write(f"Selected color: {color}")