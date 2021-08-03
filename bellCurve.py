import plotly.express as px
import csv
import pandas as pd
import plotly.figure_factory as ff



dataFile = pd.read_csv("pro/bellCurve/data.csv")
fig = ff.create_distplot([dataFile["Avg Rating"].tolist()],["Average Rating"],show_hist=False)
fig.show()
