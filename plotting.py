from main import df

from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool, ColumnDataSource

df["Start_string"] = df["Start"].dt.strftime("%d-%m-%Y %H:%M;%s")
df["End_string"] = df["End"].dt.strftime('%d-%m-%Y %H:%M;%s')

cds = ColumnDataSource(df)

p = figure(x_axis_type="datetime", height=100, title="Motion Graph", sizing_mode="scale_width", width=500)
p.yaxis.minor_tick_line_color = None
p.yaxis.ticker.desired_num_ticks = 1

hover = HoverTool(tooltips=[("Start", "@Start_string"), ("End", "@End_string")])
p.add_tools(hover)

q = p.quad(left="Start", right="End", bottom=0, top=1, color="green", source=cds)
output_file("Graph.html")
show(p)
