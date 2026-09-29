import tkinter as tk
from tkinter import ttk, messagebox

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def caesar_encrypt(text, key):
    result = ""
    for ch in text:
        if ch.isalpha():
            upper = ch.upper()
            idx = ord(upper) - ord("A")
            new_idx = (idx + key) % 26
            result += chr(new_idx + ord("A"))
        else:
            result += ch
    return result

def caesar_decrypt(text, key):
    return caesar_encrypt(text, -key)

def get_key():
    try:
        key = int(entry_key.get())
        if not 0 <= key <= 25:
            raise ValueError
        return key
    except ValueError:
        messagebox.showerror("Kunci tidak valid", "Masukkan kunci berupa angka 0 sampai 25.")
        return None

def encrypt_action():
    key = get_key()
    if key is None:
        return
    text = entry_text.get("1.0", tk.END).rstrip("\n")
    if not text:
        messagebox.showwarning("Input kosong", "Masukkan plaintext terlebih dahulu.")
        return
    output.delete("1.0", tk.END)
    output.insert(tk.END, caesar_encrypt(text, key))

def decrypt_action():
    key = get_key()
    if key is None:
        return
    text = entry_text.get("1.0", tk.END).rstrip("\n")
    if not text:
        messagebox.showwarning("Input kosong", "Masukkan ciphertext terlebih dahulu.")
        return
    output.delete("1.0", tk.END)
    output.insert(tk.END, caesar_decrypt(text, key))

def clear_action():
    entry_text.delete("1.0", tk.END)
    entry_key.delete(0, tk.END)
    output.delete("1.0", tk.END)

root = tk.Tk()
root.title("Sistem Caesar Cipher")
root.geometry("720x560")
root.minsize(650, 500)
root.configure(bg="#f4f7fb")

style = ttk.Style()
style.theme_use("clam")
style.configure("Title.TLabel", font=("Segoe UI", 22, "bold"), background="#f4f7fb")
style.configure("Info.TLabel", font=("Segoe UI", 10), background="#f4f7fb")
style.configure("TButton", font=("Segoe UI", 10, "bold"), padding=8)

main = ttk.Frame(root, padding=25)
main.pack(fill="both", expand=True)

ttk.Label(main, text="CAESAR CIPHER", style="Title.TLabel").pack(pady=(0, 5))
ttk.Label(
    main,
    text="Enkripsi dan Dekripsi • C = (P + k) mod 26 • P = (C - k) mod 26",
    style="Info.TLabel"
).pack(pady=(0, 18))

ttk.Label(main, text="Pesan / Ciphertext:", font=("Segoe UI", 10, "bold")).pack(anchor="w")
entry_text = tk.Text(main, height=7, font=("Consolas", 12), wrap="word")
entry_text.pack(fill="x", pady=(5, 15))

key_frame = ttk.Frame(main)
key_frame.pack(fill="x", pady=(0, 15))
ttk.Label(key_frame, text="Kunci (0–25):", font=("Segoe UI", 10, "bold")).pack(side="left")
entry_key = ttk.Entry(key_frame, width=12)
entry_key.pack(side="left", padx=10)

button_frame = ttk.Frame(main)
button_frame.pack(pady=5)
ttk.Button(button_frame, text="ENKRIPSI", command=encrypt_action).pack(side="left", padx=5)
ttk.Button(button_frame, text="DEKRIPSI", command=decrypt_action).pack(side="left", padx=5)
ttk.Button(button_frame, text="BERSIHKAN", command=clear_action).pack(side="left", padx=5)

ttk.Label(main, text="Hasil:", font=("Segoe UI", 10, "bold")).pack(anchor="w", pady=(20, 5))
output = tk.Text(main, height=7, font=("Consolas", 12), wrap="word", bg="#eef3f8")
output.pack(fill="both", expand=True)

ttk.Label(
    main,
    text="Contoh: HALO DUNIA + k=3 → KDOR GXQLD",
    style="Info.TLabel"
).pack(pady=(10, 0))

root.mainloop()
