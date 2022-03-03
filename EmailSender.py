#vishnukantmule@gmail.com
import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("vishnukantmule@gmail.com", "cgezqyarhsxghdfy")

message = " Avinash Clinic 24/7 Management Dear Sir/ma'am, YOUR APPOINTMENT HAS BEEN BOOKED "


s.sendmail("20104138.avinashandhale@gmail.com", "akshaymule970@gmail.com", message,)
s.quit()

