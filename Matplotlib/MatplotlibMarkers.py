import matplotlib.pyplot as plt
x = [5, 8, 1, 10]
y = [8, 6, 1, 12]

plt.plot(
    x,
    "o:r",
    markersize=20,
    linewidth=3,
    markeredgecolor="r",
    markerfacecolor="g",
)
plt.plot(
    y,
    "o:r",
    markersize=15,
    linewidth=5,
    markeredgecolor="b",
    markerfacecolor="g",
)
plt.show()





'''1. Marker Reference
'o'	Circle	
'*'	Star	
'.'	Point	
','	Pixel	
'x'	X	
'X'	X (filled)	
'+'	Plus	
'P'	Plus (filled)	
's'	Square	
'D'	Diamond	
'd'	Diamond (thin)	
'p'	Pentagon	
'H'	Hexagon	
'h'	Hexagon	
'v'	Triangle Down	
'^'	Triangle Up	
'<'	Triangle Left	
'>'	Triangle Right	
'1'	Tri Down	
'2'	Tri Up	
'3'	Tri Left	
'4'	Tri Right	
'|'	Vline	
'_'	Hline
'''


''' 2. Line References
'-'	    Solid line	
':'	    Dotted line	
'--'	Dashed line	
'-.'	Dashed/dotted line
'''