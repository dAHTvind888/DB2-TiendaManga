from SQLServer_functions import * 

# Main window
def start_window():
    #Tk() crea la ventana
    main_window = tk.Tk()
    #geomtry() is el tamano de la venta
    main_window.geometry("400x300")
    #.title() is el titulo de la ventana
    main_window.title("Log In")
    
    labelUsuario = tk.Label(main_window, text="Usuario: ")
    labelUsuario.pack(pady=5)
    entryUsuario = tk.Entry(main_window)
    entryUsuario.pack(pady=5)

    labelPassword = tk.Label(main_window, text="Password: ")
    labelPassword.pack(pady=5)
    entryPassword = tk.Entry(main_window, show="*")
    entryPassword.pack(pady=5)

    botonConectar = tk.Button(main_window, 
                          text="Conectar", 
                          command=lambda: conectar(entryUsuario.get(), entryPassword.get())
                          )
    botonConectar.pack(pady=10)

    #.Button(window, text, command)
    #window is la venta en donde se cread el Button
    #text is el texto del button
    #command is la funcion que se llama al clickar el button
    
    #.pack() se usa siempre que se anade algo a una venta
    #pad y/x is la distancia entre los objetos
    

    
    #mainloop() is lo que mantiene 'alerta' a las acciones del usuario

    main_window.mainloop()

start_window()



    

