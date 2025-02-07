import csv
import numpy as np
import pandas as pd
from collections import Counter
# import matplotlib
# matplotlib.use("TkAgg")  # Do this before importing pyplot!
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

# ---Loading .csv via the csv module from the standard library---
with open('data.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)  # An iterator contains ordered dictionaries of each responder
    # row = next(csv_reader)  # The OrderedDict of the first responder
    # print(row['LanguagesWorkedWith'])  # A string of programming languages
    # print(row['LanguagesWorkedWith'].split(';'))  # A list of programming languages

    language_counter = Counter()
    for row in csv_reader:
        language_counter.update(row['LanguagesWorkedWith'].split(';'))


# ---Loading .csv using read_csv() method from pandas / load.txt() from numpy---
data = pd.read_csv('data.csv')
ids = data['Responder_id']
lang_responses = data['LanguagesWorkedWith']

language_counter = Counter()
for response in lang_responses:
    language_counter.update(response.split(';'))


# ---Plotting horizontal bar chart---
languages = []
popularity = []

# print(language_counter.most_common(15))  # A list of tuple pairs of most common languages
for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

print(languages)
print(popularity)

languages.reverse()
popularity.reverse()
plt.barh(languages, popularity)  # Horizontal bar chart

plt.title('Most Popular Languages')
# plt.ylabel("Programming Languages")
plt.xlabel("Number of People Who Use")

plt.tight_layout()
plt.show()
