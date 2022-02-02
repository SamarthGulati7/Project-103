import pandas as pd
import plotly.express as pe

df= pd.read_csv('covid_cases.csv')
fig= pe.scatter(df,x='date',y='cases',color='country',title='No. of cases in different countries')
fig.show()