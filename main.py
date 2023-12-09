import flet as ft
from flet import *


def main(page: ft.Page):
    # Page Layouts
    page.title = "Calculator ng mga pogi"
    pageWidth = page.window_width = 350

    # Page Fonts
    page.fonts = {
        'font1': 'fonts/assets/Gordita-Bold.otf',
        'font2': 'fonts/assets/Nunito-Bold.ttf'
    }

    # Init default theme
    page.bgcolor = "#f9f9f9"

    #########
    # Logic #
    #########

    # Changing theme
    def change_theme(e):
        # Change if theme is default
        page.bgcolor = "#2c3e50" if page.bgcolor == "#f9f9f9" else "#f9f9f9"
        calculation.color = "#bdc3c7" if calculation.color == "#2c3e50" else "#bdc3c7"
        result.color = "#2c3e50" if result.color == "#f9f9f9" else "#f9f9f9"
        # Buttons
        btn1.bgcolor = "#ecf0f1" if btn1.bgcolor == "#bdc3c7" else "#bdc3c7"
        btn1.color = "#2c3e50" if btn1.color == "#2c3e50" else "#2c3e50"
        btn2.bgcolor = "#ecf0f1" if btn2.bgcolor == "#bdc3c7" else "#bdc3c7"
        btn2.color = "#2c3e50" if btn2.color == "#2c3e50" else "#2c3e50"
        btn3.bgcolor = "#ecf0f1" if btn3.bgcolor == "#bdc3c7" else "#bdc3c7"
        btn3.color = "#2c3e50" if btn3.color == "#2c3e50" else "#2c3e50"
        btn5.bgcolor = "#bdc3c7" if btn5.bgcolor == "#ecf0f1" else "#ecf0f1"
        btn5.color = "#2c3e50" if btn5.color == "#2c3e50" else "#2c3e50"
        btn6.bgcolor = "#bdc3c7" if btn6.bgcolor == "#ecf0f1" else "#ecf0f1"
        btn6.color = "#2c3e50" if btn6.color == "#2c3e50" else "#2c3e50"
        btn7.bgcolor = "#bdc3c7" if btn7.bgcolor == "#ecf0f1" else "#ecf0f1"
        btn7.color = "#2c3e50" if btn7.color == "#2c3e50" else "#2c3e50"
        btn9.bgcolor = "#bdc3c7" if btn9.bgcolor == "#ecf0f1" else "#ecf0f1"
        btn9.color = "#2c3e50" if btn9.color == "#2c3e50" else "#2c3e50"
        btn10.bgcolor = "#bdc3c7" if btn10.bgcolor == "#ecf0f1" else "#ecf0f1"
        btn10.color = "#2c3e50" if btn10.color == "#2c3e50" else "#2c3e50"
        btn11.bgcolor = "#bdc3c7" if btn11.bgcolor == "#ecf0f1" else "#ecf0f1"
        btn11.color = "#2c3e50" if btn11.color == "#2c3e50" else "#2c3e50"
        btn13.bgcolor = "#bdc3c7" if btn13.bgcolor == "#ecf0f1" else "#ecf0f1"
        btn13.color = "#2c3e50" if btn13.color == "#2c3e50" else "#2c3e50"
        btn14.bgcolor = "#bdc3c7" if btn14.bgcolor == "#ecf0f1" else "#ecf0f1"
        btn14.color = "#2c3e50" if btn14.color == "#2c3e50" else "#2c3e50"
        btn15.bgcolor = "#bdc3c7" if btn15.bgcolor == "#ecf0f1" else "#ecf0f1"
        btn15.color = "#2c3e50" if btn15.color == "#2c3e50" else "#2c3e50"
        btn17.bgcolor = "#bdc3c7" if btn17.bgcolor == "#ecf0f1" else "#ecf0f1"
        btn17.color = "#2c3e50" if btn17.color == "#2c3e50" else "#2c3e50"
        btn18.bgcolor = "#bdc3c7" if btn18.bgcolor == "#ecf0f1" else "#ecf0f1"
        btn18.color = "#2c3e50" if btn18.color == "#2c3e50" else "#2c3e50"
        btn19.bgcolor = "#bdc3c7" if btn19.bgcolor == "#ecf0f1" else "#ecf0f1"
        btn19.color = "#2c3e50" if btn19.color == "#2c3e50" else "#2c3e50"

        page.update()

        # Change icon
        toggleTheme.selected = not toggleTheme.selected
        page.update()

    # Get input
    def button_click(e):
        data = e.control.data

        # Numbers
        if data in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".", "+", "-", "/", "(", ")", "*"]:
            calculation.value = str(calculation.value) + str(data)
            page.update()

        # Evaluate expression
        if data == "=":
            result.value = str(eval(calculation.value))
            page.update()

        # Remove 1 input
        if data == "C":
            decreaseSt = list(calculation.value)
            decreaseSt.pop()
            calculation.value = "".join(map(str, decreaseSt))

            # Check if value is 0
            if calculation.value == "":
                calculation.value = ""
                result.value = "0"

            page.update()

        # Remove all input
        if data == "AC":
            calculation.value = ""
            result.value = "0"
            page.update()

    #
    #START main UI area
    #
    toggleTheme = ft.IconButton(on_click=change_theme, icon="dark_mode", selected_icon="light_mode", icon_size=20, style=ButtonStyle(color={"": "#2c3e50", "selected": "#ffe569"}))
    calculation = ft.TextField(value="", width=page.window_width , text_align=TextAlign.RIGHT, color="#bdc3c7", text_size=50, read_only=True, border=InputBorder.NONE, content_padding=0)
    result = ft.TextField(value="0", width=page.window_width , text_align=TextAlign.RIGHT, color="#2c3e50", text_size=60,  read_only=True, border=InputBorder.NONE, content_padding=0)

    # Calc button
    def calc_button(text, bgcolor, data):
        return ElevatedButton(
            text=text,
            data=data,
            width=75,
            height=75,
            on_click=button_click,
            style=ButtonStyle(
                padding=0,
                bgcolor=bgcolor,
                color="#2c3e50",
                shape=RoundedRectangleBorder(radius=10),
            ),
        )

    # Buttons
    btn1 = calc_button("AC",  "#ecf0f1", "AC")
    btn2 = calc_button("(",  "#ecf0f1", "(")
    btn3 = calc_button(")", "#ecf0f1", ")")
    btn4 = calc_button("÷",  "#ffe569", "/")
    btn5 = calc_button("7",  "#bdc3c7", "7")
    btn6 = calc_button("8", "#bdc3c7", "8")
    btn7 = calc_button("9",  "#bdc3c7", "9")
    btn8 = calc_button("x",  "#ffe569", "*")
    btn9 = calc_button("4",  "#bdc3c7", "4")
    btn10 = calc_button("5",  "#bdc3c7", "5")
    btn11 = calc_button("6",  "#bdc3c7", "6")
    btn12 = calc_button("-", "#ffe569", "-")
    btn13 = calc_button("1",  "#bdc3c7", "1")
    btn14 = calc_button("2",  "#bdc3c7", "2")
    btn15 = calc_button("3", "#bdc3c7", "3")
    btn16 = calc_button("+",  "#ffe569", "+")
    btn17 = calc_button("0", "#bdc3c7", "0")
    btn18 = calc_button(".", "#bdc3c7", ".")
    btn19 = calc_button("C",  "#bdc3c7", "C")
    btn20 = calc_button("=", "#ffe569", "=")

    #Add to container
    topCont = ft.Container(
        padding=ft.padding.only(top=20),
        content=ft.Column(
            controls=[calculation, result]
        )
    )

    # Add to row
    btnr1 = ft.Container(
        width=pageWidth,
        padding=ft.padding.only(top=70),
        content=ft.Row(
            controls=[btn1, btn2, btn3, btn4],
            alignment = ft.MainAxisAlignment.SPACE_BETWEEN
        )
    )

    btnr2 = ft.Container(
        width=pageWidth,
        content=ft.Row(
            controls=[btn5, btn6, btn7, btn8],
            alignment = ft.MainAxisAlignment.SPACE_BETWEEN
        )
    )

    btnr3 = ft.Container(
        width=pageWidth,
        content=ft.Row(
            controls=[btn9, btn10, btn11, btn12],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )
    )

    btnr4 = ft.Container(
        width=pageWidth,
        content=ft.Row(
            controls=[btn13, btn14, btn15, btn16],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )
    )

    btnr5 = ft.Container(
        width=pageWidth,
        content=ft.Row(
            controls=[btn17, btn18, btn19, btn20],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )
    )

    page.add(toggleTheme,topCont)
    page.add(btnr1, btnr2, btnr3, btnr4, btnr5)


ft.app(target=main)