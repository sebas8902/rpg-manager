import customtkinter as ctk

from servicios.gestor_juego import GestorJuego

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


class VentanaPrincipal(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Gestor de Combate RPG - POO")
        self.geometry("720x560")
        self.minsize(620, 460)

        self.gestor = GestorJuego()

        self.lbl_titulo = ctk.CTkLabel(
            self,
            text="Simulador RPG POO",
            font=ctk.CTkFont(size=22, weight="bold"),
        )
        self.lbl_titulo.pack(pady=(18, 12))

        self.frame_crear = ctk.CTkFrame(self)
        self.frame_crear.pack(fill="x", padx=20, pady=8)

        self.txt_nombre = ctk.CTkEntry(
            self.frame_crear,
            placeholder_text="Nombre del personaje",
            width=250,
        )
        self.txt_nombre.pack(side="left", padx=(12, 8), pady=12, expand=True, fill="x")

        self.combo_tipo = ctk.CTkComboBox(
            self.frame_crear,
            values=["Guerrero", "Mago"],
            width=140,
        )
        self.combo_tipo.set("Guerrero")
        self.combo_tipo.pack(side="left", padx=8, pady=12)

        self.btn_crear = ctk.CTkButton(
            self.frame_crear,
            text="Crear",
            command=self.crear_personaje_accion,
            width=100,
        )
        self.btn_crear.pack(side="left", padx=(8, 12), pady=12)

        self.frame_combate = ctk.CTkFrame(self)
        self.frame_combate.pack(fill="x", padx=20, pady=8)

        self.combo_p1 = ctk.CTkComboBox(self.frame_combate, values=["Sin personajes"], width=200)
        self.combo_p1.pack(side="left", padx=(12, 8), pady=12, expand=True)

        self.combo_p2 = ctk.CTkComboBox(self.frame_combate, values=["Sin personajes"], width=200)
        self.combo_p2.pack(side="left", padx=8, pady=12, expand=True)

        self.btn_atacar = ctk.CTkButton(
            self.frame_combate,
            text="Simular turno",
            command=self.simular_turno,
            width=140,
        )
        self.btn_atacar.pack(side="left", padx=(8, 12), pady=12)

        self.txt_output = ctk.CTkTextbox(self, width=640, height=220)
        self.txt_output.pack(pady=(8, 18), padx=20, fill="both", expand=True)
        self.txt_output.insert("end", "Bienvenido al simulador RPG POO.\n")
        self.txt_output.configure(state="disabled")

    def crear_personaje_accion(self):
        nombre = self.txt_nombre.get()
        tipo = self.combo_tipo.get()

        try:
            personaje = self.gestor.crear_personaje(tipo, nombre)
            self.txt_output.configure(state="normal")
            self.txt_output.insert(
                "end",
                f"Se creó el {tipo}: {personaje.nombre} (Vida: {personaje.vida})\n",
            )
            self.txt_output.see("end")
            self.txt_output.configure(state="disabled")
            self.actualizar_combos()
            self.txt_nombre.delete(0, "end")
        except ValueError as error:
            self.txt_output.configure(state="normal")
            self.txt_output.insert("end", f"Error: {error}\n")
            self.txt_output.see("end")
            self.txt_output.configure(state="disabled")

    def actualizar_combos(self):
        nombres = [p.nombre for p in self.gestor.personajes]

        if not nombres:
            self.combo_p1.configure(values=["Sin personajes"])
            self.combo_p2.configure(values=["Sin personajes"])
            self.combo_p1.set("Sin personajes")
            self.combo_p2.set("Sin personajes")
            return

        self.combo_p1.configure(values=nombres)
        self.combo_p2.configure(values=nombres)
        self.combo_p1.set(nombres[0])
        self.combo_p2.set(nombres[1] if len(nombres) > 1 else nombres[0])

    def simular_turno(self):
        nombre1 = self.combo_p1.get()
        nombre2 = self.combo_p2.get()

        if nombre1 in ("Sin personajes", "") or nombre2 in ("Sin personajes", ""):
            self.txt_output.configure(state="normal")
            self.txt_output.insert("end", "Debes crear al menos dos personajes antes de combatir.\n")
            self.txt_output.see("end")
            self.txt_output.configure(state="disabled")
            return

        if nombre1 == nombre2:
            self.txt_output.configure(state="normal")
            self.txt_output.insert("end", "Un personaje no puede atacarse a sí mismo.\n")
            self.txt_output.see("end")
            self.txt_output.configure(state="disabled")
            return

        p1 = next((p for p in self.gestor.personajes if p.nombre == nombre1), None)
        p2 = next((p for p in self.gestor.personajes if p.nombre == nombre2), None)

        if p1 is None or p2 is None:
            self.txt_output.configure(state="normal")
            self.txt_output.insert("end", "No se pudo encontrar a uno de los personajes.\n")
            self.txt_output.see("end")
            self.txt_output.configure(state="disabled")
            return

        resultado = self.gestor.simular_combate(p1, p2)
        self.txt_output.configure(state="normal")
        self.txt_output.insert("end", f"{resultado}\n{'-' * 40}\n")
        self.txt_output.see("end")
        self.txt_output.configure(state="disabled")
