import threading
from tkinter import messagebox
import tkinter as tk
from pathlib import Path

target_dir = Path(r'\\jimny\snet01\ｓ-ｎｅｔ\補給現品票')
file = target_dir / '補給用現品票.pdf'
ico_path = r'C:\Windows\user_icon\python_logo.ico'
bg_color = 'RosyBrown4'
fg_color = 'snow'

class App():
    def __init__(self,root):
        self.root = root
        self.root.title('補給現品票再構成')
        self.root.geometry('300x100')
        self.root.config(bg=bg_color)
        self.root.attributes('-topmost',True)

        if ico_path:
            self.root.iconbitmap(ico_path)

        self.frame = tk.Frame(self.root,bg=bg_color)
        self.frame.pack()
        self.label = tk.Label(self.frame,text=f'加工先:{target_dir}',
                              bg=bg_color,fg=fg_color,pady=10).grid(row=0,column=0)
        self.btn = tk.Button(self.frame,text='再構成',bg=bg_color,fg=fg_color,padx=10,pady=5,
                             font=('Helvetica', 12),command=self.start_task)
        self.btn.grid(row=1,column=0)

        self.controls = [self.btn]
    def start_task(self):
        if not file.exists():
            messagebox.showerror('元ファイルなし','補給用現品票.pdf がありません。処理を終了します。')
            return

        self.set_enabled(False)
        threading.Thread(target=self.run_task,daemon=True).start()

    def set_enabled(self,enabled):
        state = 'normal' if enabled else 'disabled'

        for ctrl in self.controls:
            ctrl.config(state=state)

    def run_task(self):
        from PR1_A4_9split import PR_1_split_A4_9
        from PR2_marge_9 import restructure_combined_pdf
        try:
            pdf_doc = PR_1_split_A4_9(file)
            restructure_combined_pdf(pdf_doc,target_dir)
        finally:
            self.root.after(0,self.finish_task)

    def finish_task(self):
        self.set_enabled(True)
        messagebox.showinfo('処理終了', '分割が完了しました。')

if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()