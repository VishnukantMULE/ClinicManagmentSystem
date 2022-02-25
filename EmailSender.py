#vishnukantmule@gmail.com
import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("vishnukantmule@gmail.com", "cgezqyarhsxghdfy")

message = "Hello User APPOINTMENT BOOKED"


s.sendmail("vishnukant@gmail.com", "akshaymule970@gmail.com", message,)
s.quit()
