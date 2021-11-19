import random

colores = ['amarillo', 'azul', 'verde', 'rojo']
#usuarios = [{'Nombre':'Josep'}, {'Nombre':'Claudio'}, {'Nombre':'Isabel'}, {'Nombre':'Sheila'}]
# colores = ['amarillo', 'azul', 'verde', 'rojo']
# sorted_colores = sorted(colores)
usuarios = [{'Nombre':'Josep'}, {'Nombre':'Claudio'}, {'Nombre':'Isabel'}, {'Nombre':'Sheila'}]
menu_abierto = True
while menu_abierto == True:    
    menu_items = ["1 - Añadir Color", "2 - Mostrar lista Colores", "3 - Ordenar Colores alfabeticamente", 
                "4 - Añadir Usuario", "5 - Asigna Color a cada Usuario", "6 - Eliminar Usuario", 
                "7 - Mostrar Usuario", "8 - Salir"
                ]
    for item in menu_items:
        print(item)
    seleccion_menu = int(input("Elige la opción del menú, pulsando el número correspondiente: "))
    if seleccion_menu == 1:
        editar_colores = True
        while editar_colores == True:
            # colores = ['amarillo', 'azul', 'verde', 'rojo']
            def anadir_color():
                global colores
                if elige_color not in colores:
                    colores.append(elige_color)
                else:
                    print("Ese color ya esta en el menú")
            seguir_editando = input("Editar menu de colores? ")
            if seguir_editando == "si":
                elige_color = input("Qué color te gustaria añadir? ").lower()
                anadir_color()
                editar_menu = True
                # sorted_colores = sorted(colores)
                # for color in sorted_colores:
                #     print( "·" + " " + color)
                #print(sorted_colores)
            else:
                editar_colores = False
    elif seleccion_menu == 2:
        print(colores)
    elif seleccion_menu == 3:
        print(sorted(colores))
    elif seleccion_menu == 4:
        def anadir_color():
            global colores
            if elige_color not in colores:
                colores.append(elige_color)
            else:
                print("Ese color ya esta en el menú")
        usuario_nuevo = input("Introduce el nombre del nuevo usuario por favor: ")
        usuarios.append({'Nombre': usuario_nuevo})
        if len(usuarios) > len(colores):
            print("Hay mas usuarios que colores, añade un color: ")
            elige_color = input("Qué color te gustaria añadir? ").lower()
            anadir_color()
    elif seleccion_menu == 5:
        usuarios_copia = usuarios.copy()
        for i in usuarios_copia:
            q = random.choice(colores)
            i['Color'] = q
            colores.remove(q)             
        print(usuarios_copia)
    elif seleccion_menu == 6:
        usuario_a_borrar = input("Qué usuario te gustaria borrar? ")
        for i in usuarios:
            if usuario_a_borrar in i['Nombre']:
                numero_usuario = usuarios.index(i)
                del usuarios[numero_usuario]
        print(usuarios)
    elif seleccion_menu == 7:
        for i in usuarios:
            if i == {}:
                continue
            else:
                print(i['Nombre'])
    elif seleccion_menu == 8:
        menu_abierto = False