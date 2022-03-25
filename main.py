import os
import sys
msg=' '.join(sys.argv[1:(len(sys.argv))])
import webbrowser

url='https://api.whatsapp.com/send?phone=91XXXXXXXXXX&text='+msg
webbrowser.register('edge',
    None,
    webbrowser.BackgroundBrowser("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"))
webbrowser.get('edge').open(url)
import keyboard as k
import time
time.sleep(10)
k.press_and_release('enter')