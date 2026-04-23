import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. Gerando dados de 365 dias
dias = np.arange(1, 366)
meses_nomes = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']

# Criando um padrão de temperatura (Sazonalidade: Quente -> Frio -> Quente)
temp = 26 + 8 * np.cos(2 * np.pi * (dias - 20) / 365) + np.random.normal(0, 1.5, 365)
chuva = np.random.gamma(2, 5, 365)
chuva[chuva < 7] = 0 

df = pd.DataFrame({'Dia': dias, 'Temp': temp, 'Chuva': chuva})
df['Media_Movel'] = df['Temp'].rolling(window=30).mean() # Média Mensal

# 2. Configurando o Visual Profissional
plt.figure(figsize=(12, 6))

# Área de Chuva (Azul)
plt.fill_between(df['Dia'], df['Chuva'], color='deepskyblue', alpha=0.3, label='Chuva (mm)')

# Temperatura Diária (Linha fina)
plt.plot(df['Dia'], df['Temp'], color='salmon', alpha=0.4, linewidth=1, label='Temp. Diária (°C)')

# Tendência Mensal (Linha Forte)
plt.plot(df['Dia'], df['Media_Movel'], color='red', linewidth=3, label='Tendência (Média 30 dias)')

# 3. Ajustando os Meses no Eixo X
plt.xticks(np.linspace(0, 365, 12), meses_nomes)

plt.title('Dashboard Anual: Análise de Sazonalidade Climática', fontsize=14)
plt.ylabel('Escala de Medição')
plt.legend(loc='upper right')

# 4. Salvando com Alta Qualidade
plt.savefig('dashboard_anual.png', dpi=300)
print("✅ Sucesso! Dashboard de 1 ano gerado: dashboard_anual.png")
