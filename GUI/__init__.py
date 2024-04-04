import tkinter as tk


# Frame to show all discovered, but not connected, individuals
class DiscoveryFrame(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(bg="red")

# Frame to display application name + current connections + current host + port
class InformationFrame(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(bg="blue")

# Frame to display all connected individuals, anyone who message traffic has gone between
class FriendsFrame(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(bg="green")

# Frame to dynamically display and show messages from user
class MessageFrame(tk.Frame):
    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.create_widgets()

    # Creates bottom widgets for text entry and sending on GUI
    def create_widgets(self):
        self.send_button = tk.Button(self, text="Send Message", command=self.send_message)
        self.send_button.pack(pady=1, padx=1, side=tk.BOTTOM)

        self.entry = tk.Entry(self, width=40)
        self.entry.pack(pady=1, padx=1, side=tk.BOTTOM)

    def send_message(self):
        message = self.entry.get()
        # Here you can implement the functionality to send the message
        print("Message sent:", message)
        self.entry.delete(0, tk.END)  # Clear the entry after sending

# GUI Packs every Frame using column packing
class FourFramesApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Four Frames App")

        self.frame1 = DiscoveryFrame(self.master)
        self.frame1.grid(row=0, column=0, sticky="nsew")

        self.frame2 = InformationFrame(self.master)
        self.frame2.grid(row=0, column=1, sticky="nsew")

        self.frame3 = FriendsFrame(self.master)
        self.frame3.grid(row=1, column=0, sticky="nsew")

        self.frame4 = MessageFrame(self.master)
        self.frame4.grid(row=1, column=1, sticky="nsew")

        self.master.grid_rowconfigure(0, weight=2)
        self.master.grid_rowconfigure(1, weight=3)
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=3)

