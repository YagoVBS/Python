import pyautogui
import time
import pandas as pd


# Espera inicial para permitir abrir o programa
time.sleep(5)
pyautogui.press('win')
time.sleep(0.2)
pyautogui.write("thunderbird")
time.sleep(0.5)
pyautogui.press('enter')

# Carrega a lista de emails e contratos do arquivo CSV

lista = pd.read_csv('C:/Users/Usuário/Desktop/Envios de Boletos por Email/Mensal.Agosto2024.csv')

for linha in lista.index:
    contrato = lista.loc[linha, "Contrato"]
    nome = lista.loc[linha, "Nome"]
    email = lista.loc[linha, "Email"]
    email2 = lista.loc[linha, "Email2"]
    email3 = lista.loc[linha, "Email3"]
    
    # Abertura de nova mensagem no Thunderbird
    time.sleep(10)
    pyautogui.hotkey('ctrl', 'n')
    time.sleep(2)
    
    # Preenchimento dos campos de email
    pyautogui.write("cob1@memorialjardim.com.br")
    time.sleep(0.2)
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.write("cob2@memorialjardim.com.br")
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(0.5)
    
    if email: 
        pyautogui.write(str(email))
        time.sleep(0.5)
        pyautogui.press('enter')
        time.sleep(1)
    
    if pd.notna(email2):  
        pyautogui.write(str(email2))
        time.sleep(0.5)
        pyautogui.press('enter')
        time.sleep(1)
    
    if pd.notna(email3): 
        pyautogui.write(str(email3))
        time.sleep(0.5)
        pyautogui.press('enter')
        time.sleep(1)
    
    # Preenchimento do campo de assunto e corpo do email
    pyautogui.press('tab')
    time.sleep(1)    
    pyautogui.write(f"BOLETO MENSAL - CEMITERIO MEMORIAL JARDIM SANTO ANDRE : {contrato}")
    pyautogui.press('enter')
    pyautogui.write("Segue em anexo o boleto Mensal.\n")
    pyautogui.write("\n")
    pyautogui.write("Mensagem Automatica.\n")
    pyautogui.write("\n")
    pyautogui.write("Atenciosamente,\n")
    
    # Verificar e anexar arquivo
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'shift', 'a')
    time.sleep(1)
    pyautogui.write(nome)
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)  
    
    try:
        if pyautogui.locateOnScreen('C:/Users/Usuário/Desktop/Envios de Boletos por Email/Erro1.png'):
            pyautogui.press('enter')  # Fechar a mensagem de erro
            time.sleep(1)
            pyautogui.hotkey('alt', 'f4')
            time.sleep(0.5)
            pyautogui.hotkey('alt', 'f4')
            time.sleep(0.5)
            pyautogui.press('enter')
            time.sleep(1)
    except pyautogui.ImageNotFoundException:
        pass
        
    
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'enter')   
    

    
 

    
