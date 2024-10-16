from tkinter import *
from PIL import Image, ImageTk
import action
import spech_to_text

def User_send():
    send = entry1.get()
    if send.strip() == "":
        text.insert(END, "Me --> You haven't entered anything.\n")
        return
    bot = action.Action(send)
    text.insert(END, "Me --> " + send + "\n")
    if bot is not None:
        text.insert(END, "Bot <-- " + str(bot) + "\n")
    if bot == "ok sir":
        root.destroy()

def ask():
    ask_val = spech_to_text.spech_to_text()
    if ask_val.strip() == "":
        text.insert(END, "Me --> I didn't hear anything.\n")
        return
    bot_val = action.Action(ask_val)
    text.insert(END, "Me --> " + ask_val + "\n")
    if bot_val is not None:
        text.insert(END, "Bot <-- " + str(bot_val) + "\n")
    if bot_val == "ok sir":
        root.destroy()

def delete_text():
    text.delete("1.0", "end")

# Initialize Tkinter window
root = Tk()
root.geometry("600x750")  # Adjust size for more spacing
root.title("AI Assistant")
root.resizable(False, False)
root.config(bg="#f0f0f0")

# Main Frame
Main_frame = Frame(root, padx=20, pady=20, bg="#2a9d8f", bd=5, relief="groove")
Main_frame.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

# Text Label 
Text_label = Label(Main_frame, text="AI Assistant", font=("Helvetica", 18, "bold"), bg="#2a9d8f", fg="white")
Text_label.grid(row=0, column=0, padx=20, pady=10)

# Image 
Display_Image = None
try:
    Display_Image = ImageTk.PhotoImage(Image.open("image/assitant.png"))  # Ensure the path and filename are correct
    Image_Label = Label(Main_frame, image=Display_Image, bg="#2a9d8f")
    Image_Label.grid(row=1, column=0, pady=10)
except Exception as e:
    print("Error: Could not load image. Check the file path.")  # Print error message instead of using `text` before its definition

# Add a text widget inside a frame
text_frame = Frame(root)
text_frame.grid(row=1, column=0, padx=20, pady=10)
text = Text(text_frame, font=('Helvetica', 12), bg="#e9cfcf", wrap=WORD, height=8, width=45)  # Reduced height
text.grid(row=0, column=0)
scrollbar = Scrollbar(text_frame, command=text.yview)
scrollbar.grid(row=0, column=1, sticky='nsew')
text['yscrollcommand'] = scrollbar.set

# Add an entry widget below the text widget with padding
entry1 = Entry(root, justify=CENTER, font=('Helvetica', 12))
entry1.grid(row=2, column=0, padx=20, pady=(10, 20), sticky="ew")  # Added padding between entry and text

# Button Frame
button_frame = Frame(root)
button_frame.grid(row=3, column=0, pady=20)

# Add buttons with updated styles and better spacing
button1 = Button(button_frame, text="ASK", bg="#264653", fg="white", font=("Helvetica", 12, "bold"),
                 padx=40, pady=10, command=ask)
button1.grid(row=0, column=0, padx=10)

button2 = Button(button_frame, text="SEND", bg="#264653", fg="white", font=("Helvetica", 12, "bold"),
                 padx=40, pady=10, command=User_send)
button2.grid(row=0, column=1, padx=10)

button3 = Button(button_frame, text="DELETE", bg="#264653", fg="white", font=("Helvetica", 12, "bold"),
                 padx=40, pady=10, command=delete_text)
button3.grid(row=0, column=2, padx=10)

root.mainloop()
