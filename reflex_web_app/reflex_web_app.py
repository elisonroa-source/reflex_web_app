import reflex as rx


class State(rx.State):
    mensaje = "Bienvenido a la cocina 🍳"

    def inicio(self):
        self.mensaje = "🔥 Estás en el inicio de la cocina"

    def recetas(self):
        self.mensaje = "📖 Explora nuestras mejores recetas"

    def chef(self):
        self.mensaje = "👨‍🍳 Modo chef activado"


def index():
    return rx.center(
        rx.vstack(
            rx.box(
                rx.heading("COCINA INTERACTIVA 🍽️", size="8"),
                rx.text(State.mensaje, font_size="18px"),
                text_align="center",
                padding="20px",
            ),

            rx.hstack(
                rx.button(
                    "Inicio",
                    on_click=State.inicio,
                    bg="blue",
                    color="white",
                    padding="10px 20px",
                ),
                rx.button(
                    "Recetas",
                    on_click=State.recetas,
                    bg="red",
                    color="white",
                    padding="10px 20px",
                ),
                rx.button(
                    "Chef",
                    on_click=State.chef,
                    bg="blue",
                    color="white",
                    padding="10px 20px",
                ),
                spacing="5",
            ),

            rx.image(
                src="https://images.unsplash.com/photo-1556911220-e15b29be8c8f",
                width="450px",
                border_radius="15px",
                box_shadow="lg",
            ),

            spacing="6",
            align="center",
        ),
        height="100vh",
    )


app = rx.App()
app.add_page(index)



