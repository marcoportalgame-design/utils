import tkinter as tk
from tkinter import ttk
root = tk.Tk()
splash = tk.Toplevel(root)
splash.overrideredirect(True)
splash.geometry("400x300+{}+{}".format(
    (root.winfo_screenwidth() - 400) // 2,
    (root.winfo_screenheight() - 300) // 2
))
ttk.Progressbar(splash, mode="determinate").pack()
splash.wm_attributes("-topmost", True)
root.title("Noobws0.1")
root.state("zoomed")
root.configure(bg="black")
terminal = tk.Text(splash, bg="violet")
terminal.pack()

root.mainloop()