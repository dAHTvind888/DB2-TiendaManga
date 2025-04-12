import pyodbc
import tkinter as tk
from tkinter import ttk, messagebox

def conectar(usuario, password):
    conn = get_connection(usuario, password)
    if conn:
        # Determinamos el rol del usuario
        if usuario == "VendedorLogin":
            # Si es Vendedor, abrimos ventana de opciones de vendedor
            opcionesVentanaVendedor()
        elif usuario == "GerenteLogin":
            # Si es Gerente, abrimos ventana de opciones de gerente
            opcionesVentanaGerente()
            #abrir_ventana_gerente()
        elif usuario == "DBALogin":
            opcionesVentanaDBA()
        else:
            messagebox.showerror("Acceso Denegado", "El usuario no tiene acceso permitido.")
            conn.close()  # Cerramos conexion si es exitosa
            #main_window.quit()  # Cerrar ventana de login al conectarse

def opcionesVentanaDBA():
    ventanaDBA = tk.Tk()
    ventanaDBA.geometry("400x300")

    add_button = tk.Button(ventanaDBA, text="Add Data", command=add_select_table)
    add_button.pack(pady=10)

    visualize_button = tk.Button(ventanaDBA, text="Visualize Data", command=visualize_select_table)
    visualize_button.pack(pady=10)

    delete_button = tk.Button(ventanaDBA, text="Delete Data", command=delete_select_table)
    delete_button.pack(pady=10)

    modify_button = tk.Button(ventanaDBA, text="Modify Data", command=modify_select_table)
    modify_button.pack(pady=10)


def get_connection(usuario, password):
    try:
        conn = pyodbc.connect("Driver=ODBC Driver 17 for SQL Server;"
                            "Server=LAPTOP-3PL8FJF2;"
                            "Database=Manga_Store_BD2;"
                            f"UID={usuario};"
                            f"PWD={password};"
                            )
        return conn
    except pyodbc.Error as e:
        #  Capturamos error de autenticacion
        if "Login failed" in str(e):  
           messagebox.showerror("Error de autenticacion", "Usuario o contrasena incorrectos")
        else:
            messagebox.showerror("Error de conexion", f"Ocurrio un error: {str(e)}")

def opcionesVentanaGerente():
    ventaGerente = tk.Tk()
    ventaGerente.geometry("400x300")
    ventaGerente.title("Acciones Gerente")
    
    botonReporte1 = tk.Button(ventaGerente, text="Ganancia por Dia", command=ventasPorManga)
    botonReporte1.pack(pady=5)

    botonReporte2 = tk.Button(ventaGerente, text="Top Mangas", command=topMangasVendidos)
    botonReporte2.pack(pady=5)

def ventasPorManga():
    ventanaVentasPorManga = tk.Tk()
    ventanaVentasPorManga.geometry("400x300")
    
    labelDate = tk.Label(ventanaVentasPorManga, text="Fecha(YYYY-MM-DD): ")
    labelDate.pack(pady=5)
    entryDate = tk.Entry(ventanaVentasPorManga)
    entryDate.pack(pady=5)

    # Crear un Treeview para mostrar los resultados
    textResultados = ttk.Treeview(ventanaVentasPorManga, show="headings")
    textResultados.pack(pady=10, fill=tk.BOTH, expand=True)

    def reporte1():
        date = entryDate.get()  # Obtener la fecha introducida por el usuario
        if not date:
            messagebox.showwarning("Advertencia", "Por favor, ingrese una fecha.")
            return

        query = f"SELECT * FROM VentasPorManga WHERE Sales_date = '{date}'"
        
        try:
            conn = get_connection("GerenteLogin", "1234")
            cursor = conn.cursor()
            cursor.execute(query)
            results = cursor.fetchall()  # Obtienes los resultados

            # Limpiar el Treeview antes de insertar los nuevos datos
            textResultados.delete(*textResultados.get_children())

            # Asumiendo que ya tienes una lista de columnas, las obtienes de la tabla
            columns = [description[0] for description in cursor.description]
            textResultados["columns"] = columns
            
            # Establecer encabezados de las columnas
            for col in columns:
                textResultados.heading(col, text=col)
                textResultados.column(col, width=100)

            # Limpiar y agregar filas de datos
            for row in results:
                # Limpiar cada valor de la fila solo si es una cadena
                clean_row = tuple(value.strip().replace("  ", " ") if isinstance(value, str) else value for value in row)
                
                # Insertar la fila limpiada en el Treeview
                textResultados.insert("", tk.END, values=clean_row)

            cursor.close()
            conn.close()

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    # Crear un botón para confirmar la fecha y ejecutar la consulta
    botonConfirmar = tk.Button(ventanaVentasPorManga, text="Confirmar Fecha", command=reporte1)
    botonConfirmar.pack(pady=20)

