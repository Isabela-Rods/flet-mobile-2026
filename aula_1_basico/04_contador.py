import flet as ft

def main(page: ft.Page):
    # Título que aparece na barra da janela/aba
    page.title = "Contador"

    # Cor de fundo na tela
    page.bgcolor = "#0D1B2A"

    #Centrlizar elementos
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # Padding vertical de 60px
    page.padding = ft.Padding(top=60, bottom=60, left=0, right=0)

    # Texto que exibe o valo atual do contador
    contador = ft.Text("0", size=40, color="#FF6B68", weight=ft.FontWeight.BOLD)

    # Variável para guardar a contagem
    valor = 0

    # Funcionalidades
    def somar(e):
        # Usamos "nonlocal" para dizer ao Python: quero alterar o valor da variável "valor" que foi criada na função "main" sem ter que criar uma nova variável
        nonlocal valor
        valor += 1 # Atualiação do contador (Mesmo que: "valor= valor + 1")
        contador.value = str(valor)
        page.update()

    def subtrair(e):
        nonlocal valor
        valor -= 1 # Atualização do contador (Mesmo que: "valor= valor - 1")
        contador.value = str(valor)
        page.update()     

    def resetar(e):
            nonlocal valor
            valor = 0 # Zera a variável
            contador.value = str(valor)
            page.update()

    # Montagem da página do app
    page.add(
         ft.Row(
              alignment=ft.MainAxisAlignment.CENTER,
              controls=[
                   ft.IconButton(ft.Icons.REMOVE, on_click=subtrair, icon_color="#FF6B6B"), contador,
                   ft.IconButton(ft.Icons.ADD, on_click=somar, icon_color="#FF6B6B"),
            ],
         ),
         ft.Row(
              alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.TextButton(
                        "Resetar",
                        icon=ft.Icons.RESTART_ALT,
                        on_click=resetar,
                        style=ft.ButtonStyle(color="#FFB4B4"),
                ),
            ],
         ),
    )

ft.run(main)
