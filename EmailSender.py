#vishnukantmule@gmail.com
import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("vishnukantmule@gmail.com", "cgezqyarhsxghdfy")

message = "YOU APPOINTMENT HAS BEEN BOOK "


s.sendmail("vishnukant@gmail.com", "20104109jeminbhanushali@gmail.com", message,)
s.quit()

