import pandas as pd
from pandas.io.json import json_normalize
pd.__version__
import matplotlib.pyplot as plt
import json


dict = {}
count = 0
with open("commitComments.json") as json_file:
    json_data = json.load(json_file)

data = json_data['data']['viewer']['contributedRepositories']['edges']
result = json_normalize(data) 
result

for index, row in result.iterrows():
    commitId = json_normalize(row['node.commitComments.edges'])
    count=len(commitId.index)
    name = row['node.name']
    if name not in dict:
        dict[name] = 0
    dict[name] += count

df = pd.DataFrame.from_dict(dict,orient="index")
print(df)
df
df.plot.bar(subplots=True, figsize=(8, 8))
plt.show()
