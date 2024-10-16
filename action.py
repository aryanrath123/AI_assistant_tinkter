import datetime
import speak
import webbrowser
import weather
import os
import re
import math
import subprocess


def Action(send):
    if send is None:
        return "I didn't catch that. Could you please repeat?"

    data_btn = send.lower()

    # Greeting & Introduction
    if "what is your name" in data_btn:
        speak.speak("My name is Virtual Assistant, your personal AI.")
        return "My name is Virtual Assistant, your personal AI."

    elif "hello" in data_btn or "hi" in data_btn:
        speak.speak("Hello! How can I assist you today?")
        return "Hello! How can I assist you today?"

    elif "how are you" in data_btn:
        speak.speak("I'm doing well! Thank you for asking. How can I help you?")
        return "I'm doing well! Thank you for asking. How can I help you?"

    elif "thank you" in data_btn or "thanks" in data_btn:
        speak.speak("You're very welcome!")
        return "You're very welcome!"

    elif "good morning" in data_btn:
        speak.speak("Good morning! How can I assist you today?")
        return "Good morning! How can I assist you today?"

    # Time Query
    elif "time now" in data_btn or "what time" in data_btn:
        current_time = datetime.datetime.now()
        Time = f"It is {current_time.hour} Hour and {current_time.minute} Minute."
        speak.speak(Time)
        return Time

    # System Shutdown or Quit
    elif "shutdown" in data_btn or "quit" in data_btn:
        speak.speak("Shutting down. Have a great day!")
        return "Shutting down. Have a great day!"

    # Play Music Online or Locally
    elif "play music" in data_btn or "song" in data_btn:
        webbrowser.open("https://gaana.com/")
        speak.speak("Gaana.com is now ready for you. Enjoy your music!")
        return "Gaana.com is now ready for you. Enjoy your music!"

    elif "music from my laptop" in data_btn:
        url = 'D:\\music'
        songs = os.listdir(url)
        os.startfile(os.path.join(url, songs[0]))
        speak.speak("Playing songs from your library.")
        return "Playing songs from your library."

    # Open Websites and Software
    elif 'open google' in data_btn or 'google' in data_btn:
        webbrowser.open("https://google.com/")
        speak.speak("Opening Google.")
        return "Google is open."

    elif 'open youtube' in data_btn or 'youtube' in data_btn:
        webbrowser.open("https://youtube.com/")
        speak.speak("Opening YouTube.")
        return "YouTube is open."

    elif 'open notepad' in data_btn:
        subprocess.Popen('notepad.exe')
        speak.speak("Opening Notepad.")
        return "Notepad is open."

    elif 'open calculator' in data_btn:
        subprocess.Popen('calc.exe')
        speak.speak("Opening Calculator.")
        return "Calculator is open."

    # Weather Query
    elif 'weather' in data_btn:
        ans = weather.Weather()
        speak.speak(ans)
        return ans

    # Improved Arithmetic Calculations
    elif re.search(r'(\d+)\s*[+]\s*(\d+)', data_btn):
        nums = re.findall(r'(\d+)', data_btn)
        if len(nums) == 2:
            result = int(nums[0]) + int(nums[1])
            response = f"The result is {result}."
            speak.speak(response)
            return response

    elif re.search(r'(\d+)\s*[*]\s*(\d+)', data_btn):
        nums = re.findall(r'(\d+)', data_btn)
        if len(nums) == 2:
            result = int(nums[0]) * int(nums[1])
            response = f"The result is {result}."
            speak.speak(response)
            return response

    elif re.search(r'what is the sum of (\d+) and (\d+)', data_btn):
        nums = re.findall(r'\d+', data_btn)
        if len(nums) == 2:
            result = int(nums[0]) + int(nums[1])
            response = f"The result is {result}."
            speak.speak(response)
            return response

    elif re.search(r'what is the value of (\d+) and addition (\d+)', data_btn):
        nums = re.findall(r'\d+', data_btn)
        if len(nums) == 2:
            result = int(nums[0]) + int(nums[1])
            response = f"The result is {result}."
            speak.speak(response)
            return response

    # Open Applications
    elif 'open whatsapp' in data_btn or 'launch whatsapp' in data_btn:
        webbrowser.open("https://web.whatsapp.com/")
        speak.speak("Opening WhatsApp.")
        return "WhatsApp is open."

    elif 'open a new tab' in data_btn or 'open new tab' in data_btn:
        webbrowser.open_new_tab("https://google.com")  # Adjust this to your desired URL
        speak.speak("Opening a new tab.")
        return "A new tab is open."

    # Fallback Response
    else:
        speak.speak("I'm able to understand! How else can I assist you?")
        return "I'm able to understand! How else can I assist you?"