def topMangasVendidos():
    ventanaTopMangasVendidos = tk.Tk()
    ventanaTopMangasVendidos.geometry("600x400")
    ventanaTopMangasVendidos.title("Top Mangas Vendidos")

    try:
        conn = get_connection("GerenteLogin", "1234")
        cursor = conn.cursor()

        query = "SELECT * FROM TopMangasVendidos ORDER BY Total_Ganado DESC"
        cursor.execute(query)
        rows = cursor.fetchall()

        # Obtener nombres de columnas
        column_names = [desc[0] for desc in cursor.description]

        # Crear Treeview
        tree = ttk.Treeview(ventanaTopMangasVendidos, columns=column_names, show="headings")

        for col in column_names:
            tree.heading(col, text=col)
            tree.column(col, anchor="center", width=150)

        for row in rows:
            # Limpia cada valor de la fila
            clean_row = tuple(str(value).strip().replace("  ", " ") for value in row)
            tree.insert("", tk.END, values=clean_row)

        tree.pack(fill=tk.BOTH, expand=True)

        cursor.close()
        conn.close()

    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")



def opcionesVentanaVendedor():
    ventanaVendedor = tk.Tk()
    ventanaVendedor.geometry("400x300")
    ventanaVendedor.title("Acciones Vendedor")

    botonInsertar = tk.Button(ventanaVendedor, text="Insertar", command=mostrarTablasInsertar)
    botonInsertar.pack(pady=20)

    botonActualizar = tk.Button(ventanaVendedor, text="Actualizar", command=mostrarTablasActualizar)
    botonActualizar.pack(pady=5)

def mostrarTablasInsertar():
    ventanaInsertarTablas = tk.Tk()
    ventanaInsertarTablas.title("Seleccionar: ")

    botonManga = tk.Button(ventanaInsertarTablas, text="Manga", command=insertarManga)
    botonManga.pack(pady=5)

    botonVolume = tk.Button(ventanaInsertarTablas, text="Volume", command=insertarVolume)
    botonVolume.pack(pady=5)

    botonVender = tk.Button(ventanaInsertarTablas, text="Vender", command=venderManga)
    botonVender.pack(pady=5)

    #botonSales = tk.Button(ventanaInsertarTablas, text="Sales", command=insertarSales)
    #botonSales.pack(pady=5)

    #botonSalesDetails = tk.Button(ventanaInsertarTablas, text="Sales Details", command=insertarSalesDetails)
    #botonSalesDetails.pack(pady=5)

    botonCustomer = tk.Button(ventanaInsertarTablas, text="Customer", command=insertarCustomer)
    botonCustomer.pack(pady=5)

def venderManga():
    ventanaVender = tk.Tk()
    ventanaVender.geometry("400x300")

    labelEmpleadoID = tk.Label(ventanaVender, text="ID del Empleado:")
    labelEmpleadoID.pack(pady=5)
    entryEmpleadoID = tk.Entry(ventanaVender)
    entryEmpleadoID.pack(pady=5)

    labelNIT = tk.Label(ventanaVender, text="NIT:")
    labelNIT.pack(pady=5)
    entryNIT = tk.Entry(ventanaVender)
    entryNIT.pack(pady=5)

    def datosManga():
        tempNIT = entryNIT.get()
        conn = get_connection("DBALogin", "12345")
        cursor = conn.cursor()
        cursor.execute(f"SELECT NIT FROM CUSTOMER WHERE NIT = ?", (tempNIT),)
        resultado = cursor.fetchone()
        #if not resultado:
         #   NIT = 'NULL'
            #messagebox.showerror("NIT no valido")
            #return
        
        ventanaDatosManga = tk.Tk()
        ventanaDatosManga.geometry("800x800")

        labelManga = tk.Label(ventanaDatosManga, text="Nombre del Manga:")
        labelManga.pack(pady=5)
        entryManga = tk.Entry(ventanaDatosManga)
        entryManga.pack(pady=5)

        labelVolumen = tk.Label(ventanaDatosManga, text="Volumen del Manga")
        labelVolumen.pack(pady=5)
        entryVolumen = tk.Entry(ventanaDatosManga)
        entryVolumen.pack(pady=5)

        labelCantidad = tk.Label(ventanaDatosManga, text="Cantidad:")
        labelCantidad.pack(pady=5)
        entryCantidad = tk.Entry(ventanaDatosManga)
        entryCantidad.pack(pady=5)

        def cerrar_todo():
            ventanaDatosManga.destroy()
            ventanaVender.destroy()

        def agregarAlCarrito():
            manga = entryManga.get()
            volumen = entryVolumen.get()
            cantidad = entryCantidad.get()
            conn = get_connection("DBALogin", "12345")
            cursor = conn.cursor()
            cursor.execute("""
            SELECT Manga_name, V.Volume_nro 
            FROM MANGA as M
            INNER JOIN VOLUME as V on V.Id_Manga = M.Id_Manga
            WHERE M.Manga_name = ? and V.Volume_nro = ?
            """, (manga, volumen))

            resultado = cursor.fetchone()

            if not resultado:
                messagebox.showerror("Error", "No existe ese manga con ese volumen.")
                return
            
            try:
                carrito.insert("", "end", values=(manga, volumen, cantidad))

            except Exception as e:
                messagebox.showerror("Error:",f" {str(e)}")
                print(str(e))

        def confirmarCompra():
            if not carrito.get_children():
                messagebox.showwarning("Carrito vacio")
                return
            
            NIT = entryNIT.get()
            NIT = int(NIT) if NIT else None
            empleadoID = entryEmpleadoID.get()
            conn = get_connection("VendedorLogin", "123")
            cursor = conn.cursor()
            cursor.execute("EXEC InsertarDetails ?, ?", (NIT, empleadoID))
            conn.commit()

            for item_id in carrito.get_children():
                fila = carrito.item(item_id)['values']
                manga = fila[0]
                volumen = fila[1]
                cantidad = fila[2]
                cursor.execute("EXEC InsertarSales ?, ?, ?", (manga, volumen, cantidad))
                conn.commit()
                print(manga, volumen, cantidad)


        
        botonAgregarManga = tk.Button(ventanaDatosManga, text="Agregar", command=agregarAlCarrito)
        botonAgregarManga.pack(pady=5)

        botonConfirmarCompra = tk.Button(ventanaDatosManga, text="Confirmar Compra", command=confirmarCompra)
        botonConfirmarCompra.pack(pady=5)

        carrito = ttk.Treeview(ventanaDatosManga, columns=("Manga", "Volumen", "Cantidad"), show="headings")
        carrito.heading("Manga", text="Manga")
        carrito.heading("Volumen", text="Volumen")
        carrito.heading("Cantidad", text="Cantidad")
        carrito.pack(pady=10)

        def dobleClickEliminar(event):
            item = carrito.selection()  
            if item:                   
                carrito.delete(item)   
            else:
                messagebox.showwarning("Selecionar fila")

        carrito.bind("<Double-1>", dobleClickEliminar)
        
        ventanaDatosManga.protocol("WM_DELETE_WINDOW", cerrar_todo)




    botonConfirmarIdentificadores = tk.Button(ventanaVender, text="Confirmar", command=datosManga)
    botonConfirmarIdentificadores.pack(pady=5)

    

    

    

    


