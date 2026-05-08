import reflex as rx


class State(rx.State):
    mensaje = "Bienvenido a la cocina 👨‍🍳"

    def inicio(self):
        self.mensaje = "🔥 Bienvenido a la cocina, listo para empezar"

    def recetas(self):
        self.mensaje = "📖 Aquí puedes encontrar recetas deliciosas"

    def chef(self):
        self.mensaje = "🍽️ Modo chef activado, a cocinar con estilo"


def index():
    return rx.center(
        rx.vstack(
            rx.heading("COCINA INTERACTIVA 🍳", size="8", color="blue"),

            rx.text(State.mensaje, color="red"),

            rx.hstack(
                rx.button(
                    "Inicio",
                    on_click=State.inicio,
                    color="white",
                    bg="blue",
                ),
                rx.button(
                    "Recetas",
                    on_click=State.recetas,
                    color="white",
                    bg="red",
                ),
                rx.button(
                    "Chef",
                    on_click=State.chef,
                    color="white",
                    bg="blue",
                ),
                spacing="4",
            ),

            rx.image(
                src="https://images.unsplash.com/photo-1504674900247-0877df9cc836",
                width="400px",
                border_radius="10px",
            ),

            spacing="6",
        ),
        height="100vh",
    )


app = rx.App()
app.add_page(index)



