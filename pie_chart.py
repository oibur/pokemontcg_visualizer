import matplotlib.pyplot as plt

# # Pie chart, where the slices will be ordered and plotted counter-clockwise:
# labels = 'Gen 8', 'Gen 7', 'Gen6', 'Gen5', 'Gen4', 'Gen3',  'Gen2', 'Gen1'
# sizes = [3.45, 5.55, 4.85, 12.15, 10.95, 17.55, 14.55, 30.95]

# fig1, ax1 = plt.subplots()
# ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
#         shadow=True, startangle=90)
# ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
# ax1.set(title='Each Gens Percent of Total Cards')

# plt.show()

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Gen 8', 'Gen 7', 'Gen6', 'Gen5', 'Gen4', 'Gen3',  'Gen2', 'Gen1'
sizes = [9.85, 9.85, 8.05, 17.35, 11.85, 15.05, 11.15, 16.85]

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax.legend(labels,
          title="Gens",
          loc="center left",

ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax1.set(title='Each Gens Percent of Total Pokemon')

plt.show()