def mostrarTablasActualizar():
    ventanaActualizarTablas = tk.Tk()
    ventanaActualizarTablas.title("Seleccionar: ")

    botonManga = tk.Button(ventanaActualizarTablas, text="Manga", command=actualizarManga)
    botonManga.pack(pady=5)

    botonVolume = tk.Button(ventanaActualizarTablas, text="Volume", command=actualizarVolume)
    botonVolume.pack(pady=5)

def insertarManga():
    # Crear ventana para ingresar datos del manga
    ventanaManga = tk.Tk()
    ventanaManga.title("Insertar Manga")

    labelMangaName = tk.Label(ventanaManga, text="Nombre del Manga:")
    labelMangaName.pack(pady=5)
    entryMangaName = tk.Entry(ventanaManga)
    entryMangaName.pack(pady=5)

    labelAuthorName = tk.Label(ventanaManga, text="Nombre del Autor:")
    labelAuthorName.pack(pady=5)
    entryAuthorName = tk.Entry(ventanaManga)
    entryAuthorName.pack(pady=5)

    labelGenre = tk.Label(ventanaManga, text="Genero:")
    labelGenre.pack(pady=5)
    entryGenre = tk.Entry(ventanaManga)
    entryGenre.pack(pady=5)

    labelPublishDate = tk.Label(ventanaManga, text="Fecha de Publicacion (YYYY-MM-DD):")
    labelPublishDate.pack(pady=5)
    entryPublishDate = tk.Entry(ventanaManga)
    entryPublishDate.pack(pady=5)

    # Boton para insertar
    def insertar():
        manga_name = entryMangaName.get()
        author_name = entryAuthorName.get()
        genre = entryGenre.get()
        publish_date = entryPublishDate.get()

        query = f"INSERT INTO Manga (Manga_name, Author_name, Genre, Publish_date, Modified_date) VALUES ('{manga_name}', '{author_name}', '{genre}', '{publish_date}', GETDATE())"
        try:
            conn = get_connection("VendedorLogin", "123")
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            messagebox.showinfo("Exito", "Manga insertado correctamente.")
            cursor.close()
            conn.close()
            #ventanaManga.quit()  # Cerrar ventana despues de insertar
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo insertar el manga: {str(e)}")

    botonInsertar = tk.Button(ventanaManga, text="Insertar", command=insertar)
    botonInsertar.pack(pady=20)

