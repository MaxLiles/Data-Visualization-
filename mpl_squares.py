import matplotlib.pyplot as pyplot

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

pyplot.style.use('seaborn')
fig, ax = pyplot.subplots()


ax.plot(input_values, squares, linewidth=3)

ax.set_title("Square numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

ax.tick_params(axis='both', labelsize=14)



pyplot.show()
