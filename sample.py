import smtplib

server = smtplib.SMTP("smtp.gmail.com", 587)
server.ehlo()
server.starttls()  # No extra arguments here!
server.login("sumanthgm12345@gmail.com", "dvli dhub goow djds")

server.sendmail(
    "214g1a32a4@srit.ac.in@gmail.com",
    "gmsumanth93917@gmail.com",
    "Subject: Test\n\nThis is a test email."
)

server.quit()
print("Email sent successfully!")