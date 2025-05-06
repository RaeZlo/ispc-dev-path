"""
Crea una tupla con tus tres colores favoritos e imprime sólo el segundo color.
"""



def get_second_favorite_color(colors: tuple) -> str:
    return colors[1]


def main():
    favorite_colors = ("black", "violet", "green")

    try:
        second_color = get_second_favorite_color(favorite_colors)
        print(f"Mi segundo color favorito es: {second_color}")
    except IndexError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
