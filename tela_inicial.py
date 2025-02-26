import tkinter as tk
from tkinter import ttk
import time



class WelcomeScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Bem-vindo")
        self.geometry("600x400")
        self.configure(bg="#107db2")
        self.wm_maxsize(1280, 1080)
        self.wm_minsize(720, 480)
        self.resizable(True, True)
          # Remove a barra de título
        
        # Texto de boas-vindas
        self.label = ttk.Label(self, text="Bem-vindo ao Sistema!", font=("Arial", 18, "bold"), background="#FFFFFF", foreground="black")
        self.label.place(relx=0.5, rely=0.4, anchor="center")
        
        # Barra de progresso
        self.progress = ttk.Progressbar(self, orient=tk.HORIZONTAL, length=300, mode='determinate')
        self.progress.place(relx=0.5, rely=0.6, anchor="center")
        
        # Botão de prosseguir
        self.proceed_button = ttk.Button(self, text="Prosseguir", command=self.proceed)
        self.proceed_button.place(relx=0.5, rely=0.75, anchor="center")
        
        # Animação de fade-in
        self.attributes('-alpha', 0)
        self.fade_in()
        self.load_progress()
        
    def fade_in(self):
        alpha = 0
        while alpha < 1:
            self.attributes('-alpha', alpha)
            alpha += 0.05
            self.update()
            time.sleep(0.05)
    
    def load_progress(self):
        for i in range(100):
            self.progress['value'] = i + 1
            self.update_idletasks()
            time.sleep(0.03)
    
    def proceed(self):
        
        self.destroy()
        from aplicacao import Application
        Application()

if __name__ == "__main__":
    app = WelcomeScreen()
    app.mainloop()
