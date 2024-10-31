import streamlit as st
import pandas as pd
import pymssql
import numpy as np
import datetime
from modules.nav import sidebar
from containter.footer import footer
from modules.globalfunction import *

st.set_page_config(page_title="ERP운영팀 해외",
                   page_icon="🔥",
                   layout="wide")

vert_space = '<div style="padding: 20px 5px;"></div>'

sidebar()
footer()

curdate = datetime.datetime.now()
curdate = curdate.strftime("%Y-%m-%d")

curweek = datetime.datetime.now()
curweek = curweek.strftime("%w")

if curweek == "1":
    curweek = "월"
elif curweek == "2":
    curweek = "화"
elif curweek == "3":
    curweek = "수"
elif curweek == "4":
    curweek = "목"
elif curweek == "5":
    curweek = "금"
elif curweek =="6":
    curweek = "토"
elif curweek == "0":
    curweek ="일"
else:
    curweek = "에러"

with st.spinner('Data Loading Please Wait...'):

    st.title('🔥APR 해외 모니터링')
    st.subheader("📅날짜 : "+curdate+"("+curweek+")")

    st.markdown(vert_space, unsafe_allow_html=True)
    Range1, Range2, Range3 = st.columns(3)

    # 범위1
    with Range1:
        #재고부족 확인
        st.markdown("### 재고부족 확인")  

        ClaimDupliPointAllData=TEST()
        if ClaimDupliPointAllData is not True:
            st.dataframe(ClaimDupliPointAllData)  
