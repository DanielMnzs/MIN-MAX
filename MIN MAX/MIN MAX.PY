import pyautogui
import pandas as pd 
import PIL  
import time


caminho_arquivo = r"//depo0903/gpa$/PAC/Daniel Menezes/Python/MIN MAX/MIN MAX.xlsx"
ler = pd.read_excel(caminho_arquivo)
tabela = pd.DataFrame(ler)
print(tabela)

x = 0 
y = 0 

while True and x < len (tabela):
    plu = tabela.iloc[x, y]
    min = "{:.0f}".format(tabela.iloc[x, y + 1])
    max = "{:.0f}".format(tabela.iloc[ x , y + 2])
    print(min)
    print(max)
    print(plu)
    pyautogui.doubleClick(236, 192)
    time.sleep(1)
    pyautogui.write(str(plu),interval=0.111)
    time.sleep(1)
    pyautogui.leftClick(1085, 192)
    time.sleep(3)
    pyautogui.leftClick(33, 292)
    time.sleep(0.5)
    pyautogui.leftClick(1112, 700)
    time.sleep(2)
    pyautogui.leftClick(1149, 440)
    time.sleep(1)
    pyautogui.scroll(-600)
    time.sleep(0.5)
    pyautogui.doubleClick(653, 574)
    pyautogui.write(str(min),interval=0.111)
    for i in range (4):
        pyautogui.hotkey("tab")
    pyautogui.write(str(max),interval=0.111)
    for i in range(3):
        pyautogui.hotkey("tab")
    pyautogui.write(str(min),interval=0.111)
    time.sleep(1)
    pyautogui.leftClick(896, 697)
    time.sleep(3)
    pyautogui.leftClick(21, 145)
    time.sleep(3)
    pyautogui.press("enter")
    time.sleep(1)
    x = x + 1
    

