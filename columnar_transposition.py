import tkinter as tk
from tkinter import ttk, messagebox

def key_order(key):
    # Kunci sebaiknya mempunyai huruf berbeda, seperti contoh TOMBAK pada materi.
    key = "".join(ch for ch in key.upper() if ch.isalpha())
    if not key:
        raise ValueError("Kata kunci harus berisi huruf.")
    if len(set(key)) != len(key):
        raise ValueError(
            "Untuk versi ini, setiap huruf pada kunci harus berbeda.\n"
            "Contoh: TOMBAK"
        )
    return key

def encrypt_columnar(text, key):
    key = key_order(key)
    # Spasi dan karakter non-alfabet dibuang sesuai contoh transposisi pada materi.
    text = "".join(ch.upper() for ch in text if ch.isalpha())

    if not text:
        raise ValueError("Plaintext harus berisi huruf.")

    cols = len(key)
    rows = (len(text) + cols - 1) // cols

    # Isi tabel dari kiri ke kanan, atas ke bawah.
    table = []
    pos = 0
    for _ in range(rows):
        row = []
        for _ in range(cols):
            if pos < len(text):
                row.append(text[pos])
                pos += 1
            else:
                row.append("")
        table.append(row)

    # Urutan kolom ditentukan oleh urutan alfabet pada kata kunci.
    order = sorted(range(cols), key=lambda i: key[i])

    cipher = []
    for col in order:
        for row in table:
            if row[col]:
                cipher.append(row[col])

    return "".join(cipher)

def decrypt_columnar(ciphertext, key):
    key = key_order(key)
    ciphertext = "".join(ch.upper() for ch in ciphertext if ch.isalpha())

    if not ciphertext:
        raise ValueError("Ciphertext harus berisi huruf.")

    cols = len(key)
    rows = (len(ciphertext) + cols - 1) // cols
    remainder = len(ciphertext) % cols

    # Panjang kolom pada tabel asli.
    col_lengths = [rows if (remainder == 0 or i < remainder) else rows - 1
                   for i in range(cols)]

    order = sorted(range(cols), key=lambda i: key[i])
    columns = [""] * cols

    pos = 0
    for col in order:
        length = col_lengths[col]
        columns[col] = ciphertext[pos:pos + length]
        pos += length

    plaintext = []
    for row in range(rows):
        for col in range(cols):
            if row < len(columns[col]):
                plaintext.append(columns[col][row])

    return "".join(plaintext)

def encrypt_action():
    key = entry_key.get()
    text = entry_text.get("1.0", tk.END).rstrip("\n")
    if not text:
        messagebox.showwarning("Input kosong", "Masukkan plaintext terlebih dahulu.")
        return
    try:
        result = encrypt_columnar(text, key)
        output.delete("1.0", tk.END)
        output.insert(tk.END, result)
    except ValueError as e:
        messagebox.showerror("Input tidak valid", str(e))

def decrypt_action():
    key = entry_key.get()
    text = entry_text.get("1.0", tk.END).rstrip("\n")
    if not text:
        messagebox.showwarning("Input kosong", "Masukkan ciphertext terlebih dahulu.")
        return
    try:
        result = decrypt_columnar(text, key)
        output.delete("1.0", tk.END)
        output.insert(tk.END, result)
    except ValueError as e:
        messagebox.showerror("Input tidak valid", str(e))

def clear_action():
    entry_text.delete("1.0", tk.END)
    entry_key.delete(0, tk.END)
    output.delete("1.0", tk.END)

root = tk.Tk()
root.title("Sistem Columnar Transposition Cipher")
root.geometry("760x580")
root.minsize(680, 520)
root.configure(bg="#f4f7fb")

style = ttk.Style()
style.theme_use("clam")
style.configure("Title.TLabel", font=("Segoe UI", 22, "bold"), background="#f4f7fb")
style.configure("Info.TLabel", font=("Segoe UI", 10), background="#f4f7fb")
style.configure("TButton", font=("Segoe UI", 10, "bold"), padding=8)

main = ttk.Frame(root, padding=25)
main.pack(fill="both", expand=True)

ttk.Label(main, text="COLUMNAR TRANSPOSITION", style="Title.TLabel").pack(pady=(0, 5))
ttk.Label(
    main,
    text="Cipher Transposisi • Susun plaintext ke dalam baris lalu baca kolom berdasarkan kunci",
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
ttk.Label(key_frame, text="Contoh: TOMBAK", style="Info.TLabel").pack(side="left")

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
    text="Catatan: gunakan kunci dengan huruf berbeda, misalnya TOMBAK.",
    style="Info.TLabel"
).pack(pady=(10, 0))

root.mainloop()
