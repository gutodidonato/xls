with open("read.txt") as arquivo_email:
    gmail = 0
    yahoo = 0
    outlook = 0
    hotmail = 0
    linhas = arquivo_email.readlines()
    for indice, linha in enumerate(linhas):
        if "@gmail" in linha:
            gmail += 1
        elif "@hotmail" in linha:
            hotmail += 1
        elif "@yahoo" in linha:
            yahoo += 1
        elif "@outlook" in linha:
            outlook += 1
    print(f"Temos emails no google: {gmail}")
    print(f"Temos emails no hotmail: {hotmail}")
    print(f"Temos emails no yahoo: {yahoo}")
    print(f"Temos emails no outlook: {outlook}")

with open("email_para_pegar.txt", "w") as arquivo_emails_plotados:
    print("Arquivo Criado!")
    

        
    