import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def enviar_email(destinatario, assunto, mensagem):
    # Configurações do servidor de e-mail SMTP
    servidor_smtp = 'smtp.seuemail.com'
    porta_smtp = 587
    remetente = 'seuemail@seuemail.com'
    senha = 'suasenha'

    # Crie um objeto MIMEText para o corpo do e-mail
    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = assunto
    msg.attach(MIMEText(mensagem, 'plain'))

    # Inicie a conexão SMTP
    try:
        servidor = smtplib.SMTP(servidor_smtp, porta_smtp)
        servidor.starttls()
        servidor.login(remetente, senha)

        # Envie o e-mail
        servidor.sendmail(remetente, destinatario, msg.as_string())
        print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {str(e)}")
    finally:
        servidor.quit()

# Exemplo de uso:
destinatario = 'destinatario@email.com'
assunto = 'Assunto do e-mail'
mensagem = 'Corpo do e-mail'
enviar_email(destinatario, assunto, mensagem)