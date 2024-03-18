import pyautogui
from time import sleep

# 1 - Clicar e digitar usuário
pyautogui.click(995,539, duration=0.5)
pyautogui.write('gabriellol88')
# 2 - Clicar e digitar senha
pyautogui.click(995,576, duration=0.5)
pyautogui.write('gabriellol8')
# 3 - Clicar em "Entrar"
pyautogui.click(848,610,duration=0.5)
# 4 - Extrair cada produto
with open('produtos.txt','r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]
#       4.1 - clicar e digitar produto 
        pyautogui.click(624,526,duration=0.5)
        pyautogui.write(produto)
#       4.2 - clicar e digitar quantidade
        pyautogui.click(627,558,duration=0.5)
        pyautogui.write(quantidade)
#       4.3 - clicar e digitar preço
        pyautogui.click(630,595,duration=0.5)
        pyautogui.write(preco)
#       4.4 - clicar em registrar
        pyautogui.click(502,788,duration=0.5)