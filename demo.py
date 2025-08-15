import numpy as np
import pandas as pd
import streamlit as st

st.title("It's Friday!")
st.write("## The weather is nice today")
st.write("### Let's creative webpage using streamlit")
st.write("#### This is a simple demo of streamlit")
st.write("##### We can use markdown to format text")
st.write("###### This is the end of the demo")
arr1 = np.array([1, 2, 3, 4, 5])
st.write(arr1)

df1 = pd.DataFrame ([[11, 22, 33, 44, 55],[50,60,70,80]])
st.write(df1)
st.table(df1)

st.write("## 核取方塊")
r1=st.checkbox("外帶")
if r1:
    st.info("外帶")
else:
    st.info("內用")


checks=st.columns(3)
txt=""
with checks[0]:
    r11=st.checkbox("A")
    if r11:
        txt+="A "
with checks[1]:
    r12=st.checkbox("B")
    if r12:
        txt+="B"
with checks[2]:      
    r13=st.checkbox("C")
    if r13:
        txt+=" C"
st.info(txt)

st.write("## 單選按鈕")
b1=st.radio("飲料", ["果汁", "可樂", "咖啡", "茶"])
st.info(b1)
b2=st.radio("飲料", ["果汁", "可樂", "咖啡", "茶"],key="drink2")
st.info(b2)

st.write("## 多選按鈕")
c1=st.multiselect("飲料", ["果汁", "可樂", "咖啡", "茶"])
st.info(c1)

st.write("## 滑桿")
num=st.slider("請選擇數量:", 0, 100, 50, step=5)
st.info(num)


st.write("## 下拉選單")
select1=st.selectbox("請選擇飲料", ["果汁", "可樂", "咖啡", "茶","others"])
if select1 == "果汁":
    st.info("你選擇了果汁")
elif select1 == "可樂":
    st.info("你選擇了可樂")
elif select1 == "咖啡":
    st.info("你選擇了咖啡")
elif select1 == "茶":
    st.info("你選擇了茶")
else:
    st.info("你選擇了其他")

st.sidebar.write  ("##下拉選單")
city=st.sidebar.selectbox("居住地", ("台北", "新北", "桃園", "台中", "台南", "高雄"))
if city=="台北":
    st.sidebar.info("A")
elif city=="新北":
    st.sidebar.info("B")
elif city=="桃園":
    st.sidebar.info("C")
elif city=="台中":
    st.sidebar.info("D")    
elif city=="台南":
    st.sidebar.info("E")    

st.write("## 按鈕 ")
a = st.number_input("num...")
b = st.number_input("num...",key='b')
if st.button("相加"):
    st.write("###", a+b)
    

