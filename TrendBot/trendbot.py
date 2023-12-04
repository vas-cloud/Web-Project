import datetime
from bardapi import BardCookies
from tkinter import *

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"
FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"  




def _on_enter_pressed():
        global msg
        msg = msg_entry.get()
        _insert_message(msg, "You")

def main():
    cookie_dict = {
    "__Secure-1PSID": "cwgAH0UelQ67hFZU97f784UgndgZrpC_17Ln8uxBxil4W3orgrjNbRsBKz6C019Zr2csvA.",
    "__Secure-1PSIDTS": "sidts-CjEBNiGH7hq-dcVgm2jI_7FQQc4a7KVmEZSxZYfsuRWAsP0GQLpOTcXarN42EmlD6RC1EAA",
    "__Secure-1PSIDCC": "ACA-OxMZbSjSrrVcF8GGH09C_ZbWuidOrLgEMgba3w9u_KO7qbcV8DmNbZohuu2cqHOXw0XhBw"}

    bard = BardCookies(cookie_dict = cookie_dict)

    while True:
        global reply
        query = msg
        reply = bard.get_answer(query)['content']
        print(reply)
        break
    return reply

def _insert_message(msg, sender):
        if not msg:
            return
        
        elif msg == "quit":
            root.destroy()
             

        msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        text_widget.configure(state=NORMAL)
        text_widget.insert(END, msg1)
        text_widget.configure(state=DISABLED)
        print(msg1,msg)

        reply = main()
        msg_entry.delete(0, END)
        msg2 = f"TrendBot: {reply}\n\n"
        text_widget.configure(state=NORMAL)
        text_widget.insert(END, msg2)
        text_widget.configure(state=DISABLED,fg="white")

        text_widget.see(END)
        

root = Tk()
root.title("TrendBot...")
root.geometry('880x500')

head_label = Label(root, bg=BG_COLOR, fg=TEXT_COLOR,
                           text="Welcome", font=FONT_BOLD, pady=10)
head_label.place(relwidth=1)
        
        # tiny divider
line = Label(root, width=450, bg=BG_GRAY)
line.place(relwidth=1, rely=0.07, relheight=0.012)


text_widget = Text(root, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR,
                                font=FONT, padx=5, pady=5)
text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
text_widget.configure(cursor="arrow", state=DISABLED)

        # scroll bar
scrollbar = Scrollbar(root)
scrollbar.place(relheight=1, relx=0.974)
scrollbar.configure(command=text_widget.yview)
        
        # bottom label
bottom_label = Label(root, bg=BG_GRAY, height=80)
bottom_label.place(relwidth=1, rely=0.825)

# message entry box
msg_entry = Entry(bottom_label, bg="#2C3E50", fg=TEXT_COLOR, font=FONT)
msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
msg_entry.focus()
msg_entry.bind()
        
        # send button
send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg=BG_GRAY,command=lambda:[_on_enter_pressed(), main()])
send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)


root.mainloop()



