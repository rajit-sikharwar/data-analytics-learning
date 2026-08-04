import matplotlib.pyplot as plt
study_hours = [3, 6, 9, 10, 12]
test_scores = [60, 75, 80, 90, 98]
plt.plot(
    study_hours,
    test_scores,
    marker="o",
    linestyle="-",
    color="b",
    label="Student Progress",
)

plt.title("Impact of Study Hours on Test Scores",
          fontsize=14,
          fontweight="bold",
          loc = 'left'
          )

plt.xlabel("Hours Spent Studying", fontsize=12)
plt.ylabel("Test Score (%)", fontsize=12)
plt.legend(loc="upper left")
plt.grid(True,
         axis = 'x', 
         # axis = 'y',
         color = 'gray',
         linestyle="--",
         alpha=1,
         ) #Grid lines added to the plot for better readability
plt.show()