import streamlit as st
import pandas as pd
import pymssql
import numpy as np
import datetime
import time
import pyodbc

# DB 연결
#conn = pymssql.connect(host=st.secrets['server'], user=st.secrets['username'], password=st.secrets['password'], database=st.secrets['database'], charset="utf8", autocommit=True)
#conn = pymssql.connect(host='192.168.35.201:1433', user='root', password='Aa1234!!', database='Delivery', charset="utf8", autocommit=True)
conn_str= (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=121.125.187.152;"
    "DATABASE=Delivery;"
    "UID=root;"
    "PWD=Aa1234!!;"        
)
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# 재고부족 확인
def TEST():
    fu_query = "SELECT * FROM DeliveryStand01t"
    data = pd.read_sql_query(fu_query,conn)
    DeliveryData = pd.DataFrame(data)
    return DeliveryData

    
