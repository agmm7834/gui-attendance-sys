import tkinter as tk
from datetime import date
import database

database.create_tables()

def refresh_students():
    listbox.delete(0, tk.END)
    students.clear()
    for s in database.get_students():
        students.append(s)
        listbox.insert(tk.END, s[1])

def add_student():
    name = entry.get()
    if name:
        database.add_student(name)
        entry.delete(0, tk.END)
        refresh_students()

def mark_present():
    idx = listbox.curselection()
    if idx:
        student_id = students[idx[0]][0]
        database.mark_attendance(student_id, date.today().isoformat(), "BOR")
        status_label.config(text="Davomat: BOR ✅")

def mark_absent():
    idx = listbox.curselection()
    if idx:
        student_id = students[idx[0]][0]
        database.mark_attendance(student_id, date.today().isoformat(), "YO‘Q")
        status_label.config(text="Davomat: YO‘Q ❌")

# ---------- GUI ----------
root = tk.Tk()
root.title("Talabalar Davomat Tizimi")
root.geometry("350x350")

tk.Label(root, text="Talaba ismi").pack()
entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Talaba qo‘shish", command=add_student).pack(pady=5)

listbox = tk.Listbox(root)
listbox.pack(fill=tk.BOTH, expand=True, padx=10)

tk.Button(root, text="BOR", bg="lightgreen", command=mark_present).pack(pady=3)
tk.Button(root, text="YO‘Q", bg="lightcoral", command=mark_absent).pack(pady=3)

status_label = tk.Label(root, text="")
status_label.pack(pady=5)

students = []
refresh_students()

root.mainloop()
