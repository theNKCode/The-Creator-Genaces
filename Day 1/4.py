import os
ip = input("Press 1: to start notepad\nPress 2: to start chrome or firefox\nPress 3: to start vlc player or any other player\nPress 4: if ask input which url to open in browser, and when we give url, it open that website in browser\n")

if int(ip) ==1:
    os.system("notepad")
elif int(ip)==2:
    os.system("start firefox")
elif int(ip)==3:
    os.system("start vlc")
elif int(ip)==4:
    url = input("Enter the URL to open: ")
    os.system(f"start {url}")
