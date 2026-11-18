import customtkinter as ctk

from servicios.gestor_juego import GestorJuego

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class VentanaPrincipal(ctk.CTk):
    ICONOS_CLASE = {
        "Guerrero": "⚔️",
        "Mago": "🔮",
    }

    def __init__(self):
        super().__init__()

        self.title("⚔️ RPG Manager — Simulador de Combate POO")
        self.geometry("760x620")
        self.minsize(660, 520)

        self.gestor = GestorJuego()

        # --- Encabezado ---
        self.frame_header = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_header.pack(fill="x", padx=24, pady=(20, 8))

        self.lbl_titulo = ctk.CTkLabel(
            self.frame_header,
            text="🛡️ RPG Manager — Arena de Combate",
            font=ctk.CTkFont(size=24, weight="bold"),
        )
        self.lbl_titulo.pack()

        self.lbl_subtitulo = ctk.CTkLabel(
            self.frame_header,
            text="Crea héroes, equípalos y pon a prueba sus habilidades por turnos",
            font=ctk.CTkFont(size=13),
            text_color=("gray40", "gray70"),
        )
        self.lbl_subtitulo.pack(pady=(2, 0))

        # --- Sección 1: Creación de Personajes ---
        self.frame_crear = ctk.CTkFrame(self, corner_radius=12)
        self.frame_crear.pack(fill="x", padx=24, pady=8)

        self.lbl_sec_crear = ctk.CTkLabel(
            self.frame_crear,
            text="✨ Reclutar Nuevo Personaje",
            font=ctk.CTkFont(size=14, weight="bold"),
        )
        self.lbl_sec_crear.pack(anchor="w", padx=16, pady=(12, 4))

        self.frame_crear_controles = ctk.CTkFrame(self.frame_crear, fg_color="transparent")
        self.frame_crear_controles.pack(fill="x", padx=12, pady=(0, 12))

        self.txt_nombre = ctk.CTkEntry(
            self.frame_crear_controles,
            placeholder_text="Nombre del héroe (ej. Aragorn, Gandalf)...",
            height=38,
        )
        self.txt_nombre.pack(side="left", padx=(4, 8), expand=True, fill="x")

        # Selector visual con iconos para la clase del personaje
        self.seg_tipo = ctk.CTkSegmentedButton(
            self.frame_crear_controles,
            values=["⚔️ Guerrero", "🔮 Mago"],
            height=38,
            font=ctk.CTkFont(size=13, weight="bold"),
        )
        self.seg_tipo.set("⚔️ Guerrero")
        self.seg_tipo.pack(side="left", padx=8)

        self.btn_crear = ctk.CTkButton(
            self.frame_crear_controles,
            text="➕ Crear",
            command=self.crear_personaje_accion,
            width=110,
            height=38,
            font=ctk.CTkFont(size=13, weight="bold"),
        )
        self.btn_crear.pack(side="left", padx=(8, 4))

        # --- Sección 2: Arena de Combate ---
        self.frame_combate = ctk.CTkFrame(self, corner_radius=12)
        self.frame_combate.pack(fill="x", padx=24, pady=8)

        self.lbl_sec_combate = ctk.CTkLabel(
            self.frame_combate,
            text="⚔️ Selección de Combatientes",
            font=ctk.CTkFont(size=14, weight="bold"),
        )
        self.lbl_sec_combate.pack(anchor="w", padx=16, pady=(12, 4))

        self.frame_combate_controles = ctk.CTkFrame(self.frame_combate, fg_color="transparent")
        self.frame_combate_controles.pack(fill="x", padx=12, pady=(0, 12))

        self.combo_p1 = ctk.CTkComboBox(
            self.frame_combate_controles,
            values=["Sin personajes"],
            height=38,
            state="readonly",
        )
        self.combo_p1.set("Sin personajes")
        self.combo_p1.pack(side="left", padx=(4, 6), expand=True, fill="x")

        self.lbl_vs = ctk.CTkLabel(
            self.frame_combate_controles,
            text="⚡ VS ⚡",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color=("#D97706", "#FBBF24"),
        )
        self.lbl_vs.pack(side="left", padx=6)

        self.combo_p2 = ctk.CTkComboBox(
            self.frame_combate_controles,
            values=["Sin personajes"],
            height=38,
            state="readonly",
        )
        self.combo_p2.set("Sin personajes")
        self.combo_p2.pack(side="left", padx=(6, 8), expand=True, fill="x")

        self.btn_atacar = ctk.CTkButton(
            self.frame_combate_controles,
            text="🔥 Simular Turno",
            command=self.simular_turno,
            width=145,
            height=38,
            fg_color=("#DC2626", "#B91C1C"),
            hover_color=("#B91C1C", "#991B1B"),
            font=ctk.CTkFont(size=13, weight="bold"),
        )
        self.btn_atacar.pack(side="left", padx=(4, 4))

        # --- Sección 3: Bitácora de Batalla ---
        self.frame_log = ctk.CTkFrame(self, corner_radius=12)
        self.frame_log.pack(fill="both", expand=True, padx=24, pady=(8, 20))

        self.frame_log_header = ctk.CTkFrame(self.frame_log, fg_color="transparent")
        self.frame_log_header.pack(fill="x", padx=16, pady=(10, 4))

        self.lbl_log = ctk.CTkLabel(
            self.frame_log_header,
            text="📜 Bitácora de Eventos y Combate",
            font=ctk.CTkFont(size=14, weight="bold"),
        )
        self.lbl_log.pack(side="left")

        self.btn_limpiar = ctk.CTkButton(
            self.frame_log_header,
            text="🧹 Limpiar",
            command=self.limpiar_bitacora,
            width=85,
            height=28,
            fg_color=("gray75", "gray28"),
            hover_color=("gray65", "gray35"),
            font=ctk.CTkFont(size=12),
        )
        self.btn_limpiar.pack(side="right")

        self.txt_output = ctk.CTkTextbox(
            self.frame_log,
            font=ctk.CTkFont(family="Consolas", size=13),
            corner_radius=8,
        )
        self.txt_output.pack(pady=(4, 14), padx=14, fill="both", expand=True)
        self._escribir_log("🏰 Bienvenido a RPG Manager. Crea al menos dos personajes para iniciar el combate.\n")

    def _escribir_log(self, mensaje: str):
        self.txt_output.configure(state="normal")
        self.txt_output.insert("end", mensaje)
        self.txt_output.see("end")
        self.txt_output.configure(state="disabled")

    def limpiar_bitacora(self):
        self.txt_output.configure(state="normal")
        self.txt_output.delete("1.0", "end")
        self.txt_output.configure(state="disabled")

    def _formatear_etiqueta_personaje(self, personaje) -> str:
        clase = type(personaje).__name__
        icono = self.ICONOS_CLASE.get(clase, "🛡️")
        estado = f"{personaje.vida} HP" if personaje.esta_vivo() else "💀 Caído"
        return f"{icono} {personaje.nombre} ({estado})"

    def _extraer_nombre_de_etiqueta(self, etiqueta: str) -> str:
        # Formato esperado: "⚔️ Aragorn (120 HP)" -> "Aragorn"
        if etiqueta in ("Sin personajes", ""):
            return ""
        sin_icono = etiqueta.split(" ", 1)[1] if " " in etiqueta else etiqueta
        return sin_icono.rsplit(" (", 1)[0]

    def crear_personaje_accion(self):
        nombre = self.txt_nombre.get()
        seleccion_tipo = self.seg_tipo.get()
        # Extraer "Guerrero" o "Mago" de "⚔️ Guerrero" / "🔮 Mago"
        tipo = seleccion_tipo.split(" ", 1)[1] if " " in seleccion_tipo else seleccion_tipo
        icono = self.ICONOS_CLASE.get(tipo, "🛡️")

        try:
            personaje = self.gestor.crear_personaje(tipo, nombre)
            self._escribir_log(
                f"✅ {icono} Reclutado {tipo}: {personaje.nombre} "
                f"(❤️ Vida: {personaje.vida} | 🗡️ Ataque base: {personaje.ataque_base})\n"
            )
            self.actualizar_combos(seleccionar_ultimo=True)
            self.txt_nombre.delete(0, "end")
        except ValueError as error:
            self._escribir_log(f"⚠️ Error: {error}\n")

    def actualizar_combos(self, seleccionar_ultimo: bool = False):
        if not self.gestor.personajes:
            self.combo_p1.configure(values=["Sin personajes"])
            self.combo_p2.configure(values=["Sin personajes"])
            self.combo_p1.set("Sin personajes")
            self.combo_p2.set("Sin personajes")
            return

        sel_actual_1 = self._extraer_nombre_de_etiqueta(self.combo_p1.get())
        sel_actual_2 = self._extraer_nombre_de_etiqueta(self.combo_p2.get())

        etiquetas = [self._formatear_etiqueta_personaje(p) for p in self.gestor.personajes]
        self.combo_p1.configure(values=etiquetas)
        self.combo_p2.configure(values=etiquetas)

        if seleccionar_ultimo and len(etiquetas) >= 2:
            if not sel_actual_1 or sel_actual_1 == "Sin personajes":
                self.combo_p1.set(etiquetas[0])
            else:
                match1 = next((e for e in etiquetas if self._extraer_nombre_de_etiqueta(e) == sel_actual_1), etiquetas[0])
                self.combo_p1.set(match1)
            self.combo_p2.set(etiquetas[-1])
        else:
            match1 = next((e for e in etiquetas if self._extraer_nombre_de_etiqueta(e) == sel_actual_1), etiquetas[0])
            default2 = etiquetas[1] if len(etiquetas) > 1 else etiquetas[0]
            match2 = next((e for e in etiquetas if self._extraer_nombre_de_etiqueta(e) == sel_actual_2), default2)
            self.combo_p1.set(match1)
            self.combo_p2.set(match2)

    def simular_turno(self):
        etiqueta1 = self.combo_p1.get()
        etiqueta2 = self.combo_p2.get()

        nombre1 = self._extraer_nombre_de_etiqueta(etiqueta1)
        nombre2 = self._extraer_nombre_de_etiqueta(etiqueta2)

        if not nombre1 or not nombre2:
            self._escribir_log("⚠️ Debes crear al menos dos personajes antes de combatir.\n")
            return

        if nombre1 == nombre2:
            self._escribir_log("⚠️ Un personaje no puede atacarse a sí mismo.\n")
            return

        p1 = next((p for p in self.gestor.personajes if p.nombre == nombre1), None)
        p2 = next((p for p in self.gestor.personajes if p.nombre == nombre2), None)

        if p1 is None or p2 is None:
            self._escribir_log("⚠️ No se pudo encontrar a uno de los personajes.\n")
            return

        resultado = self.gestor.simular_combate(p1, p2)
        self._escribir_log(f"⚔️ {resultado}\n{'─' * 48}\n")
        self.actualizar_combos()
