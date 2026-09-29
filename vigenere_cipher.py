import tkinter as tk
from tkinter import ttk, messagebox

def clean_key(key):
    key = "".join(ch for ch in key.upper() if ch.isalpha())
    return key

def vigenere_encrypt(text, key):
    key = clean_key(key)
    if not key:
        raise ValueError("Kunci harus berisi huruf alfabet.")
    result = []
    key_index = 0

    for ch in text:
        if ch.isalpha():
            p = ord(ch.upper()) - ord("A")
            k = ord(key[key_index % len(key)]) - ord("A")
            c = (p + k) % 26
            result.append(chr(c + ord("A")))
            key_index += 1
        else:
            result.append(ch)
    return "".join(result)

def vigenere_decrypt(text, key):
    key = clean_key(key)
    if not key:
        raise ValueError("Kunci harus berisi huruf alfabet.")
    result = []
    key_index = 0

    for ch in text:
        if ch.isalpha():
            c = ord(ch.upper()) - ord("A")
            k = ord(key[key_index % len(key)]) - ord("A")
            p = (c - k) % 26
            result.append(chr(p + ord("A")))
            key_index += 1
        else:
            result.append(ch)
    return "".join(result)

def get_key():
    key = clean_key(entry_key.get())
    if not key:
        messagebox.showerror("Kunci tidak valid", "Masukkan kata kunci berupa huruf, misalnya LAMPION.")
        return None
    return key

def encrypt_action():
    key = get_key()
    if key is None:
        return
    text = entry_text.get("1.0", tk.END).rstrip("\n")
    if not text:
        messagebox.showwarning("Input kosong", "Masukkan plaintext terlebih dahulu.")
        return
    try:
        result = vigenere_encrypt(text, key)
        output.delete("1.0", tk.END)
        output.insert(tk.END, result)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def decrypt_action():
    key = get_key()
    if key is None:
        return
    text = entry_text.get("1.0", tk.END).rstrip("\n")
    if not text:
        messagebox.showwarning("Input kosong", "Masukkan ciphertext terlebih dahulu.")
        return
    try:
        result = vigenere_decrypt(text, key)
        output.delete("1.0", tk.END)
        output.insert(tk.END, result)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def clear_action():
    entry_text.delete("1.0", tk.END)
    entry_key.delete(0, tk.END)
    output.delete("1.0", tk.END)

root = tk.Tk()
root.title("Sistem Vigenère Cipher")
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

ttk.Label(main, text="VIGENÈRE CIPHER", style="Title.TLabel").pack(pady=(0, 5))
ttk.Label(
    main,
    text="Cipher Abjad-Majemuk • C = (P + K) mod 26 • P = (C - K) mod 26",
    style="Info.TLabel"
).pack(pady=(0, 18))

ttk.Label(main, text="Pesan / Ciphertext:", font=("Segoe UI", 10, "bold")).pack(anchor="w")
entry_text = tk.Text(main, height=7, font=("Consolas", 12), wrap="word")
entry_text.pack(fill="x", pady=(5, 15))

key_frame = ttk.Frame(main)
key_frame.pack(fill="x", pady=(0, 15))
ttk.Label(key_frame, text="Kata Kunci:", font=("Segoe UI", 10, "bold")).pack(side="left")
entry_key = ttk.Entry(key_frame, width=25)
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
    text="Contoh materi: plaintext kriptografi... dengan kunci LAMPION",
    style="Info.TLabel"
).pack(pady=(10, 0))

root.mainloop()
