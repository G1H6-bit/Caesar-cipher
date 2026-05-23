import tkinter as tk
from tkinter import ttk, messagebox


# shift every letter by the given number — spaces and symbols stay the same
def encrypt(text, shift):
    result = []
    for char in text:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            # move the letter forward by shift, wrap around if it goes past Z
            shifted = (ord(char) - base + shift) % 26 + base
            result.append(chr(shifted))
        else:
            result.append(char)
    return "".join(result)


# decrypt is just encrypt but in the opposite direction
def decrypt(text, shift):
    return encrypt(text, -shift)


class CaesarApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Caesar Cipher")
        self.resizable(False, False)
        self.configure(bg="#0b0e14")

        self.build_styles()
        self.build_ui()

    def build_styles(self):
        style = ttk.Style(self)
        style.theme_use("clam")

        style.configure("Dark.TFrame",  background="#0b0e14")
        style.configure("Card.TFrame",  background="#111520", relief="flat")

        style.configure("Title.TLabel",
                        background="#0b0e14", foreground="#00e5ff",
                        font=("Courier New", 22, "bold"))
        style.configure("Sub.TLabel",
                        background="#0b0e14", foreground="#64748b",
                        font=("Courier New", 10))
        style.configure("Field.TLabel",
                        background="#111520", foreground="#00e5ff",
                        font=("Courier New", 9, "bold"))
        style.configure("OutLabel.TLabel",
                        background="#0d1117", foreground="#64748b",
                        font=("Courier New", 9))
        style.configure("Cipher.TLabel",
                        background="#0d1117", foreground="#00e5ff",
                        font=("Courier New", 13, "bold"),
                        wraplength=380, justify="left")
        style.configure("Plain.TLabel",
                        background="#0d1117", foreground="#00ff9d",
                        font=("Courier New", 13, "bold"),
                        wraplength=380, justify="left")
        style.configure("Status.TLabel",
                        background="#111520", foreground="#64748b",
                        font=("Courier New", 9))

        style.configure("Accent.TButton",
                        background="#7c3aed", foreground="white",
                        font=("Courier New", 11, "bold"),
                        relief="flat", borderwidth=0, padding=(20, 10))
        style.map("Accent.TButton",
                  background=[("active", "#00e5ff")],
                  foreground=[("active", "#0b0e14")])

        style.configure("Dark.TSpinbox",
                        fieldbackground="#0d1117", background="#0d1117",
                        foreground="#e2e8f0", insertcolor="#e2e8f0",
                        font=("Courier New", 13))

    def build_ui(self):

        # header section
        header = ttk.Frame(self, style="Dark.TFrame")
        header.pack(fill="x", pady=(24, 0))

        ttk.Label(header, text="DECODELABS",
                  background="#0b0e14", foreground="#00e5ff",
                  font=("Courier New", 10, "bold")).pack()
        ttk.Label(header, text="Caesar Cipher",
                  style="Title.TLabel").pack()
        ttk.Label(header, text="// shift · encrypt · decrypt · verify",
                  style="Sub.TLabel").pack(pady=(2, 16))

        # purple line under the header
        tk.Frame(self, height=2, bg="#7c3aed").pack(fill="x")

        # main card
        card = ttk.Frame(self, style="Card.TFrame", padding=20)
        card.pack(fill="both", padx=24, pady=20)

        # text input
        ttk.Label(card, text="PLAINTEXT", style="Field.TLabel").pack(anchor="w")
        self.pt_text = tk.Text(
            card, height=4, width=52,
            bg="#0d1117", fg="#e2e8f0",
            insertbackground="#e2e8f0",
            font=("Courier New", 12),
            relief="flat", bd=8,
            highlightthickness=1,
            highlightbackground="#1f2a3c",
            highlightcolor="#00e5ff"
        )
        self.pt_text.pack(fill="x", pady=(4, 12))
        self.pt_text.insert("1.0", "Hello World")

        # shift key selector
        key_row = ttk.Frame(card, style="Card.TFrame")
        key_row.pack(fill="x", pady=(0, 16))
        ttk.Label(key_row, text="SHIFT KEY  (0 – 25)",
                  style="Field.TLabel").pack(side="left")
        self.shift_var = tk.IntVar(value=3)
        ttk.Spinbox(
            key_row, from_=0, to=25,
            textvariable=self.shift_var,
            width=6, style="Dark.TSpinbox"
        ).pack(side="left", padx=(12, 0))

        # run button
        ttk.Button(
            card, text="⚡  Encrypt & Decrypt",
            style="Accent.TButton",
            command=self.run_cipher
        ).pack(fill="x", pady=(0, 16))

        # output area — two boxes side by side
        out_row = ttk.Frame(card, style="Card.TFrame")
        out_row.pack(fill="x")
        out_row.columnconfigure(0, weight=1)
        out_row.columnconfigure(1, weight=1)

        ct_box = tk.Frame(out_row, bg="#0d1117", padx=12, pady=10)
        ct_box.grid(row=0, column=0, padx=(0, 6), sticky="nsew")
        ttk.Label(ct_box, text="🔐  CIPHERTEXT",
                  style="OutLabel.TLabel").pack(anchor="w")
        self.ct_var = tk.StringVar(value="—")
        ttk.Label(ct_box, textvariable=self.ct_var,
                  style="Cipher.TLabel").pack(anchor="w", pady=(4, 0))

        dt_box = tk.Frame(out_row, bg="#0d1117", padx=12, pady=10)
        dt_box.grid(row=0, column=1, padx=(6, 0), sticky="nsew")
        ttk.Label(dt_box, text="🔓  DECRYPTED",
                  style="OutLabel.TLabel").pack(anchor="w")
        self.dt_var = tk.StringVar(value="—")
        ttk.Label(dt_box, textvariable=self.dt_var,
                  style="Plain.TLabel").pack(anchor="w", pady=(4, 0))

        # status bar at the bottom
        self.status_var = tk.StringVar(value="// waiting for input…")
        ttk.Label(card, textvariable=self.status_var,
                  style="Status.TLabel").pack(anchor="w", pady=(14, 0))

        # press enter to run
        self.bind("<Return>", lambda e: self.run_cipher())

    def run_cipher(self):
        plaintext = self.pt_text.get("1.0", "end-1c").strip()

        # dont run if the input is empty
        if not plaintext:
            messagebox.showwarning("Input needed", "Please enter some text first.")
            return

        # make sure the shift value is valid
        try:
            shift = int(self.shift_var.get())
            if not (0 <= shift <= 25):
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid key", "Shift must be a number between 0 and 25.")
            return

        # run encrypt and decrypt
        ciphertext = encrypt(plaintext, shift)
        decrypted  = decrypt(ciphertext, shift)

        self.ct_var.set(ciphertext)
        self.dt_var.set(decrypted)

        # update the status bar
        self.status_var.set(
            f"✔  key={shift}  ·  {len(plaintext)} characters processed"
        )


if __name__ == "__main__":
    app = CaesarApp()
    app.mainloop()