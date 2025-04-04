import tkinter as tk
from tkinter import messagebox

class TextEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Editor")
        self.filename = "output.txt"
        self.file = open(self.filename, "a")
        self.questions = []

        self.text_input = tk.Entry(root, width=100)
        self.text_input.pack(pady=10)

        self.submit_button = tk.Button(root, text="Submit", command=self.submit_text)
        self.submit_button.pack(pady=5)

        self.save_exit_button = tk.Button(root, text="Save and Exit", command=self.save_and_exit)
        self.save_exit_button.pack(pady=5)

        self.clear_button = tk.Button(root, text="Clear the file", command=self.clear_file)
        self.clear_button.pack(pady=5)

        self.clear_insertion = tk.Button(root, text="Clear insertions", command=self.clear_insertion)
        self.clear_insertion.pack(pady=5)

        self.exit_button = tk.Button(root, text="Exit", command=self.exit_without_save)
        self.exit_button.pack(pady=5)

    def submit_text(self):
        text = self.text_input.get()
        if text.strip():
            self.questions.append(text + "\n")
            self.text_input.delete(0, tk.END)
            messagebox.showinfo("Success", "Text submitted successfully!")

    def save_and_exit(self):
        self.file.writelines(self.questions)
        self.file.close()
        self.root.destroy()

    def exit_without_save(self):
        self.file.close()
        self.file.close()
        self.root.destroy()
    
    def clear_file(self) :
        self.file.seek(0)
        self.file.truncate()

    def clear_insertion(self) :
        self.questions.clear()

root = tk.Tk()
app = TextEditorApp(root)
root.mainloop()