from sklearn.linear_model import LinearRegression 
import streamlit as st
import pandas as pd
import pickle as pkl
import numpy as np
#import model
pipe = pkl.load(open("pipe.pkl","rb"))
df = pkl.load(open("df.pkl","rb"))

st.title("Laptop pridictor\n -by Adesh shrivastav")

#dropdown
company = st.selectbox("## Brand",df["CompanyName"].unique())
inch = st.selectbox("## Inches",df["Inches"].unique())
ram = st.selectbox("## RAM",df["Ram"].unique())
gpu = st.selectbox("## GPU",df["Gpu"].unique())
OpSys = st.selectbox("## Oprating System",df["OpSys"].unique())
Weight = st.selectbox("## Weight",df["Weight"].unique())
touchscr = st.selectbox("## Touch screen 0 = NO , 1 = Yes",df["touchscr"].unique())
new_res = st.selectbox("## Resolution",df["new_res"].unique())
Cpu_brand = st.selectbox("## Cpu brand",df["Cpu_brand"].unique())
HDD = st.selectbox("## Hard drive(in GB)",[0,128,256,512,1024,2048])
SSD = st.selectbox("## SSD(in GB)",[0,128,256,512,1024])
oth = st.selectbox("## Other storage (in GB)",[0,128,256,512,1024,2048])
SSDT = st.selectbox("## SSD Type if not select 0",df["SSD_Type"].unique())
Storage= st.selectbox("## Storage",df["Storage"].unique())

if st.button("predict Price"):
    query = [[company,inch,ram,gpu,OpSys,Weight,touchscr,new_res,Cpu_brand,HDD,SSD,oth,SSDT,Storage]]
    
    prise = pipe.predict(query)
    st.title(f"""Your laptop prise will be :""")
    st.title(float(int(prise[0])))



