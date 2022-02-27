#vishnukantmule@gmail.com
import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("20104138.avinashandhale@gmail.com", "bbruwivjwtxqeozr")

message = " Avinash Clinic 24/7 Management Dear Sir/ma'am, YOUR APPOINTMENT HAS BEEN BOOKED "


s.sendmail("20104138.avinashandhale@gmail.com", "20104109jeminbhanushali@gmail.com", message,)
s.quit()

