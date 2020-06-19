import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import messagebox
from tkinter import scrolledtext as st
import SeguridadBD

class SeguridadSocial:
    def __init__(self):
        self.seguridad=SeguridadBD.Seguridad()
        self.ventana1=tk.Tk()
        self.ventana1.title("Seguridad social")
        self.cuaderno1 = ttk.Notebook(self.ventana1)   
        self.CargarDatos()
        self.Consultar()
        self.Modificar()
        self.numero = tk.StringVar()
        #self.consulta_por_codigo()
        #self.listado_completo()
        self.cuaderno1.grid(column=0, row=0, padx=10, pady=10)
        self.ventana1.mainloop()
        
    def CargarDatos(self):
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Registro")
        self.labelframe1=ttk.LabelFrame(self.pagina1, text="Registrar")  
        self.labelframe1.grid(column=0, row=0, padx=0, pady=10)

        #Identificacion
        self.labelIdentificacion=ttk.Label(self.labelframe1, text="Identificación:")
        self.labelIdentificacion.grid(column=0, row=0, padx=0, pady=4)
        self.identificacion=tk.StringVar()
        self.InputIdentificacion=ttk.Entry(self.labelframe1, textvariable=self.identificacion)
        self.InputIdentificacion.grid(column=1, row=0, padx=0, pady=4)
        
        #Nombres
        self.Nombres=ttk.Label(self.labelframe1, text="Nombres:")        
        self.Nombres.grid(column=0, row=1, padx=0, pady=4)
        self.nombres=tk.StringVar()
        self.InputNombres=ttk.Entry(self.labelframe1, textvariable=self.nombres)
        self.InputNombres.grid(column=1, row=1, padx=0, pady=4)
        
        #Apellidos
        self.Apellidos=ttk.Label(self.labelframe1, text="Apellidos:")        
        self.Apellidos.grid(column=0, row=2, padx=0, pady=4)
        self.apellidos=tk.StringVar()
        self.InputApellidos=ttk.Entry(self.labelframe1, textvariable=self.apellidos)
        self.InputApellidos.grid(column=1, row=2, padx=0, pady=4)
        
        #Salud
        self.Salud=ttk.Label(self.labelframe1, text="Salud:")        
        self.Salud.grid(column=0, row=3, padx=0, pady=4)
        self.salud=tk.StringVar()
        self.InputSalud=ttk.Entry(self.labelframe1, textvariable=self.salud)
        self.InputSalud.grid(column=1, row=3, padx=0, pady=4)
        
        #Pension
        self.Pension=ttk.Label(self.labelframe1, text="Pension:")        
        self.Pension.grid(column=0, row=4, padx=0, pady=4)
        self.pension=tk.StringVar()
        self.InputPension=ttk.Entry(self.labelframe1, textvariable=self.pension)
        self.InputPension.grid(column=1, row=4, padx=0, pady=4)
        
        #Riesgos laborales
        self.RiesgoL=ttk.Label(self.labelframe1, text="Riesgos laborales:")        
        self.RiesgoL.grid(column=0, row=5, padx=0, pady=4)
        self.riesgoL=tk.StringVar()
        self.InputRiesgoL=ttk.Entry(self.labelframe1, textvariable=self.riesgoL)
        self.InputRiesgoL.grid(column=1, row=5, padx=0, pady=4)
        
        
        #Caja de compensacion
        self.CajaC=ttk.Label(self.labelframe1, text="Caja de compensación:")        
        self.CajaC.grid(column=0, row=6, padx=4, pady=4)
        self.cajaC=tk.StringVar()
        self.InputCajaC=ttk.Entry(self.labelframe1, textvariable=self.cajaC)
        self.InputCajaC.grid(column=1, row=6, padx=4, pady=4)
        
        
        self.boton1=ttk.Button(self.labelframe1, text="Agregar", command=self.AgregarRegistro)#command=self.agregar)
        self.boton1.grid(column=1, row=7, padx=4, pady=4)
        
        
    def Consultar(self):
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="Consulta")
        
        self.labelframe1=ttk.LabelFrame(self.pagina2, text="Buscar")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        
        #Buscar
        self.Id=ttk.Label(self.labelframe1, text="Identificación:")        
        self.Id.grid(column=0, row=1, padx=4, pady=4)
        self.identificador=tk.StringVar()  
        self.InputId=ttk.Entry(self.labelframe1, textvariable=self.identificador)
        self.InputId.grid(column=0, row=2, padx=4, pady=4)
        self.boton1=ttk.Button(self.labelframe1, text="Consultar",command=self.ConsultarRegistro)#, command=self.listar)
        self.boton1.grid(column=0, row=3, padx=4, pady=4)
        
        self.boton1=ttk.Button(self.labelframe1, text="Listado completo", command=self.ListarRegistros)#, command=self.listar)
        self.boton1.grid(column=0, row=4, padx=4, pady=4)
        
        self.scrolledtext=st.ScrolledText(self.labelframe1, width=50, height=10)
        self.scrolledtext.grid(column=0,row=5, padx=10, pady=10)
           
    
    def Modificar(self):
        self.pagina3 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3, text="Modificar")
        
        self.labelframe1=ttk.LabelFrame(self.pagina3, text="Modificar")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        
        #Buscar
        self.Id=ttk.Label(self.labelframe1, text="Identificación:")        
        self.Id.grid(column=0, row=1, padx=4, pady=4)
        self.id=tk.StringVar()
        self.InputId=ttk.Entry(self.labelframe1, textvariable=self.id)
        self.InputId.grid(column=1, row=1, padx=4, pady=4)
        
        
        self.boton1=ttk.Button(self.labelframe1, text="Modificar",command=self.EditarRegistros)#, command=self.listar)
        self.boton1.grid(column=0, row=2, padx=4, pady=4)
        
        #Identificacion
        self.labelIdentificacion=ttk.Label(self.labelframe1, text="Identificación:")
        self.labelIdentificacion.grid(column=0, row=3, padx=4, pady=4)
        self.identificacionM=tk.StringVar()
        self.InputIdentificacion=ttk.Entry(self.labelframe1, textvariable=self.identificacionM)
        self.InputIdentificacion.grid(column=1, row=3, padx=4, pady=4)
        
        #Nombres
        self.Nombres=ttk.Label(self.labelframe1, text="Nombres:")        
        self.Nombres.grid(column=0, row=4, padx=4, pady=4)
        self.nombresM=tk.StringVar()
        self.InputNombres=ttk.Entry(self.labelframe1, textvariable=self.nombresM)
        self.InputNombres.grid(column=1, row=4, padx=4, pady=4)
        
        #Apellidos
        self.Apellidos=ttk.Label(self.labelframe1, text="Apellidos:")        
        self.Apellidos.grid(column=0, row=5, padx=4, pady=4)
        self.apellidosM=tk.StringVar()
        self.InputApellidos=ttk.Entry(self.labelframe1, textvariable=self.apellidosM)
        self.InputApellidos.grid(column=1, row=5, padx=4, pady=4)
        
        #Salud
        self.Salud=ttk.Label(self.labelframe1, text="Salud:")        
        self.Salud.grid(column=0, row=6, padx=4, pady=4)
        self.saludM=tk.StringVar()
        self.InputSalud=ttk.Entry(self.labelframe1, textvariable=self.saludM)
        self.InputSalud.grid(column=1, row=6, padx=4, pady=4)
        
        #Pension
        self.Pension=ttk.Label(self.labelframe1, text="Pension:")        
        self.Pension.grid(column=0, row=7, padx=4, pady=4)
        self.pensionM=tk.StringVar()
        self.InputPension=ttk.Entry(self.labelframe1, textvariable=self.pensionM)
        self.InputPension.grid(column=1, row=7, padx=4, pady=4)
        
        #Riesgos laborales
        self.RiesgoL=ttk.Label(self.labelframe1, text="Pension:")        
        self.RiesgoL.grid(column=0, row=8, padx=4, pady=4)
        self.riesgoLM=tk.StringVar()
        self.InputRiesgoL=ttk.Entry(self.labelframe1, textvariable=self.riesgoLM)
        self.InputRiesgoL.grid(column=1, row=8, padx=4, pady=4)
        
        
        #Caja de compensacion
        self.CajaC=ttk.Label(self.labelframe1, text="Pension:")        
        self.CajaC.grid(column=0, row=9, padx=4, pady=4)
        self.cajaCM=tk.StringVar()
        self.InputCajaC=ttk.Entry(self.labelframe1, textvariable=self.cajaCM)
        self.InputCajaC.grid(column=1, row=9, padx=4, pady=4)
        
        
        self.boton1=ttk.Button(self.labelframe1, text="Guardar Cambios", command=self.GuardarCambios)#command=self.agregar)
        self.boton1.grid(column=1, row=10, padx=4, pady=4)







    def AgregarRegistro(self):
        if(self.identificacion.get() == "" or self.nombres.get() == "" or self.apellidos.get()=="" or self.salud.get()=="" or self.pension.get() =="" or self.riesgoL.get() ==""or self.cajaC.get() ==""):
            messagebox.showwarning("Dato vacio","Por favor no deje campos vacios");
        else:
            if(self.identificacion.get().isdigit()):
                datos = (self.identificacion.get(),self.nombres.get(),self.apellidos.get(),self.salud.get(),self.pension.get(),self.riesgoL.get(),self.cajaC.get())
                a = self.seguridad.agregar(datos)
                if(a):
                    messagebox.showinfo("Registrado","Registro guardado exitosamente")
                    self.identificacion.set("")
                    self.nombres.set("")
                    self.apellidos.set("")
                    self.salud.set("")
                    self.pension.set("")
                    self.cajaC.set("")
                    self.riesgoL.set("")
            else:
                messagebox.showwarning("Dato no valido","Ingrese un numero de identificacion valido(numerico)");
        
    def ConsultarRegistro(self):
        if(self.identificador.get() == ""):
            messagebox.showwarning("Dato vacio","Por favor escriba un numero de identificación");
        else:
            if(self.identificador.get().isdigit()):
                iden = (self.identificador.get(),)
                self.scrolledtext.delete("1.0", tk.END)
                registro = self.seguridad.ConsultarR(iden)
                
                if(len(registro) > 0):
                    self.scrolledtext.insert(tk.END,"DATOS DEL USUARIO\n")
                    for dato in registro:
                        self.scrolledtext.insert(tk.END,"Identificación: "+str(dato[0])+"\n")
                        self.scrolledtext.insert(tk.END,"Nombres: "+str(dato[1])+"\n")
                        self.scrolledtext.insert(tk.END,"Apellidos: "+str(dato[2])+"\n")
                        self.scrolledtext.insert(tk.END,"Salud: "+str(dato[3])+"\n")
                        self.scrolledtext.insert(tk.END,"Pensión: "+str(dato[4])+"\n")
                        self.scrolledtext.insert(tk.END,"Riesgos Laborales: "+str(dato[5])+"\n")
                        self.scrolledtext.insert(tk.END,"Caja de compensación: "+str(dato[6]))
                else:
                    messagebox.showinfo("No registrado","No hay registros con ese numero de identificación")
            else:
                messagebox.showwarning("Dato vacio","Por favor escriba un numero de identificación valido");
                        
    def ListarRegistros(self):
        datos = self.seguridad.ListarRegistros()
        self.scrolledtext.delete("1.0", tk.END)
        if(len(datos) > 0):
            self.scrolledtext.insert(tk.END,"DATOS DEL USUARIO\n\n")
            for dato in datos:
                self.scrolledtext.insert(tk.END,"Identificación: "+str(dato[0])+"\n")
                self.scrolledtext.insert(tk.END,"Nombres: "+str(dato[1])+"\n")
                self.scrolledtext.insert(tk.END,"Apellidos: "+str(dato[2])+"\n")
                self.scrolledtext.insert(tk.END,"Salud: "+str(dato[3])+"\n")
                self.scrolledtext.insert(tk.END,"Pensión: "+str(dato[4])+"\n")
                self.scrolledtext.insert(tk.END,"Riesgos Laborales: "+str(dato[5])+"\n")
                self.scrolledtext.insert(tk.END,"Caja de compensación: "+str(dato[6])+"\n\n")
                
    def EditarRegistros(self):
        if(self.id.get()==""):
            messagebox.showwarning("Dato vacio","Por favor escriba un numero de identificación del registro a modificar")
        else:
            if(self.id.get().isdigit()):
                iden = (self.id.get(),)
                self.numero.set(self.id.get())
                registro = self.seguridad.ConsultarR(iden)
                if(len(registro) > 0):
                    self.identificacionM.set(registro[0][0])
                    self.nombresM.set(registro[0][1])
                    self.apellidosM.set(registro[0][2])
                    self.saludM.set(registro[0][3])
                    self.pensionM.set(registro[0][4])
                    self.riesgoLM.set(registro[0][5])
                    self.cajaCM.set(registro[0][6])
                else:
                      messagebox.showwarning("No hay registro","No existe un registro con ese numero de identificacion");
            else:
                messagebox.showwarning("Numero no valido","Ingrese un numero de identificacion valido");

    def GuardarCambios(self):
        if(self.identificacionM.get() == "" or self.nombresM.get() == "" or self.apellidosM.get()=="" or self.saludM.get()=="" or self.pensionM.get() =="" or self.riesgoLM.get() ==""or self.cajaCM.get() ==""):
            messagebox.showwarning("Dato vacio","Por favor no deje campos vacios");
        else:
            if(self.identificacionM.get().isdigit()):
                datos = (self.identificacionM.get(),self.nombresM.get(),self.apellidosM.get(),self.saludM.get(),self.pensionM.get(),self.riesgoLM.get(),self.cajaCM.get())
                a = False
                a = self.seguridad.ActualizarRegistro(datos,self.numero)
                if a:
                    messagebox.showinfo("Información", "Los datos fueron modificados")
                    self.identificacionM.set("")
                    self.nombresM.set("")
                    self.apellidosM.set("")
                    self.saludM.set("")
                    self.pensionM.set("")
                    self.cajaCM.set("")
                    self.riesgoLM.set("")
            else:
                messagebox.showwarning("Dato no valido", "Ingrese un numero de identificacion valido")
                    
        
        
        
        
        
        
        
        
        
        
        
        
            
app = SeguridadSocial()