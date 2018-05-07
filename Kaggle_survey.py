import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

kaggle_survey_csv = "https://storage.googleapis.com/kaggle_survey/kagglesurvey.csv"
responses = pd.read_csv(kaggle_survey_csv)
responses.head()

print(responses.shape)
print(responses.columns)

#處理數據
tools_select = responses["WorkToolsSelect"].str.split(pat = ",")
tools_select_lst = []
for i in tools_select:
  if not isinstance(i, list):
    tools_select_lst.append(str(i))
  else:
    for j in i:
      tools_select_lst.append(j)

#列印出工具數量
print(len(tools_select_lst))

#列出前20最受歡迎的工具
tools_select_df = pd.DataFrame(
    {
        "tools_select": tools_select_lst
    }
)
grouped = tools_select_df.groupby("tools_select")
grouped.size().sort_values(ascending = False)[:20]

#列印出前20名熱門工具（畫圖）
top20_tools = grouped.size().sort_values(ascending = False)[:20].sort_values()
top20_tools.plot.barh()

plt.show()
