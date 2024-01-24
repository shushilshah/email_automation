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
        voice = listener.listen(source)
        data = listener.recognize_google(voice)
        print(data)
        return data.lower()


# list of email of receiver
dict = {"username": "email of receiver"}


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
    receiver = dict[name]
    system("subject of email")
    subject = mic()
    system("body of email")
    body = mic()
    send_email(receiver, subject, body)
    mic("The email has been successfully sent.")


main()
