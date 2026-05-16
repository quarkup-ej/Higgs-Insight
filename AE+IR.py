import pandas as pd

# Loja Uranum Brasil (shopee) e dados fictícios para produtos de IA (sensores)
dados_df = pd.DataFrame({
    'Categoria' : ['Astronomia', 'Astronomia', 'Astronomia', 'Astronomia', 'Astronomia', 'IA', 'IA', 'IA', 'IA'],
    'Produtos' : ['Telescópio Refrator 80/500 mm Leo-2', 'Telescópio Refrator 70/700 mm', 'Telescópio Refrator 90/700 mm Tauro-2', 
                'Telescópio Refletor Newtoniano 114/900 mm', 'Telescópio Refletor Newtoniano 130/650 mm', 'Sensor DHT11',
                'Sensor PIR HC-SR501', 'Módulo Câmera OV7670 para Arduino', 'Sensor Ultrassônico HC-SR04'],
    'Precos (R$)' : [1104.00, 1117.80, 1490.40, 1674.40, 2292.64,
                    10.90, 14.90, 38.50, 19.90],
    
    'Vendas' : [29, 48, 31, 6, 10,
                52, 45, 18, 37]
})

dados_df['Total (R$)'] = dados_df['Precos (R$)'] * dados_df['Vendas']

print('--- PRODUTOS ---')
print(dados_df.to_string(index=False))

print('\n--- RESUMO POR CATEGORIA ---')
resumo = dados_df.groupby('Categoria').agg(
    Media_Preco  = ('Precos (R$)', 'mean'),
    Total_Vendas = ('Vendas',      'sum'),
    Total_RS     = ('Total (R$)',  'sum')
)
print(resumo.to_string())

print('\n--- TOTAL GERAL ---')
print(f" Vendas totais : {dados_df['Vendas'].sum()} unidades")
print(f" Receita total : R$ {dados_df['Total (R$)'].sum():,.2f}")