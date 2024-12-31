import streamlit as st
import pandas as pd

st.write("AVD2")
data ={
	 	'Task' : ['Extract', 'Transform' , 'Load'],
		'Status' : ['Completed' , 'InProgress' , 'Pending']
	}
df = pd.DataFrame(data)
st.write('ETL Pipeline Execution Status',df)	# st.write(df)
