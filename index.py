import json
import smtplib
from email.message import EmailMessage
def main():
    with open('relatorio.txt', 'r') as file:
        conteudo = file.read()


    def cifradecesar(texto):
        resultado = ''
        for letra in texto:
            resultado += chr((ord(letra) - 97 + 13) % 26 + 97)
        return resultado

    criptografado = cifradecesar(conteudo)
    
    def mail(criptografado):
        
        SMTP_SERVER = 'smtp.gmail.com'
        SMTP_PORT = 587

        with open("settings_pessoal.json", encoding='utf-8') as meu_json: # Importar dados de um arquivo com email e password app
            dados = json.load(meu_json)
            email = dados["email"]
            print(dados)
            senha = dados["password"]
            print('Dados do settings_pessoal.json lidos com sucesso!')
        # Credenciais de login  (Adiciona um arquivo JSON com o nome settings_pessoal.json)


        EMAIL_ADDRESS = email
        EMAIL_PASSWORD = senha

        # Criar a mensagem do email
        msg = EmailMessage()
        msg['Subject'] = 'Assunto do Email'
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = 'destinatario@example.com'
        msg.set_content(criptografado)

        # Enviar o email
        try:
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()  
                server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)  
                server.send_message(msg)  #

            print('Email enviado com sucesso!')
        except Exception as e:
            print(f'Ocorreu um erro ao enviar o email: {e}')


    mail(criptografado)
main()






    
