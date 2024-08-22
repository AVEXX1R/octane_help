import flet as ft

def main(page: ft.Page):
    page.title = "Aplicativo de Monitoramento"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = ft.colors.BLACK

    # Conteúdo principal
    content = ft.Column(expand=True)

    def on_menu_click(e):
        content.controls.clear()
        if e.control.selected_index == 0:
            # Mix de Gasolina
            gasolina_input = ft.TextField(label="Quantidade (Litros) de gasolina abastecida", expand=1)
            etanol_input = ft.TextField(label="Porcentagem de Etanol na Gasolina", expand=1)
            options = ft.Dropdown(
                label="Selecione a mistura",
                options=[
                    ft.dropdown.Option("E25"),
                    ft.dropdown.Option("E50"),
                    ft.dropdown.Option("E85")
                ],
                expand=1
            )
            calcular_button = ft.ElevatedButton(text="Calcular")

            # Layout da opção "Mix de Gasolina"
            content.controls.append(
                ft.Row(
                    [
                        gasolina_input,
                        etanol_input
                    ],
                    spacing=10
                )
            )
            content.controls.append(
                ft.Row(
                    [
                        options,
                        calcular_button
                    ],
                    spacing=10
                )
            )

            # Área de Resultado
            result_area = ft.Container(
                content=ft.Text("Resultado aparecerá aqui", color=ft.colors.WHITE),
                bgcolor=ft.colors.BLUE_GREY_900,
                padding=10,
                alignment=ft.alignment.center,
                border_radius=5
            )
            content.controls.append(result_area)

        elif e.control.selected_index == 1:
            # Deslocamento
            diametro_input = ft.TextField(label="Diâmetro", expand=1)
            curso_input = ft.TextField(label="Curso", expand=1)
            cilindros_dropdown = ft.Dropdown(
                label="Cilindros",
                options=[
                    ft.dropdown.Option("3"),
                    ft.dropdown.Option("4"),
                    ft.dropdown.Option("5"),
                    ft.dropdown.Option("6"),
                    ft.dropdown.Option("8"),
                    ft.dropdown.Option("10"),
                    ft.dropdown.Option("12")
                ],
                expand=1
            )
            calcular_button = ft.ElevatedButton(text="Calcular")

            # Layout da opção "Deslocamento"
            content.controls.append(
                ft.Row(
                    [
                        diametro_input,
                        curso_input
                    ],
                    spacing=10
                )
            )
            content.controls.append(
                ft.Row(
                    [
                        cilindros_dropdown,
                        calcular_button
                    ],
                    spacing=10
                )
            )

            # Área de Resultado
            result_area = ft.Container(
                content=ft.Text("Resultado aparecerá aqui", color=ft.colors.WHITE),
                bgcolor=ft.colors.BLUE_GREY_900,
                padding=10,
                alignment=ft.alignment.center,
                border_radius=5
            )
            content.controls.append(result_area)

        elif e.control.selected_index == 2:
            content.controls.append(ft.Text("Pressão-Potência", color=ft.colors.BLUE))

        elif e.control.selected_index == 3:
            content.controls.append(ft.Text("Configurações", color=ft.colors.BLUE))

        content.update()

    # Navegação lateral
    nav = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        leading=ft.Text("Menu", color=ft.colors.WHITE),
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.LOCAL_GAS_STATION,
                selected_icon=ft.icons.LOCAL_GAS_STATION,
                label="Mix de Gasolina"
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.DIRECTIONS_CAR,
                selected_icon=ft.icons.DIRECTIONS_CAR,
                label="Deslocamento"
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.SPEED,
                selected_icon=ft.icons.SPEED,
                label="Pressão-Potência"
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.SETTINGS,
                selected_icon=ft.icons.SETTINGS,
                label="Configurações"
            )
        ],
        on_change=on_menu_click,
    )

    # Layout
    page.add(
        ft.Row(
            [
                nav,
                content
            ],
            expand=True,
        )
    )

    # Inicializa o conteúdo com a primeira opção diretamente
    gasolina_input = ft.TextField(label="Quantidade (Litros) de gasolina abastecida", expand=1)
    etanol_input = ft.TextField(label="Porcentagem de Etanol na Gasolina", expand=1)
    options = ft.Dropdown(
        label="Selecione a mistura",
        options=[
            ft.dropdown.Option("E25"),
            ft.dropdown.Option("E50"),
            ft.dropdown.Option("E85")
        ],
        expand=1
    )
    calcular_button = ft.ElevatedButton(text="Calcular")

    content.controls.append(
        ft.Text("Mix de Gasolina", color=ft.colors.BLUE)
    )
    content.controls.append(
        ft.Row(
            [
                gasolina_input,
                etanol_input
            ],
            spacing=10
        )
    )
    content.controls.append(
        ft.Row(
            [
                options,
                calcular_button
            ],
            spacing=10
        )
    )

    result_area = ft.Container(
        content=ft.Text("Resultado aparecerá aqui", color=ft.colors.WHITE),
        bgcolor=ft.colors.BLUE_GREY_900,
        padding=10,
        alignment=ft.alignment.center,
        border_radius=5
    )
    content.controls.append(result_area)
    content.update()

ft.app(target=main)
