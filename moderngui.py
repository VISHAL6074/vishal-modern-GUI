import customtkinter
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.geometry("500x500")
root.title("Vishal's Program")

def login():
    print("test")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20,padx=60,fill="both",expand=True)

label1 = customtkinter.CTkLabel(master=frame,text="Login System",font=("Roboto",24))
label1.pack(padx=12,pady=10)

entry1 = customtkinter.CTkEntry(master=frame,placeholder_text="userid")
entry1.pack(pady=12,padx=10)
entry2 = customtkinter.CTkEntry(master=frame,placeholder_text="Password",show ="*")
entry2.pack(pady=12,padx=10)

button = customtkinter.CTkButton(master=frame, text="Submit Data",command=login)
button.pack(pady=12,padx=10)

chkbox = customtkinter.CTkCheckBox(master=frame,text="Save for Future")
chkbox.pack(pady=12,padx=10)

root.mainloop()
