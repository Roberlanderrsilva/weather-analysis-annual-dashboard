import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. Gerando dados de 365 dias
datas = pd.date_range(start='2025-01-01', periods=365)
temp = 20 + 10 * np.sin(np.linspace(0, 3 * np.pi, 365)) + np.random.normal(0, 2, 365)
chuva = np.random.choice([0, 1, 5, 10], size=365, p=[0.7, 0.15, 0.1, 0.05])

df = pd.DataFrame({'Data': datas, 'Temp': temp, 'Chuva': chuva})
df['Mes'] = df['Data'].dt.month

# Configurando o Dashboard (Layout com 3 gráficos)
fig = plt.figure(figsize=(12, 10))
plt.subplots_adjust(hspace=0.4)

# --- GRÁFICO 1: Linhas (Tendência Anual) ---
ax1 = plt.subplot(2, 1, 1)
ax1.plot(df['Data'], df['Temp'], color='salmon', alpha=0.5, label='Temp. Diária')
ax1.plot(df['Data'], df['Temp'].rolling(30).mean(), color='red', linewidth=2, label='Média Móvel (30 dias)')
ax1.set_title('Análise de Tendência Térmica Anual', fontsize=14)
ax1.legend()

# --- GRÁFICO 2: Barras (Médias Mensais) ---
ax2 = plt.subplot(2, 2, 3)
media_mensal = df.groupby('Mes')['Temp'].mean()
ax2.bar(media_mensal.index, media_mensal.values, color='skyblue')
ax2.set_title('Média de Temperatura por Mês', fontsize=12)
ax2.set_xticks(range(1, 13))

# --- GRÁFICO 3: Pizza (Distribuição de Chuva) ---
ax3 = plt.subplot(2, 2, 4)
dias_chuva = (df['Chuva'] > 0).sum()
dias_seco = 365 - dias_chuva
ax3.pie([dias_chuva, dias_seco], labels=['Com Chuva', 'Seco'], autopct='%1.1f%%', colors=['dodgerblue', 'orange'])
ax3.set_title('Proporção de Dias Chuvosos', fontsize=12)

# Salvando a versão profissional
plt.savefig('dashboard_anual.png')
print("Sucesso! Dashboard multi-gráfico gerado.")
