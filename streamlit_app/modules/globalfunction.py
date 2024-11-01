import streamlit as st
import pandas as pd
import pymssql
import numpy as np
import datetime
import time
import pyodbc

# DB 연결
#conn = pymssql.connect(host='192.168.110.49:1433', user='APR', password='Aa1234!!', database='APR', charset="utf8", autocommit=True)
conn_str= (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=192.168.110.49,1433;"
    "DATABASE=APR;"
    "UID=APR;"
    "PWD=Aa1234!!;"        
)
conn = pyodbc.connect(conn_str)

cursor = conn.cursor()

# 재고부족 확인
def TEST():
    fu_query = "SELECT TOP 5 CONVERT(NVARCHAR(50),Manager) Manager,TrackNumber FROM DHL01T "
    data = pd.read_sql_query(fu_query,conn)
    DeliveryData = pd.DataFrame(data)
    return DeliveryData
