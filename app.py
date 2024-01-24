import smtplib
import pyttsx3
import speech_recognition as sr
from email.message import EmailMessage

# initializing the text to speech engine
listener = sr.Recognizer()
ts = pyttsx3.Engine()

# speaking the content of email


def system(text):
    ts.say(text)
    ts.runAndWait()

# mic function


def mic():
    with sr.Microphone() as source:
        print("listening.......")
        try:
            voice = listener.listen(source, timeout=5)
            data = listener.recognize_google(voice)
            print(data)
            return data.lower()
        except sr.UnknownValueError:
            print("can not understand the sound.")
            return ""


# list of email of receiver
email_dict = {"username": "email of receiver"}


def send_email(receiver, subject, body):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("email of sender", "your email generated app token")
    email = EmailMessage()
    email['From'] = "sender email"
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(body)
    server.send_message(email)


def main():
    system("To whom the email sent")
    name = mic()

    if name in email_dict:
        receiver = email_dict[name]
        system("subject of email")
        subject = mic()
        system("Body of email")
        body = mic()

        if subject and body:
            send_email(receiver, subject, body)
            system("Your email has been successfully sent.")
        else:
            system('Email subject or body is empty. Please try again.')
    else:
        system("Recipient email not found in the database. Please provide valid email.")


if __name__ == "__main__":
    main()
