# Задание 4
#
# Жду от вас письмо! (слайды 13-17). Воспользуйтесь менеджером контекста (with … as) (слайд 17)

import smtplib

with smtplib.SMTP('smtp.gmail.com', 587) as smtp_object:
    smtp_object.starttls()
    smtp_object.login('login','password')
    smtp_object.sendmail("from","to","message")