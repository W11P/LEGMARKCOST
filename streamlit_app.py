import pandas as pd
import streamlit as st
from pathlib import Path

Click_rate = st.number_input('Click Through Rate?', step=1)

web_rate =st.number_input('Website Conversation Rate?',step=1)

a=Click_rate
b=web_rate

def formula_lg(a,b):
    c = int(a)+int(b)
    return c
#print(formula_lg(a))
st.write('This is the answer=',formula_lg(a,b))
data_set ='./testCVS.csv'
#data_set = "C:\\Users\\wil\\PycharmProjects\\pythonProject1\\pythonProject\\LegmarkCost\\venv\\testCVS.csv"
#data_set = "https://github.com/W11P/LEGMARKCOST/blob/94a6d9d58a867c3edbd137f3b2c4b902856af5f7/testCVS.csv"
#st.write(data_set)
df = pd.read_csv(data_set)

injury_column= df.columns[0]
drop_down_box = st.selectbox(
    label="Select a Injury",
    options=df[injury_column].tolist()
)

if drop_down_box is not None:
    st.write(drop_down_box)
    index_column=df[injury_column].tolist().index(drop_down_box)
#    st.write(index_column)


lawer_class_row =df.columns.tolist()
#st.write(lawer_class_row)
drop_down_box_2=st.selectbox(
    label="Select a Type",
    options=lawer_class_row
)
if drop_down_box_2 is not None:
    st.write(drop_down_box_2)
    index_heading=lawer_class_row.index(drop_down_box_2)
#    st.write(index_heading)


returned_value = df.iat[index_column,index_heading]
st.write('index value:-',returned_value)

def calculated_value(a,b,returned_value):
    c = int(a)+int(b)*returned_value
    return c
st.write('Formula result:-',calculated_value(a,b,returned_value))
st.write(df)
