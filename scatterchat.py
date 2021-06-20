import pandas as pd
import plotly.express as px
df=pd.read_csv("scatter.csv")
fig=px.scatter(df,x="date\tcases\tcountry", y="date\tcases\tcountry",color="date\tcases\tcountry")
fig.show()