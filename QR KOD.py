import tkinter as tk
from tkinter import messagebox, filedialog
import qrcode
from PIL import Image, ImageTk

def create_qr_code(content, save_path):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(content)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(save_path)
    return img
def make():
    content = txtMetin.get()
    if content:
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if save_path:
            create_qr_code(content, save_path)
            messagebox.showinfo("Başarılı", "QR kod oluşturuldu ve kaydedildi.")
        else:
            messagebox.showerror("Hata", "Kaydetme işlemi iptal edildi.")
    else:
        messagebox.showerror("Hata", "Lütfen bir içerik girin veya dosya seçin.")

# Pencere oluşturma
window = tk.Tk()
window.title("qr code maker")
window.geometry("400x400")

# Kullanıcı arayüzü
tk.Label(window, text="QR CODE OLUŞTURULACAK METNİ GİR!").pack()
txtMetin = tk.Entry(window, width=50)
txtMetin.pack(pady=10)

# QR oluşturma butonu
btn_qr = tk.Button(window, text="QR OLUŞTUR", command=make)
btn_qr.pack(pady=20)

window.mainloop()