import yfinance as yf
import matplotlib.pyplot as plt

# Defina o símbolo da ação que você deseja analisar
symbol = 'AAPL'  # Exemplo: Apple Inc.

# Obtenha os dados históricos da ação
stock_data = yf.download(symbol, start='2024-03-01', end='2024-03-31')  # Período de um mês

# Exiba as primeiras linhas dos dados
print(stock_data.head())

# Plotar o gráfico de linha dos preços de fechamento ao longo do tempo
plt.figure(figsize=(14, 8))

# Adicionar os retângulos (cards) no topo da interface
plt.text(0.1, 0.95, f'Média do preço de fechamento: {stock_data["Close"].mean():.2f}', transform=plt.gcf().transFigure, size=12, color='black', bbox=dict(facecolor='lightgray', alpha=0.5))
plt.text(0.4, 0.95, f'Máximo preço máximo: {stock_data["Close"].max():.2f}', transform=plt.gcf().transFigure, size=12, color='black', bbox=dict(facecolor='lightgray', alpha=0.5))
plt.text(0.7, 0.95, f'Mínimo preço mínimo: {stock_data["Close"].min():.2f}', transform=plt.gcf().transFigure, size=12, color='black', bbox=dict(facecolor='lightgray', alpha=0.5))

# Gráfico de linha
plt.subplot(1, 2, 1)
plt.plot(stock_data.index, stock_data['Close'], marker='o', linestyle='-')
plt.title('Preços de Fechamento de ' + symbol)
plt.xlabel('Data')
plt.ylabel('Preço de Fechamento')
plt.xticks(rotation=45)  # Girar os rótulos do eixo x em 45 graus para melhor legibilidade
plt.grid(True)

# Adicionar rótulos aos pontos
for i, price in enumerate(stock_data['Close']):
    plt.annotate(f'{price:.2f}', (stock_data.index[i], price), textcoords="offset points", xytext=(0, 10), ha='center')

# Gráfico de barras para o volume de negociação
plt.subplot(1, 2, 2)
plt.bar(stock_data.index, stock_data['Volume'], color='blue')
plt.title('Volume de Negociação de ' + symbol)
plt.xlabel('Data')
plt.ylabel('Volume')
plt.xticks(rotation=45)  # Girar os rótulos do eixo x em 45 graus para melhor legibilidade
plt.grid(True)

plt.tight_layout()
plt.show()
