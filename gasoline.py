import seaborn as sns
import pandas as pd

gas_df = pd.read_csv(filepath_or_buffer="gasolina.csv")
#gas_df.head()

gas_plot = sns.lineplot(data=gas_df, x="dia", y="venda")

fig = gas_plot.get_figure()
fig.savefig('gasolina.png')  