def insertarVolume():
    # Crear ventana para ingresar datos del volumen
    ventanaVolume = tk.Tk()
    ventanaVolume.title("Insertar Volume")

    # Campos para recibir la informacion
    labelVolumeNro = tk.Label(ventanaVolume, text="Numero de Volumen:")
    labelVolumeNro.pack(pady=5)
    entryVolumeNro = tk.Entry(ventanaVolume)
    entryVolumeNro.pack(pady=5)

    labelReleaseDate = tk.Label(ventanaVolume, text="Fecha de Lanzamiento (YYYY-MM-DD):")
    labelReleaseDate.pack(pady=5)
    entryReleaseDate = tk.Entry(ventanaVolume)
    entryReleaseDate.pack(pady=5)

    labelPrice = tk.Label(ventanaVolume, text="Precio:")
    labelPrice.pack(pady=5)
    entryPrice = tk.Entry(ventanaVolume)
    entryPrice.pack(pady=5)

    labelStock = tk.Label(ventanaVolume, text="Stock:")
    labelStock.pack(pady=5)
    entryStock = tk.Entry(ventanaVolume)
    entryStock.pack(pady=5)

    labelIdManga = tk.Label(ventanaVolume, text="ID del Manga:")
    labelIdManga.pack(pady=5)
    entryIdManga = tk.Entry(ventanaVolume)
    entryIdManga.pack(pady=5)

    # Boton para insertar
    def insertar():
        volume_nro = entryVolumeNro.get()
        release_date = entryReleaseDate.get()
        price = entryPrice.get()
        stock = entryStock.get()
        id_manga = entryIdManga.get()

        query = f"INSERT INTO Volume (Volume_nro, Release_date, Price, Stock, Id_Manga) VALUES ({volume_nro}, '{release_date}', {price}, {stock}, {id_manga})"
        try:
            conn = get_connection("VendedorLogin", "123")
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            messagebox.showinfo("Éxito", "Volume insertado correctamente.")
            cursor.close()
            conn.close()
            #ventanaVolume.quit()  # Cerrar ventana despues de insertar
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo insertar el volume: {str(e)}")

    botonInsertar = tk.Button(ventanaVolume, text="Insertar", command=insertar)
    botonInsertar.pack(pady=20)

'''
def insertarSales():
    # Crear ventana para ingresar datos de la venta
    ventanaSales = tk.Tk()
    ventanaSales.title("Insertar Sales")

    # Campos para recibir la informacion
    labelIdSales = tk.Label(ventanaSales, text="ID de Venta:")
    labelIdSales.pack(pady=5)
    entryIdSales = tk.Entry(ventanaSales)
    entryIdSales.pack(pady=5)

    labelIdVolume = tk.Label(ventanaSales, text="ID del Volume:")
    labelIdVolume.pack(pady=5)
    entryIdVolume = tk.Entry(ventanaSales)
    entryIdVolume.pack(pady=5)

    labelQuantity = tk.Label(ventanaSales, text="Cantidad:")
    labelQuantity.pack(pady=5)
    entryQuantity = tk.Entry(ventanaSales)
    entryQuantity.pack(pady=5)

    # Boton para insertar
    def insertar():
        id_sales = entryIdSales.get()
        id_volume = entryIdVolume.get()
        quantity = entryQuantity.get()

        query = f"INSERT INTO Sales (Id_Sales, Id_Volume, Quantity) VALUES ({id_sales}, {id_volume}, {quantity})"
        try:
            conn = get_connection("VendedorLogin", "123")
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            messagebox.showinfo("Exito", "Sale insertado correctamente.")
            cursor.close()
            conn.close()
            #ventanaSales.quit()  # Cerrar ventana despues de insertar
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo insertar la venta: {str(e)}")

    botonInsertar = tk.Button(ventanaSales, text="Insertar", command=insertar)
    botonInsertar.pack(pady=20)
'''

'''
def insertarSalesDetails():
    # Crear ventana para ingresar detalles de la venta
    ventanaSalesDetails = tk.Tk()
    ventanaSalesDetails.title("Insertar Sales Details")

    # Campos para recibir la informacion
    labelIdCustomer = tk.Label(ventanaSalesDetails, text="ID del Cliente:")
    labelIdCustomer.pack(pady=5)
    entryIdCustomer = tk.Entry(ventanaSalesDetails)
    entryIdCustomer.pack(pady=5)

    labelIdEmployee = tk.Label(ventanaSalesDetails, text="ID del Empleado:")
    labelIdEmployee.pack(pady=5)
    entryIdEmployee = tk.Entry(ventanaSalesDetails)
    entryIdEmployee.pack(pady=5)

    labelSalesDate = tk.Label(ventanaSalesDetails, text="Fecha de Venta (YYYY-MM-DD):")
    labelSalesDate.pack(pady=5)
    entrySalesDate = tk.Entry(ventanaSalesDetails)
    entrySalesDate.pack(pady=5)

    labelTotalPrice = tk.Label(ventanaSalesDetails, text="Precio Total:")
    labelTotalPrice.pack(pady=5)
    entryTotalPrice = tk.Entry(ventanaSalesDetails)
    entryTotalPrice.pack(pady=5)

    # Boton para insertar
    def insertar():
        id_customer = entryIdCustomer.get()
        id_employee = entryIdEmployee.get()
        sales_date = entrySalesDate.get()
        total_price = entryTotalPrice.get()

        query = f"INSERT INTO Sales_Details (Id_Customer, Id_Employee, Sales_date, Total_price) VALUES ({id_customer}, {id_employee}, '{sales_date}', {total_price})"
        try:
            conn = get_connection("VendedorLogin", "123")
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            messagebox.showinfo("Exito", "Sales Details insertado correctamente.")
            cursor.close()
            conn.close()
            #ventanaSalesDetails.quit()  # Cerrar ventana despues de insertar
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo insertar el detalle de venta: {str(e)}")

    botonInsertar = tk.Button(ventanaSalesDetails, text="Insertar", command=insertar)
    botonInsertar.pack(pady=20)
'''

