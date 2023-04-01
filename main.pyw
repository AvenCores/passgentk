from tkinter.messagebox import showerror
import customtkinter
import tkinter
import random


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


def selectitem(choice):
    frame = customtkinter.CTkTextbox(App, width=200, height=50, border_width=4)
    frame.place(x=200, y=80, anchor=tkinter.CENTER)
    print(choice)

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("400x200")
        self.title("Password generator")
        self.iconbitmap("pass.ico")
        self.resizable(False, False)

        self.frame = customtkinter.CTkTextbox(self, width=250, height=100, text_color="#33FF33", border_width=2)
        self.frame.place(x=200, y=60, anchor=tkinter.CENTER)

        self.combox = customtkinter.CTkOptionMenu(self, values=["5", "10", "15", "20", "25"], button_hover_color="#7A848D", button_color="#3c3f41", fg_color="#565B5E", width=100, height=30)
        self.combox.place(x=130, y=140, anchor=tkinter.CENTER)
        self.combox.set("Select")
        
        self.button = customtkinter.CTkButton(self, text="Generate", width=100, height=30, hover_color="#7A848D", fg_color="#565B5E", command=self.button_callback)
        self.button.place(x=270, y=140, anchor=tkinter.CENTER)

        self.clearbutton = customtkinter.CTkButton(self, text="🧹", width=25, height=25, command=self.cleartextbox)
        self.clearbutton.place(x=200, y=140, anchor=tkinter.CENTER)

        self.lampbutton = customtkinter.CTkOptionMenu(self, values=["Unpin", "Pin"], width=80, height=25, dynamic_resizing=False, command=self.togglecommand)
        self.lampbutton.place(x=45, y=180, anchor=tkinter.CENTER)

        self.switchtheme = customtkinter.CTkOptionMenu(self, values=["System", "Dark", "Light"], width=80, height=25, dynamic_resizing=False, command=self.change_appearance_mode_event)
        self.switchtheme.place(x=355, y=180, anchor=tkinter.CENTER)
        self.switchtheme.set("System")

        self.texttheme = customtkinter.CTkLabel(self, text="🎨") 
        self.texttheme.place(x=300, y=180, anchor=tkinter.CENTER)

        self.pin = customtkinter.CTkLabel(self, text="📌") 
        self.pin.place(x=100, y=180, anchor=tkinter.CENTER)


    def cleartextbox(self):
        self.frame.delete("1.0","end")

    def button_callback(self):
        try:
            password = ""
            chars = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
            length = int(self.combox.get())
            for i in range(length):
                password += random.choice(chars)
            self.frame.insert("1.0", password + "\n")
        except:
            showerror(title="Error", message="You haven't chosen anything!")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def togglecommand(self, choice):
        if choice == "Pin":
            self.attributes("-topmost", True)
        elif choice == "Unpin":
            self.attributes("-topmost", False)


if __name__ == "__main__":
    app = App()
    app.mainloop()