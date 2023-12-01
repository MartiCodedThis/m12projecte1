import smtplib, ssl
from email.message import EmailMessage
from email.utils import formataddr

class MailManager:

    def init_app(self, app):
        # agafo els paràmetres de configuració
        self.sender_name = "Wannapop"
        self.sender_addr = "2daw.equip06@fp.insjoaquimmir.cat"
        self.sender_password = "uttVEcUemINNCX47"
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587

        print(f"self.sender_addr: {self.sender_addr}")
        print(f"self.sender_password: {self.sender_password}")
        print(f"self.smtp_server: {self.smtp_server}")
        print(f"self.smtp_port: {self.smtp_port}")

        # MAIL_SENDER_NAME="Wannapop"
        # MAIL_SENDER_ADDR="2daw.equip06@fp.insjoaquimmir.cat"
        # MAIL_SENDER_PASSWORD="uttVEcUemINNCX47"
        # MAIL_SMTP_SERVER="smtp.gmail.com"
        # MAIL_SMTP_PORT=587
        # CONTACT_ADDR="2daw.equip06@fp.insjoaquimmir.cat"
        # EXTERNAL_URL="http://127.0.0.1:5000"

        # els missatges de contacte s'envien a aquesta adreça
        self.contact_addr = app.config.get('CONTACT_ADDR')

        # URL del servidor web
        self.external_url = app.config.get('EXTERNAL_URL')

    # https://realpython.com/python-send-email/#option-2-using-starttls
    def send_contact_msg(self, msg):

        subject = "Missatge de contacte"
        content = f"""Missatge de contacte rebut:
        
        {msg}
        """

        self.__send_mail(
            dst_name = "Receptor/a de contacte",
            dst_addr = self.contact_addr,
            subject = subject,
            content = content
        )

    # https://realpython.com/python-send-email/#option-2-using-starttls
    def __send_mail(self, dst_name, dst_addr, subject, content):
        context = ssl.create_default_context()
        try:

            msg = EmailMessage()
            msg['From'] = formataddr((self.sender_name, self.sender_addr))
            msg['To'] = formataddr((dst_name, dst_addr))
            msg['Subject'] = subject
            msg.set_content(content)
            
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls(context=context)
                server.login(self.sender_addr, self.sender_password)
                server.sendmail(self.sender_addr, self.contact_addr, msg)

                print("Login done!")

                server.send_message(msg, from_addr=self.sender_addr, to_addrs=dst_addr)
        except smtplib.SMTPConnectError as e:
            print(f"SMTP connection error: {e}")
        except smtplib.SMTPServerDisconnected as e:
            print(f"SMTP server disconnected: {e}")
        except smtplib.SMTPException as e:
            print(f"SMTP error occurred: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")