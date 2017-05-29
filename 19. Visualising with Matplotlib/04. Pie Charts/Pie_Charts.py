import matplotlib.pyplot as plt

slices=[7,2,2,13]
activities=['sleeping', 'eating', 'working', 'playing']
cols=['c', 'm', 'r', 'b']

plt.pie(slices,
        labels=activities,
        colors=cols,
        startangle=90,
        shadow=False,
        explode=(0,0.5,0,0),
        autopct='%1.1f%%')

plt.title('Interesting Graph\nCheck it out')
plt.show()