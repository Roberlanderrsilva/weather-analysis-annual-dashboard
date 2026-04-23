# 🌦️ D # Weather Data Pipeline & Analytics Framework 🌦️

## 📌 Visão Geral
Este projeto simula um pipeline de dados climáticos para análise de sazonalidade e risco ambiental. Ele foi desenvolvido sob princípios de **Engenharia de Software**, focando em escalabilidade, modularidade e governança de dados.

## ⚖️ Conformidade e LGPD (Data Privacy)
Embora este projeto utilize dados sintéticos (simulados), ele foi estruturado seguindo as diretrizes da **LGPD (Lei Geral de Proteção de Dados)**:
- **Anonimização:** Não há coleta de dados de usuários finais ou PII (Personally Identifiable Information).
- **Finalidade:** Os dados processados destinam-se exclusivamente a estudos estatísticos climáticos.
- **Transparência:** O processamento é realizado localmente (On-premise/Edge computing) sem vazamento para nuvens de terceiros não autorizadas.

## 🛠️ Arquitetura e Engenharia
- **Ambiente:** Lubuntu Linux (Kernel otimizado com swap memory em SSD para gestão de processos).
- **Linguagem:** Python 3.12+
- **Bibliotecas Core:** - `Pandas`: Estruturação de DataFrames.
  - `Matplotlib`: Visualização técnica com médias móveis (window=30).
  - `Numpy`: Simulação estocástica de variações climáticas.

## 📊 Governança de Dados
O sistema implementa uma análise de **12 meses**, permitindo a identificação de anomalias térmicas e picos de precipitação, essenciais para tomada de decisão em setores como Logística e GRC (Governança, Riscos e Conformidade).

---
*Mantido por: Roberlande Silva*
