import flet as ft

def main(page: ft.Page):
    page.title = "TEST 1"
    page.theme_mode = ft.ThemeMode.DARK

    greeting_history = []

    greeting_text = ft.Text("History of greetings: \n")
    with open('history.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            greeting_history.append(line.strip())
    greeting_text.value = ", \n".join(greeting_history)

    def text_name(e):
        name = text_input.value.strip()
        if not name:
            text_hello.value = "Please enter your name!"
            text_hello.color = ft.Colors.RED_900
        else:
            print(f"Hello, {name}!")
            text_hello.value = f"Hello, {name}!"
            text_hello.color = ft.Colors.GREEN_900
            text_input.value = ""
            greeting_history.append(name)
            with open('history.txt', 'a') as file:
                file.write(name + '\n')
            greeting_text.value = ", \n".join(greeting_history)
        page.update() # page.update() is no longer necessary

    text_hello = ft.Text("Hello", color=ft.Colors.RED_900)
    text_input = ft.TextField(label="Your name", on_submit=text_name)
    button = ft.Button("SEND", on_click=text_name)

    favourite = []
    favourite_text = ft.Text("Favourite greetings: \n")
    def favourites(e):
        favourite.append(greeting_history[-1])
        favourite_text.value = "Favourite greetings: \n" + ", \n".join(favourite)
        page.update()

    favourite_button = ft.Button("Add to favourites", on_click=favourites)

    page.add(
        text_hello,
        text_input,
        button,
        greeting_text,
        favourite_button,
        favourite_text
    )

if __name__ == "__main__":
    ft.run(main, view = ft.AppView.WEB_BROWSER)