def insertarCustomer():
    # Crear ventana para ingresar datos del cliente
    ventanaCustomer = tk.Tk()
    ventanaCustomer.title("Insertar Customer")

    # Campos para recibir la informacion
    labelCustomerName = tk.Label(ventanaCustomer, text="Nombre del Cliente:")
    labelCustomerName.pack(pady=5)
    entryCustomerName = tk.Entry(ventanaCustomer)
    entryCustomerName.pack(pady=5)

    labelFirstSurname = tk.Label(ventanaCustomer, text="Primer Apellido:")
    labelFirstSurname.pack(pady=5)
    entryFirstSurname = tk.Entry(ventanaCustomer)
    entryFirstSurname.pack(pady=5)

    labelSecondSurname = tk.Label(ventanaCustomer, text="Segundo Apellido:")
    labelSecondSurname.pack(pady=5)
    entrySecondSurname = tk.Entry(ventanaCustomer)
    entrySecondSurname.pack(pady=5)

    labelNIT = tk.Label(ventanaCustomer, text="NIT:")
    labelNIT.pack(pady=5)
    entryNIT = tk.Entry(ventanaCustomer)
    entryNIT.pack(pady=5)

    labelEmail = tk.Label(ventanaCustomer, text="Correo Electronico:")
    labelEmail.pack(pady=5)
    entryEmail = tk.Entry(ventanaCustomer)
    entryEmail.pack(pady=5)

    labelBirthday = tk.Label(ventanaCustomer, text="Fecha de Nacimiento (YYYY-MM-DD):")
    labelBirthday.pack(pady=5)
    entryBirthday = tk.Entry(ventanaCustomer)
    entryBirthday.pack(pady=5)

    # Boton para insertar
    def insertar():
        customer_name = entryCustomerName.get()
        first_surname = entryFirstSurname.get()
        second_surname = entrySecondSurname.get()
        nit = entryNIT.get()
        email = entryEmail.get()
        birthday = entryBirthday.get()

        query = f"INSERT INTO Customer (Customer_name, Customer_first_surname, Customer_second_surname, NIT, Email, Customer_birthday) VALUES ('{customer_name}', '{first_surname}', '{second_surname}', '{nit}', '{email}', '{birthday}')"
        try:
            conn = get_connection("VendedorLogin", "123")
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            messagebox.showinfo("Exito", "Cliente insertado correctamente.")
            cursor.close()
            conn.close()
            #ventanaCustomer.quit()  # Cerrar ventana despues de insertar
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo insertar el cliente: {str(e)}")

    botonInsertar = tk.Button(ventanaCustomer, text="Insertar", command=insertar)
    botonInsertar.pack(pady=20)

def actualizarManga():
    # Crear ventana para ingresar datos de actualizacion de Manga
    ventanaActualizarManga = tk.Tk()
    ventanaActualizarManga.title("Actualizar Manga")

    # Campos para recibir la informacion
    labelID = tk.Label(ventanaActualizarManga, text="ID del Manga:")
    labelID.pack(pady=5)
    entryID = tk.Entry(ventanaActualizarManga)
    entryID.pack(pady=5)

    labelColumn = tk.Label(ventanaActualizarManga, text="Columna a actualizar:")
    labelColumn.pack(pady=5)
    entryColumn = tk.Entry(ventanaActualizarManga)
    entryColumn.pack(pady=5)

    labelNewData = tk.Label(ventanaActualizarManga, text="Nuevo dato:")
    labelNewData.pack(pady=5)
    entryNewData = tk.Entry(ventanaActualizarManga)
    entryNewData.pack(pady=5)

    # Boton para actualizar
    def actualizar():
        manga_id = entryID.get()
        column = entryColumn.get()
        new_data = entryNewData.get()

        query = f"UPDATE Manga SET {column} = ? WHERE Id_Manga = ?"

        try:
            conn = get_connection("VendedorLogin", "123")
            cursor = conn.cursor()
            cursor.execute(query, (new_data, manga_id))
            conn.commit()
            messagebox.showinfo("Exito", "Manga actualizado correctamente.")
            cursor.close()
            conn.close()
            #ventanaActualizarManga.quit()  # Cerrar ventana despues de actualizar
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo actualizar el manga: {str(e)}")

    botonActualizar = tk.Button(ventanaActualizarManga, text="Actualizar", command=actualizar)
    botonActualizar.pack(pady=20)

