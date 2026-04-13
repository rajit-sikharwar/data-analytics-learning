# importing the modules 
from bokeh.plotting import figure, output_file, show 

# instantiating the figure object 
graph = figure(title = "Bokeh Line Graph") 

# the points to be plotted 
x = [1, 2, 3, 4, 5] 
y = [5, 4, 3, 2, 1] 

graph.line(x, y) 
show(graph)

#2. Legend Implementation
# plotting the 1st line graph
graph.line(x, x, legend_label="Line 1", line_color="green")

# plotting the 2nd line graph with a different color
graph.line(y, x, legend_label="Line 2", line_color="blue")
show(graph)