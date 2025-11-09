import tkinter as tk


num_levels = 8



class BoxMover(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Box Mover")
        self.geometry("800x600")
        container = tk.Frame(self)
        
        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (MainMenu, LvlSelect):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")                    #columnas

        self.show_frame(MainMenu)                                  #starting page

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()
    
      
class MainMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.configure(bg="light blue")
        
        title = tk.Label(
            self,
            text="Box Mover",
            font=("Helvetica", 40),
            bg= "light blue",
            fg="dark blue"
        )
        title.pack(side="top", fill="x")

       
        levels = tk.Button(
                self,
                text="Levels",
                bg="white",
                fg="black",
                height=2,
                width=40,
                command=lambda: controller.show_frame(LvlSelect)   
            )
        levels.pack(pady=125)

        exit = tk.Button(
                self,
                text="Exit",
                bg="white",
                fg="black",
                height=2,
                width=40,
                command=parent.master.destroy
            )
        exit.pack()




class LvlSelect(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="light blue")

        title = tk.Label(
            self,
            text="Select Level",
            font=("Helvetica", 40),
            bg= "light blue",
            fg="dark blue"
        )
        title.pack(pady=10)

        button_list = []
        for level in range(1,  num_levels + 1):
            button_list.append(tk.Button(
                self,
                text=f"Level {level}",
                bg="white",
                fg="black",
                height=1,
                width=40,
                command=print("open level")   #lambda:
            ))

        for i in range(0, len(button_list)):
            
            button_list[i].pack(pady=10)
        
        back = tk.Button(
            self,
            text="Back",
            bg="white",
            fg="black",
            height=2,
            width=40,
            command=lambda:controller.show_frame(MainMenu)
        )
        back.pack(pady=20)
            





app = BoxMover()
app.mainloop()