import matplotlib.pyplot as plt
study_hours = [2, 4, 6, 8, 10]
test_scores = [55, 68, 75, 88, 94]
plt.plot(
    study_hours,
    test_scores,
    marker="o",
    linestyle="-",
    color="b",
    label="Student Progress",
)

font1 = {'family':'serif','color':'blue','size':15}
font2 = {'family':'serif','color':'darkred','size':10}


plt.title("Impact of Study Hours on Test Scores",
          fontsize=14,
          fontweight="bold",
          fontdict = font1, 
          loc = 'left'
          )

plt.xlabel("Hours Spent Studying", fontsize=12, fontdict = font2)
plt.ylabel("Test Score (%)", fontsize=12)
plt.legend(loc="upper left")
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()