import os
import smtplib
from email.message import EmailMessage
def EmailEnviator(emailUser,num):
  try:
   email = 'o.vinicius@estudante.ifro.edu.br'
   senha = 'trocarsenha'

   msg = EmailMessage()
   msg['Subject'] = 'Olá aqui esta seu numero de troca de senha'
   msg['From'] = 'o.vinicius@estudante.ifro.edu.br'
   msg['To'] = emailUser
   msg.set_content(f'Olá aqui esta o seu codigo: {num}')

   with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
     smtp.login(email,senha)
     smtp.send_message(msg)
  except smtplib.SMTPRecipientsRefused as e :
    print("algo deu errado",e)
