import tkinter as tk
import random

# لیست شغل‌ها
jobs = [
    "برنامه‌نویس", "طراح گرافیک", "مهندس عمران", "پزشک", "معلم",
    "نویسنده", "مکانیک", "آشپز", "عکاس", "محقق",
    "مدیر پروژه", "مشاور", "پرستار", "خلبان", "معمار",
    "مترجم", "بازیگر", "موسیقی‌دان", "راننده", "کارآفرین"
]

def entekhab_shoghl():
    name = name_entry.get().strip()
    if name == "":
        result_label.config(text="لطفاً نام خود را وارد کنید.")
    else:
        job = random.choice(jobs)
        result_label.config(text=f"🎉 {name} عزیز، شغل پیشنهادی شما: «{job}»")

# ساخت پنجره اصلی
root = tk.Tk()
root.title("🎲 انتخاب شغل شانسی")
root.geometry("400x300")
root.configure(bg="#f0f8ff")

# قاب اصلی
frame = tk.Frame(root, bg="#e6f2ff", bd=2, relief="ridge")
frame.place(relx=0.5, rely=0.5, anchor="center", width=350, height=220)

# ویجت‌ها
tk.Label(frame, text="نام خود را وارد کنید:", font=("B Nazanin", 13), bg="#e6f2ff").pack(pady=10)
name_entry = tk.Entry(frame, font=("B Nazanin", 13), justify="center")
name_entry.pack()

tk.Button(frame, text="انتخاب شغل", command=entekhab_shoghl, font=("B Nazanin", 12), bg="#cce5ff", activebackground="#99ccff").pack(pady=10)
result_label = tk.Label(frame, text="", font=("B Nazanin", 13), fg="#003366", bg="#e6f2ff")
result_label.pack()

signature = tk.Label(root, text="ساخته شده توسط صدرا اسدی ©", font=("B Nazanin", 10), bg="#f0f8ff", fg="gray")
signature.pack(side="bottom", pady=5)

# اجرای برنامه
root.mainloop()