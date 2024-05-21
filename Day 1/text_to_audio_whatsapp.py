# import pywhatkit as pwk
# import time

# t = time.localtime()
# current_hr = int(time.strftime("%H", t))
# current_min = int(time.strftime("%M", t))
# print(current_hr, current_min)
# pwk.sendwhatmsg("+91930910144", "Hey Bro Whataup", current_hr, current_min, 10)

import pywhatkit as pwk
import time
import pyttsx3

# Get the current time
t = time.localtime()
current_hr = int(time.strftime("%H", t))
current_min = int(time.strftime("%M", t))

# Add 1 minute to the current time
if current_min == 59:
    current_min = 0
    current_hr = (current_hr + 1) % 24
else:
    current_min += 1

text = input("Enter the message: ")
# # engine = pyttsx3.init()

# # convert this text to speech
# engine.say(text)
# # play the speech
# engine.runAndWait()
# engine.save_to_file(text, "msg.mp3")
# engine.runAndWait()
# # Send the WhatsApp message
pwk.sendwhatmsg("+919309101444",text, current_hr, current_min, 20)


# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get("https://web.whatsapp.com/")
# name = input("Enter the name of user or group: ")
# msg = filepath("Enter your filepath (audio/images): ")

# input('Enter anything after scanning QR code' )
# user = driver. fiand_element_by_xpath( '//span [@title = "{}"]'.format(name))
# user.click()

# attachment box = driver.find_element_by_xpath('//div[@title ="Attach"]')


# import pyautogui as pag
# import time
# import webbrowser
# import pyperclip
# from gtts import gTTS

# def text_to_audio(text, filename="output.mp3"):
#     tts = gTTS(text=text, lang='en')
#     tts.save(filename)
#     return filename

# def send_audio_via_whatsapp(phone_number, audio_path):
#     webbrowser.open(f"https://web.whatsapp.com/send?phone={phone_number}")
#     time.sleep(20) 

#     #Plus icon
#     pag.click(x=425, y=639)
#     time.sleep(2)

#     # Document
#     pag.click(x=790, y=626)
#     time.sleep(2)

#     # Type the audio file path
#     pyperclip.copy(audio_path)
#     pag.hotkey("ctrl", "v")
#     time.sleep(2)

#     # Press 'Enter' to upload the file
#     pag.press('enter')
#     time.sleep(2)

#     # Click the send button (you might need to adjust coordinates)
#     pag.click(x=1863, y=943)
#     time.sleep(2)

# # Example usage
# text = input("Enter the message: ")
# audio_path = text_to_audio(text)
# phone_number = "9309101444"
# send_audio_via_whatsapp(phone_number, audio_path)



# import gtts  
# from playsound import playsound 
# text = input("Enter the text: ")
# t1 = gtts.gTTS(text) 
# t1.save("welcome.mp3")
# playsound("welcome.mp3")