def actualizarVolume():
    # Crear ventana para ingresar datos de actualizacion de Volume
    ventanaActualizarVolume = tk.Tk()
    ventanaActualizarVolume.title("Actualizar Volume")

    # Campos para recibir la informacion
    labelID = tk.Label(ventanaActualizarVolume, text="ID del Volume:")
    labelID.pack(pady=5)
    entryID = tk.Entry(ventanaActualizarVolume)
    entryID.pack(pady=5)

    labelColumn = tk.Label(ventanaActualizarVolume, text="Columna a actualizar:")
    labelColumn.pack(pady=5)
    entryColumn = tk.Entry(ventanaActualizarVolume)
    entryColumn.pack(pady=5)

    labelNewData = tk.Label(ventanaActualizarVolume, text="Nuevo dato:")
    labelNewData.pack(pady=5)
    entryNewData = tk.Entry(ventanaActualizarVolume)
    entryNewData.pack(pady=5)

    # Boton para actualizar
    def actualizar():
        volume_id = entryID.get()
        column = entryColumn.get()
        new_data = entryNewData.get()

        query = f"UPDATE Volume SET {column} = ? WHERE Id_Volume = ?"
        try:
            conn = get_connection("VendedorLogin", "123")
            cursor = conn.cursor()
            cursor.execute(query, (new_data, volume_id))
            conn.commit()
            messagebox.showinfo("Exito", "Volume actualizado correctamente.")
            cursor.close()
            conn.close()
            #ventanaActualizarVolume.quit()  # Cerrar ventana despues de actualizar
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo actualizar el volumen: {str(e)}")

    botonActualizar = tk.Button(ventanaActualizarVolume, text="Actualizar", command=actualizar)
    botonActualizar.pack(pady=20)



# Table column mapping
TABLE_COLUMNS = {
    "MANGA": ["Id_Manga", "Manga_name", "Author_name", "Genre", "Publish_date", "Modified_date"],
    "VOLUME": ["Id_Volume", "Volume_nro", "Release_date", "Price", "Stock", "Id_Manga", "Modified_date"],
    "SALES": ["Id_Sales", "Id_Volume", "Quantity", "Modified_date"],
    "CUSTOMER": [
        "Id_Customer", "Customer_name", "Customer_first_surname", 
        "Customer_second_surname", "NIT", "Email", 
        "Customer_birthday", "Modified_date"
    ],
    "EMPLOYEE": [
        "Id_Employee", "Employee_name", "Employee_first_surname",
        "Employee_second_surname", "Wage", "Hired_date",
        "Email", "Phone_number", "Modified_date"
    ],
    "SALES_DETAILS": [
        "Id_Sales", "Id_Customer", "Id_Employee", 
        "Sales_date", "Total_price", "Modified_date"],
}

