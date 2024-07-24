## Power Up - Automação de Cadastro de Produtos em um Site

# Importação das bibliotecas
import pandas as pd
import pyautogui  # biblioteca possibilita o controle do mouse
import time  # medidas de tempo

# Importação da base de dados
df_raw = pd.read_csv('produtos.csv')
print(df_raw)

# Tempo de espera entre os comandos
pyautogui.PAUSE = 0.5

# Abrir sistema
pyautogui.press('win')
pyautogui.write('edge')
pyautogui.press('enter')
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

# Esperar o site carregar
time.sleep(5)

# Login no sistema
pyautogui.click(x=981, y=314)
pyautogui.write('pietragaio@hotmail.com')
pyautogui.press('tab')
pyautogui.write('124578')
pyautogui.click(x=1005, y=447)
pyautogui.click(x=993, y=273)  

# Cadastro de produtos automatizando para percorrer linha a linha
for linha in df_raw.index:
    pyautogui.click(x=953, y=213)  # clica no 1º campo
    pyautogui.write(str(df_raw.loc[linha, 'codigo']))  # pega o código do dataframe e escreve no campo
    pyautogui.press('tab')
    pyautogui.write(str(df_raw.loc[linha, 'marca']))
    pyautogui.press('tab')
    pyautogui.write(str(df_raw.loc[linha, 'tipo']))
    pyautogui.press('tab')
    pyautogui.write(str(df_raw.loc[linha, 'categoria']))
    pyautogui.press('tab')
    pyautogui.write(str(df_raw.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')
    pyautogui.write(str(df_raw.loc[linha, 'custo']))
    pyautogui.press('tab')
    
    # Só preencher o campo de observação se houver observação
    if not pd.isna(df_raw.loc[linha, 'obs']):
        pyautogui.write(str(df_raw.loc[linha, 'obs']))

    pyautogui.press('enter')
    pyautogui.scroll(5000)
