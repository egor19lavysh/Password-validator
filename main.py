#import hashlib
import uuid
import tkinter as tk
from tkinter import messagebox

def hash(data : str):
    k = 2872834536
    sum = 0
    for n in range(len(data)):
        sum += ord(data[n]) * k ** n
    return hex(sum % 245390242324457893434353)


PASSWORD = "Alexander_Victorovich_postavte_five_please"
SALT = uuid.uuid4()

database = {
    "user" : {
        "salt" : SALT,
        "password" : hash(PASSWORD + SALT.hex) #hashlib.md5((PASSWORD + SALT.hex).encode())}
    }
}
def validate():
    password = password_var.get()

    if hash(password + database["user"]["salt"].hex) == database["user"]["password"]:
        messagebox.showinfo("Result", "Пароль подтвержден")
    else:
        messagebox.showerror("Error", "Пароль неподтвержден")

root = tk.Tk()
root.title("Password validator")
root.geometry("300x150")
root.resizable(False, False)

password_var = tk.StringVar()
label = tk.Label(root, text="Enter Password:")
label.pack(pady=10)

password_entry = tk.Entry(root, textvariable=password_var, width=30, show='*')
password_entry.pack(pady=5)

confirm_btn = tk.Button(root, command=validate, text="login")
confirm_btn.pack(pady=5)

if __name__ == "__main__":
    root.mainloop()