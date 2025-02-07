import matplotlib
print(matplotlib.get_backend())  # Check the currently active (default) backend
# Need to specify the backend before importing pyplot, otherwise pyplot will load the default backend when imported
matplotlib.use("TkAgg")  # overrides the default backend (e.g., mpld3 backend for inline plotting if "Show plots in tool window" is enabled)
print(matplotlib.get_backend())  # backend changed to TkAgg
from matplotlib import pyplot as plt

print(plt.style.available)
# plt.style.use('fivethirtyeight')
plt.style.use('ggplot')

# plt.xkcd()  # xkcd comic style

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]
# plt.plot(ages_x, py_dev_y, color='#5a7d9a', linewidth=3, label='Python')
plt.plot(ages_x, py_dev_y, label='Python')

js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]
# plt.plot(ages_x, js_dev_y, color='#adad3b', linewidth=3, label='JavaScript')
plt.plot(ages_x, js_dev_y, label='JavaScript')

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]
plt.plot(ages_x, dev_y, color='#444444', linestyle='--', label='All Devs')

plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.title('Median Salary (USD) by Age')
plt.legend()
# plt.grid(True)
plt.tight_layout()

# plt.savefig('plot.pdf')
plt.show()

print("Done.")
