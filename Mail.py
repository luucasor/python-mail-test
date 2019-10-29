import smtplib
from email.mime.text import MIMEText
from ConfigParser import ConfigParser

class Mail:

    config = 0

    def lerConfiguracao(self, nomeArquivo):
        print("Lendo configuracoes...")
        self.__class__.config = ConfigParser()
        self.__class__.config.read(nomeArquivo)

    def enviarEmail(self):
        smtp_host = self.__class__.config.get("MAIL", "host")
        smtp_port = self.__class__.config.get("MAIL", "port")
        username = self.__class__.config.get("MAIL", "username")
        password = self.__class__.config.get("MAIL", "password")
        receiver = self.__class__.config.get("MAIL", "receiver")
        sender = self.__class__.config.get("MAIL", "sender")
        subject = self.__class__.config.get("MAIL", "subject")
        ssl = self.__class__.config.getboolean("MAIL", "ssl")
        msg = self.__class__.config.get("MAIL", "message")

        message = MIMEText(msg)
        message['subject'] = subject
        message['from'] = sender
        message['to'] = receiver

        print "Enviando e-mail..."
        if ssl:
            server = smtplib.SMTP_SSL(smtp_host, smtp_port)
            server.login(username, password)
        else:
            server = smtplib.SMTP(smtp_host, smtp_port)
        
        try: 
            server.sendmail(sender, receiver, message.as_string())    
            print "E-mail enviado com sucesso!"
        except smtplib.SMTPException as e:
            print "Erro: "+str(e)
        finally: 
            server.quit()


mail = Mail()
mail.lerConfiguracao('mail.conf')
mail.enviarEmail()