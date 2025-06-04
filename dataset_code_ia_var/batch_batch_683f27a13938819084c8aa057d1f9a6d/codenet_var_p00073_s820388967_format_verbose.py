while True:

    width_of_rectangle = float(input("Entrer la largeur du rectangle : "))
    height_of_triangle = float(input("Entrer la hauteur du triangle isocèle : "))

    if width_of_rectangle == 0:
        break

    half_width = width_of_rectangle / 2
    hypotenuse_of_triangle = (half_width ** 2 + height_of_triangle ** 2) ** 0.5
    area_of_rectangle = width_of_rectangle ** 2
    area_of_two_triangles = 2 * width_of_rectangle * hypotenuse_of_triangle

    total_area = area_of_rectangle + area_of_two_triangles

    print(total_area)