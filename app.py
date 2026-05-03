import tkinter as tk
from tkinter import messagebox

# Fungsi tambah tugas
def tambah_tugas():
    tugas = entry.get()
    if tugas != "":
        listbox.insert(tk.END, tugas)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Peringatan", "Tugas tidak boleh kosong!")

# Fungsi hapus tugas
def hapus_tugas():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
    except:
        messagebox.showwarning("Peringatan", "Pilih tugas yang ingin dihapus!")

# GUI utama
root = tk.Tk()
root.title("Aplikasi To-Do List")
root.geometry("300x400")

# Input
entry = tk.Entry(root, width=25)
entry.pack(pady=10)

# Tombol tambah
btn_tambah = tk.Button(root, text="Tambah Tugas", command=tambah_tugas)
btn_tambah.pack(pady=5)

# List tugas
listbox = tk.Listbox(root, width=30, height=10)
listbox.pack(pady=10)

# Tombol hapus
btn_hapus = tk.Button(root, text="Hapus Tugas", command=hapus_tugas)
btn_hapus.pack(pady=5)

# Jalankan aplikasi
root.mainloop()
