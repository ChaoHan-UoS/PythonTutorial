# Here is a stateful way of working with plots as we import the plt object and change its current state in terms of
# what figure and axis we're currently working with.

import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('seaborn')

data = pd.read_csv('data.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

# As long as no new figure or axes is explicitly created (e.g., by calling plt.figure() or plt.subplots()),
# all subsequent plotting commands (plt.plot(), plt.scatter(), etc.) will apply to the current figure and axes.
plt.plot(ages, py_salaries, label='Python')  # Implicitly create a figure and an axes (subplot)
plt.plot(ages, js_salaries, label='JavaScript')  # Plot data on the current figure and axes
plt.plot(ages, dev_salaries, color='#444444',
         linestyle='--', label='All Devs')

# # Get current figure and axes created by the first plt.plot()
# fig = plt.gcf()
# ax = plt.gca()

plt.legend()
plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')

plt.tight_layout()
plt.show()