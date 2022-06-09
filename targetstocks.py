import numpy as np
import bokeh
import pandas as pd
import datetime as dt
from bokeh.io import curdoc
from bokeh.plotting import figure, output_file, show

data = pd.read_csv('C:/Users/Grayson/Dropbox/PC/Downloads/tgt_price-history-06-09-2022 (1).csv')
data.drop(data.index[data['Time'] == 0], inplace = True)

output_file("tgt.html")
curdoc().theme = 'dark_minimal'

graph = figure(x_axis_type= "datetime",title = "Target Stocks (2020-2022)",height=350,width=600)

graph.xaxis.axis_label = "Date"
graph.yaxis.axis_label = "Price (in USD)"

dates = data['Time']
dates = pd.to_datetime(dates)

prices = data['Last']

graph.line(dates,prices,color = "red",line_cap="round",line_join="round",line_width=1)
graph.line(dates,prices,color = "red",line_cap="round",line_join="round",line_width=4,line_alpha=0.35) # Glow effect for fun

show(graph)