def add_data_to_table_SALES(table_name, select_window):
    #Elimina la ventana en la que se muestran las tablas
    select_window.destroy()
    add_window = tk.Tk()
    add_window.title(f"Add Data to {table_name}")
    #lista de las columnas de table_name
    fields = TABLE_COLUMNS[table_name]
    #Variable que almacena las entras del usuario, para anadir posteiormente
    entries = {}
    #for loop para crear las entry para el input del usuario
    #[:-1] no toma encuenta la ultima columna(modified_date)
    for field in fields[:-1]:
        #Label es una etiqueta/texto
        label = tk.Label(add_window, text=field)
        label.pack(pady=5)
        #.Entry() es donde se inserta los datos
        entry = tk.Entry(add_window)
        entry.pack(pady=5)
        #para cada field/column, se asigna el input que ingreso previamente el usuario
        entries[field] = entry
    
    def confirm_addition():
        conn = get_connection("DBALogin", "12345")
        cursor = conn.cursor()

        # Build the query dynamically
        #Joins une cada columa pero las separa por ', ' Une cada item de un tuple en una string
        columns = ", ".join(fields[:-1])
        #Crea un string de "?" en base al numero de columnas
        placeholders = ", ".join(["?"] * (len(fields) - 1))
        #Retrae los valores incresados previamente usando get() por cada columna
        values = [entries[field].get() for field in fields[:-1]]
        #Asegura que no se deje espacios vacios
        if not entries[field].get():
            messagebox.showinfo("ERROR", "Cannot leave empty data!")
            add_window.destroy()
            return

        try:
            #Inserta los valores de la variable values
            cursor.execute(f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})", values)
            conn.commit()
            messagebox.showinfo("Success", f"Data added to {table_name} successfully!")
        except pyodbc.IntegrityError as e:
            #Busca si hay un duplicado de llaves
            # Check for duplicate key error
            # Check for PRIMARY KEY in e 
            if "PRIMARY KEY" in str(e):
                messagebox.showerror("Error", "Duplicate ID detected! Please enter a unique ID.")
            else:
                # Handle other integrity errors
                messagebox.showerror("Error", f"An integrity error occurred: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
        finally:
            conn.close() 
            add_window.destroy()

    add_button_confirm = tk.Button(add_window, text="Confirm Addition", command=confirm_addition)
    add_button_confirm.pack(pady=10)
        

# Add data to the table
def add_data_to_table(table_name, del_window):
    del_window.destroy()
    add_window = tk.Tk()
    add_window.title(f"Add Data to {table_name}")
    
    fields = TABLE_COLUMNS[table_name]
    entries = {}

    # Create entry fields for each column, fields are the columns of table_name
    #[1:] is to take all except the first
    #[:-1] es para no tomar el ultimo valor
    for field in fields[1:-1]:
        label = tk.Label(add_window, text=field)
        label.pack(pady=5)
        entry = tk.Entry(add_window)
        entry.pack(pady=5)
        entries[field] = entry
        
    # Confirm addition button
    def confirm_addition():
        conn = get_connection("DBALogin", "12345")
        cursor = conn.cursor()

        # Build the query dynamically
        columns = ", ".join(fields[1:-1])
        #-2 para omitir dos column
        placeholders = ", ".join(["?"] * (len(fields) - 2))
        values = [entries[field].get() for field in fields[1:-1]]
        
        if not entries[field].get():
            messagebox.showinfo("ERROR", "Cannot leave empty data!")
            add_window.destroy()
            return

        try:
            cursor.execute(f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})", values)
            conn.commit()
            messagebox.showinfo("Success", f"Data added to {table_name} successfully!")
        except pyodbc.IntegrityError as e:
            # Check for duplicate key error
            # Check for PRIMARY KEY in e, 
            if "PRIMARY KEY" in str(e):
                messagebox.showerror("Error", "Duplicate ID detected! Please enter a unique ID.")
            else:
                # Handle other integrity errors
                messagebox.showerror("Error", f"An integrity error occurred: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
        finally:
            conn.close() 
            add_window.destroy()

    add_button = tk.Button(add_window, text="Confirm Addition", command=confirm_addition)
    add_button.pack(pady=10)

# Visualize data from the table
def visualize_table_data(table_name):
    conn = get_connection("DBALogin", "12345")
    cursor = conn.cursor()

    try:
        #Seleciona todas la data
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
    	#Creacion de ventana
        visualize_window = tk.Tk()
        visualize_window.title(f"Data in {table_name}")
        #Variable que almacena las columna de table_name
        columns_table_name = TABLE_COLUMNS[table_name]
        #Treeview(window, columns, show)
        #window es donde se muestra la tabla, columns es el nombre de las columnas
        #show es para mostrar las columns
        tree = ttk.Treeview(visualize_window, columns=columns_table_name, show="headings")
        #For loop para el display de la data
        for col in columns_table_name:
            #encabezado de las columns, sus nombre
            tree.heading(col, text=col)
            #el ancho de cada columna
            tree.column(col, width=100)
        #For loop para el display de las filas
        for row in rows:
            #limpia los datos antes de ser ingresados
            clean_row = tuple(map(str, row))
            #Inserta las tuplas una por una
            #tk.END indica que las tuplas deben insertarce una despues de otra
            #values es los datos a insertar
            #"" indica que no necesitamos jerarquias
            tree.insert("", tk.END, values=clean_row)
        #fill=tk.BOTH is to occupy all the available space
        #expand=True is to adjust to the size of the window
        tree.pack(fill=tk.BOTH, expand=True)

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
    finally:
        #Cerra coneccion
        conn.close()

# Delete data from the table
#WORKING ON THIS DELETE FUNCTION FOR SALES TABLE
#CHECK OUT THE COMMAND ON SELECT_TABLE_DELETE
def delete_data_SALES(table_name, select_window):
    select_window.destroy()
    #Crear ventana
    delete_window = tk.Tk()
    delete_window.title(f"Delete Data from {table_name}")
    
    #Label/mensage/texto
    label1 = tk.Label(delete_window, text=f"Enter Id_Sales to delete:")
    label1.pack(pady=5)
    #Entry para la entra del id_sales
    id_sales_entry = tk.Entry(delete_window)
    id_sales_entry.pack(pady=5)

    label2 = tk.Label(delete_window, text=f"Enter Id_Volume to delete:")
    label2.pack(pady=5)
    #Entrt para la entrad del id_volume
    id_volume_entry = tk.Entry(delete_window)
    id_volume_entry.pack(pady=5)
    
    def confirm_deletion():
        conn = get_connection("DBALogin", "12345")
        cursor = conn.cursor()
        #retraer la informacion usando get()
        id_sales_value = id_sales_entry.get()
        id_volume_value = id_volume_entry.get()

        try:
            cursor.execute(f"DELETE FROM {table_name} WHERE Id_Sales = ? AND Id_Volume = ?", (id_sales_value, id_volume_value))
            conn.commit()
            #Cuenta las filas afectadas, si es mayor a 0, entonces el codigo fue un exito
            if cursor.rowcount > 0:
                messagebox.showinfo("Success", f"Row deleted Successfully!")
            else:
                messagebox.showerror("Error", f"No Id_Sales = {id_sales_value} or Id_Volume = {id_volume_value} found!")
        except Exception as e:
            messagebox.showerror("Error", f"An error ocurred: {e}")
        finally:
            conn.close()
            delete_window.destroy()
    
    delete_button = tk.Button(delete_window, text="Confirm Deletion", command=confirm_deletion)
    delete_button.pack(pady=10)

def delete_data_from_table(table_name, select_window):
    select_window.destroy()
    delete_window = tk.Tk()
    delete_window.title(f"Delete Data from {table_name}")
    #Solo obtiene la primera columna, el Id
    id_column = TABLE_COLUMNS[table_name][0]  # Assuming the first column is the ID
    label = tk.Label(delete_window, text=f"Enter {id_column} to delete:")
    label.pack(pady=5)

    id_entry = tk.Entry(delete_window)
    id_entry.pack(pady=5)

    def confirm_deletion():
        conn = get_connection("DBALogin", "12345")
        cursor = conn.cursor()
        #Usamos get() para obtener el valo incresados del id por el usuario previamente
        id_value = id_entry.get()

        try:
            cursor.execute(f"DELETE FROM {table_name} WHERE {id_column} = ?", id_value)
            conn.commit()
            #After deleting, rowcount is the number of rows affected or deleted
            if cursor.rowcount > 0:
                messagebox.showinfo("Success", f"Row with {id_column} = {id_value} deleted successfully!")
            else:
                messagebox.showinfo("Info", f"No row found with {id_column} = {id_value}.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
        finally:
            conn.close()
            delete_window.destroy()

    delete_button = tk.Button(delete_window, text="Confirm Deletion", command=confirm_deletion)
    delete_button.pack(pady=10)

#Crea las opciones de tablas en donde anadir los datos
def add_select_table():
    select_window = tk.Tk()
    select_window.title("Select Table to Add Data")
    #For loop para la creacion de un boton por tabla
    #Si la funcion a llamar en command tiene argumentos, usar lambda:
    #t=table_name asegura manejar la tabla correcta
    #table_name = Nombre de la tabla
    for table_name in TABLE_COLUMNS.keys():
        if table_name == "SALES":
            button = tk.Button(select_window, text=table_name, command=lambda t=table_name: add_data_to_table_SALES(t, select_window))
            button.pack(pady=5)
        else:
            button = tk.Button(select_window, text=table_name, command=lambda t=table_name: add_data_to_table(t, select_window))
            button.pack(pady=5)


# Select table for visualizing data
def visualize_select_table():
    #Crear venta
    select_window = tk.Tk()
    select_window.title("Select Table to Visualize Data")
    #Crear botones para cadad tabla
    for table_name in TABLE_COLUMNS.keys():
        button = tk.Button(select_window, text=table_name, command=lambda t=table_name: visualize_table_data(t))
        button.pack(pady=5)


# Select table for deleting data
def delete_select_table():
    select_window = tk.Tk()
    select_window.title("Select Table to Delete Data")

    for table_name in TABLE_COLUMNS.keys():
        if table_name == "SALES":
            button = tk.Button(select_window, text=table_name, command=lambda t=table_name: delete_data_SALES(t, select_window))
            button.pack(pady=5)
        else:
            button = tk.Button(select_window, text=table_name, command=lambda t=table_name: delete_data_from_table(t, select_window))
            button.pack(pady=5)

#MODIFY FUNCTS
def modify_data(table_name, select_window):
    select_window.destroy()
    #Creacion de ventana donde trabajar
    modify_data_window = tk.Tk()
    modify_data_window.title(f"Modify Data from {table_name}")

    label_Id = tk.Label(modify_data_window, text="ID")
    label_Id.pack(pady=5)
    #Entry para el id/fila
    Id_entry = tk.Entry(modify_data_window)
    Id_entry.pack(pady=5)

    label_column = tk.Label(modify_data_window, text="Column")
    label_column.pack(pady=5)
    #Entry para la column
    column_entry = tk.Entry(modify_data_window)
    column_entry.pack(pady=5)

    label_new_data = tk.Label(modify_data_window, text="New Data")
    label_new_data.pack(pady=5)
    #Entry para la nueva data
    new_data_entry = tk.Entry(modify_data_window)
    new_data_entry.pack(pady=5)

    def confirm_modification():
        #Usar get() para obtener la informacion guardada previamente
        id_value = Id_entry.get()
        column_value = column_entry.get()
        new_data_value = new_data_entry.get()
        #No dejar espacio vacio
        if not id_value or not column_value or not new_data_value:
            messagebox.showerror("Error", "Must fill in all values!")
            return
        
        conn = get_connection("DBALogin", "12345")
        cursor = conn.cursor()

        try:
            cursor.execute(f"UPDATE {table_name} SET [{column_value}] = ? WHERE Id_{table_name} = ?", (new_data_value, id_value))
            conn.commit()
            #Verificar que el .execute() fue un exito
            if cursor.rowcount == 0:
                messagebox.showerror("Error", f"No rows found with Id_{table_name} = {id_value}")
            else:
                messagebox.showinfo("Success", f"Successfully updated: {new_data_value}")
            
        except Exception as e:
            messagebox.showerror("Error", f"An error ocurred: {e}")

        finally:
            conn.close()
            modify_data_window.destroy()

    confirm_button = tk.Button(modify_data_window, text="Confirm Modification", command=confirm_modification)
    confirm_button.pack(pady=5)


#Creacion de botones para que el usuario escoja la tabla
def modify_select_table():
    select_window = tk.Tk()
    select_window.title("Select Table to Modify Data")
    #check if t=table_name is necessary
    for table_name in TABLE_COLUMNS.keys():
        button = tk.Button(select_window, text=table_name, command=lambda t=table_name: modify_data(t, select_window))
        button.pack(pady=5)