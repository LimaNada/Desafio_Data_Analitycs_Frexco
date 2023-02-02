import pandas as pd
import warnings
from statsmodels.tsa.arima.model import ARIMA


# Importando e criando o DataFrame com os dados de vendas
df = pd.read_excel("Dados.xlsx")

# Definindo a coluna de Data como índice
df = df.set_index('Data')

# Tirando o aviso padrão do ARIMA que pode aparecer em alguns computadores
warnings.filterwarnings("ignore")

# Criando a estrutura pelo método ARIMA
model = ARIMA(df, order=(1, 1, 1), freq='D')
model_fit = model.fit()

# Realizando a previsão para os próximos 5 dias
previsao = model_fit.forecast(steps=5)

# Criando um DataFrame com a previsão
dataFP = pd.DataFrame(previsao)
dataFP.columns = ['Previsão de Vendas']
dataFP = dataFP.rename_axis("Data", axis=1)

# Formatando o DataFrame
dataFP.index = dataFP.index.strftime('%d/%m/%Y')
dataFP = dataFP.astype({"Previsão de Vendas": int})

# Exibindo a previsão de demanda para os próximos 5 dias
print(dataFP)
