import smtplib
import email.message

'''Função que envia email com base na string "aviso" recebida 
'''
def mandaEmail(aviso):

    arq = open("loginEmail.txt") #abre o arquivo onde está com informações de login como email e senha
    log = arq.readlines() #coloca essas informações na variável log

    msg = email.message.Message() #coisa da biblioteca email.message não se preocupar
    msg['Subject'] = "Bom Dia" #Assunto do Email
    msg['From'] = log[0] #para quem vai o email
    msg['To'] = log[1] #quem vai enviar (seu email)
    pwd = log[2] #senha do seu gmail
    message = str(f"""
    <p>{aviso}</p>
    """) # sera o texto que vai ser enviado por email de acordo com o conteúdo da variavel aviso
    # se vcs nunca viram isso, se chama f expressão depois pesquisem

    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(message) # mais coisas da biblioteca

    try: # Nesse bloco de codigo o script vai tentar enviar o email, se nao coseguir ele vai printar na tela a mensagem "Deu Ruim!!"
    
    	# Voces nao necessessariamente precisam utilizar o try, é mais uma convenção
    	
        s = smtplib.SMTP('smtp.gmail.com: 587') #coisas da biblioteca smtplib
        s.starttls()
        s.login(msg['From'],pwd)
        s.sendmail(msg['From'],[msg['To']],msg.as_string().encode('utf-8'))

    except:
        print(f"Deu Ruim!!")
    else: 
        print(f"Mandado com sucesso!!")
        

