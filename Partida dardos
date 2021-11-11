def nueva_tirada():
    tirada_1 = int(input("Primer lanzamiento: "))
    tirada_2 = int(input("Segundo lanzamiento: "))
    tirada_3 = int(input("Tercer lanzamiento: "))
    tres_tiradas = tirada_1 + tirada_2 + tirada_3
    return(tres_tiradas)
fin_rondas = False
puntos = 121
ronda = 0
continuar = True
while continuar == True:
    desea_continuar = input("Nueva partida de dardos? Escribe 'si' o 'no'")
    if desea_continuar == 'no':
        print("Gracias por jugar")
        continuar = False
    else:
        nombre_1 = input("Nombre del primer jugador: ")
        nombre_2 = input("Nombre del segundo jugador: ")
        nombre_3 = input("Nombre del tercer jugador: ")
        nombre_4 = input("Nombre del cuarto jugador: ")
        jugador_1 = [nombre_1.capitalize(), puntos]
        jugador_2 = [nombre_2.capitalize(), puntos]
        jugador_3 = [nombre_3.capitalize(), puntos]
        jugador_4 = [nombre_4.capitalize(), puntos]
        while not fin_rondas:
            if ronda == 3 :
                print("Fin del Juego")
                if jugador_1[1] == jugador_2[1]:
                    print(f"{nombre_1.capitalize()} ha empatado con {nombre_2.capitalize()} con {jugador_1[1]} puntos.")
                elif jugador_1[1] == jugador_3[1]:
                    print(f"{nombre_1.capitalize()} ha empatado con {nombre_3.capitalize()} con {jugador_1[1]} puntos.")
                elif jugador_1[1] == jugador_4[1]:
                    print(f"{nombre_1.capitalize()} ha empatado con {nombre_4.capitalize()} con {jugador_1[1]} puntos.")
                elif jugador_2[1] == jugador_1[1]:
                    print(f"{nombre_2.capitalize()} ha empatado con {nombre_1.capitalize()} con {jugador_2[1]} puntos.")
                elif jugador_2[1] == jugador_3[1]:
                    print(f"{nombre_2.capitalize()} ha empatado con {nombre_3.capitalize()} con {jugador_2[1]} puntos.")
                elif jugador_2[1] == jugador_4[1]:
                    print(f"{nombre_2.capitalize()} ha empatado con {nombre_4.capitalize()} con {jugador_2[1]} puntos.")
                elif jugador_3[1] == jugador_1[1]:
                    print(f"{nombre_3.capitalize()} ha empatado con {nombre_1.capitalize()} con {jugador_3[1]} puntos.")
                elif jugador_3[1] == jugador_2[1]:
                    print(f"{nombre_3.capitalize()} ha empatado con {nombre_2.capitalize()} con {jugador_3[1]} puntos.")
                elif jugador_3[1] == jugador_4[1]:
                    print(f"{nombre_3.capitalize()} ha empatado con {nombre_4.capitalize()} con {jugador_3[1]} puntos.")
                elif jugador_4[1] == jugador_1[1]:
                    print(f"{nombre_4.capitalize()} ha empatado con {nombre_1.capitalize()} con {jugador_4[1]} puntos.")
                elif jugador_4[1] == jugador_2[1]:
                    print(f"{nombre_4.capitalize()} ha empatado con {nombre_2.capitalize()} con {jugador_4[1]} puntos.")
                elif jugador_4[1] == jugador_3[1]:
                    print(f"{nombre_4.capitalize()} ha empatado con {nombre_3.capitalize()} con {jugador_4[1]} puntos.")
                elif jugador_1[1] < jugador_2[1] or jugador_1[1] < jugador_3[1] or jugador_1[1] < jugador_4[1]:
                    print(f"{nombre_1.capitalize()} ha ganado con un total de {jugador_1[1]} puntos en la ronda {ronda}")
                elif jugador_2[1] < jugador_1[1] or jugador_2[1] < jugador_3[1] or jugador_2[1] < jugador_4[1]:
                    print(f"{nombre_2.capitalize()} ha ganado con un total de {jugador_2[2]} puntos en la ronda {ronda}")
                elif jugador_3[1] < jugador_2[1] or jugador_3[1] < jugador_1[1] or jugador_3[1] < jugador_4[1]:
                    print(f"{nombre_3.capitalize()} ha ganado con un total de {jugador_[3]} puntos en la ronda {ronda}")
                elif jugador_4[1] < jugador_2[1] or jugador_4[1] < jugador_3[1] or jugador_4[1] < jugador_1[1]:
                    print(f"{nombre_4.capitalize()} ha ganado con un total de {jugador_[4]} puntos en la ronda {ronda}")
                fin_rondas = True
            else:
                ronda += 1
                print(f"Ronda numero {ronda}")
                print(f"--->{jugador_1[0]}")
                jugador_1[1] -= nueva_tirada()
                if jugador_1[1] < 0:
                    print(f"{jugador_1[0]} ha ganado con {jugador_1[1]} puntos")
                    fin_rondas = True
                else:
                    print(f"--->{jugador_2[0]}")
                    jugador_2[1] -= nueva_tirada()
                    if jugador_2[1] < 0:
                        print(f"El {jugador_2[0]} ha ganado con {jugador_2[1]} puntos")
                        fin_rondas = True
                    else:
                        print(f"--->{jugador_3[0]}")
                        jugador_3[1] -= nueva_tirada()
                        if jugador_3[1] < 0:
                            print(f"El {jugador_3[0]} ha ganado con {jugador_3[1]} puntos")
                            fin_rondas = True
                        else:
                            print(f"--->{jugador_4[0]}")
                            jugador_4[1] -= nueva_tirada()
                            if jugador_4[1] < 0:
                                print(f"El {jugador_4[0]} ha ganado con {jugador_4[1]} puntos")
                                fin_rondas = True
                            else:
                                print(f"Los puntos del {jugador_1[1]} son {jugador_1[0]}")
                                print(f"Los puntos del {jugador_2[1]} son {jugador_2[0]}")
                                print(f"Los puntos del {jugador_3[1]} son {jugador_3[0]}")
                                print(f"Los puntos del {jugador_4[1]} son {jugador_4[0]}")
