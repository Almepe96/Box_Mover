import tkinter as tk

menu = tk.Tk()
menu.geometry("800x600")
menu.configure(background="lightblue")
tk.Wm.wm_title(menu, "Box Mover")

#test start
num_of_levels = 7
#test end


def change_window():
    print("new window opened")


                                                                    #Configuracion basica
menu.grid_columnconfigure(0, weight=2)
menu.grid_columnconfigure(1, weight=2)
menu.grid_columnconfigure(2, weight=2)
menu.grid_columnconfigure(3, weight=2)
menu.grid_columnconfigure(4, weight=2)
menu.grid_rowconfigure(0, weight=3)
menu.grid_rowconfigure(num_of_levels//2 + 2, weight= 3)

                                                                    #Titulo y volver atras
title = tk.Label(
    menu,
    text="Select Level",
    font=("Helvetica", 40),
    bg= "light blue",
    fg="dark blue"
)
title.grid(row=0, column=1, sticky="ew", columnspan=3)
                                                                    #Botones del selector de niveles
button_list = []
for level in range(1,  num_of_levels + 1):
    button_list.append(tk.Button(
        menu,
        text=f"Level {level}",
        bg="white",
        fg="black",
        command=change_window   #lambda:
    ))
j = 0
for i in range(0, len(button_list)):
        menu.grid_rowconfigure((i+2) //2, weight=1)
        if i % 2 == 0:
            button_list[i].grid(row = (i+2) // 2, column = 1, sticky="ew")
        else:
            button_list[i].grid(row = (i+2) // 2, column = 3, sticky="ew")






menu.mainloop()