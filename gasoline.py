import pandas as pd
import seaborn as sns

gas_df = pd.read_csv(filepath_or_buffer="gasolina.csv")
gas_df.head() 

gas_plot = sns.lineplot(data=gas_df, x="dia", y="venda")
gas_plot.set(xlabel = 'Dia', ylabel = 'Venda', title="Venda de gasolina por dia")

fig = gas_plot.get_figure()
fig.savefig('gasolina.png') 