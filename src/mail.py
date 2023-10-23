import smtplib
from email.message import EmailMessage


class SMTPEmailer:
    def __init__(
        self,
        *,
        host: str,
        port: int,
        user: str,
        password: str,
    ):
        self.host = host
        self.port = port
        self.user = user
        self.password = password

    def send_email(
        self,
        subject: str,
        body: str,
        to_email: str,
    ) -> None:
        """
        Send an email using the given SMTP server.

        :param subject: The subject of the email.
        :param body: The body of the email.
        :param to_email: The recipient of the email.

        :return: None
        """

        msg = EmailMessage()
        msg.set_content(body)
        msg["Subject"] = subject
        msg["From"] = self.user
        msg["To"] = to_email

        with smtplib.SMTP(self.host, self.port) as server:
            server.starttls()
            server.login(self.user, self.password)
            server.send_message(msg)
