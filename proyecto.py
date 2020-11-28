import csv
__author__ = "tololo90"
__email__ = "tololo90@gmail.com"
__version__ = "1.0"


def inicio_programa():
    while True:
        try:
            seleccion = int(input("Para agregar datos escriba 1\nPara"
                                  " consultar estadisticas escriba 2\n"
                                  "Para finalizar escriba 3\n"))
        except:
            print("Opcion incorrecta, vuelva a intentarlo")
            continue
        if seleccion != 1 and seleccion != 2 and seleccion != 3:
            print("Opcion incorrecta, vuelva a intentarlo")
            continue
        if seleccion == 1:
            while True:
                try:
                    accion = int(input("Esta en la seccion de datos\nSi desea "
                                       "continuar escriba 1\nSi deasea volver "
                                       "atras escriba 2\n"))
                    if accion == 1:
                        pass
                    if accion == 2:
                        break
                    if accion != 1 and accion != 2:
                        print("Error, vuelva a intentarlo")
                        continue
                except:
                    print("Error, vuelva a intentarlo")
                    continue
                print("Complete los siguientes datos")
                mes = str(input("Mes:\n"))
                liga = str(input("Liga:\n"))
                local = str(input("Equipo local:\n"))
                visitante = str(input("Equipo visitante:\n"))
                linea = str(input("Linea\n"))
                inversion = int(input("Inversion\n"))
                cuota = float(input("Cuota\n"))
                resultado = str(input("Resultado, W (ganancias) "
                                      "L (perdidas)\n"))
                ganancia = float(input("Ganancia\n"))
                break
            while True:
                print(f"Verifique los datos ingresados\nMes = {mes}\nLiga = "
                      f"{liga}\nLocal = {local}\nVisitante = {visitante}\n"
                      f"Linea = {linea}\nInversion = {inversion}\nCuota = "
                      f"{cuota}\nResultado = {resultado}\n"
                      f"Ganancia = {ganancia}")
                try:
                    validar = int(input("Si los datos estan bien escriba "
                                        "1\nSi estan mal escriba 2\nSi"
                                        " desea volver atras 3\n"))
                except:
                    print("Error, vuelva a intentarlo")
                    continue
                if validar != 1 and validar != 2 and validar != 3:
                        print("Error, vuelva a intentarlo")
                        continue
                if validar == 3:
                    break
                if validar == 2:
                    print("Escriba el numero segun el dato que quiera "
                          "corregir")
                    try:
                        dato_error = int(input("Mes = 1\nLiga = 2\nLocal"
                                               " = 3\nVisitante = 4\nLinea"
                                               " = 5\nInversion = 6\nCuota"
                                               " = 7\nResultado = 8\n"
                                               "Ganancia = 9\n"))
                    except:
                        print("Error, vuelva a intentarlo")
                        continue
                    if dato_error <= 0 and dato_error >= 10:
                        print("Error, vuelva a intentarlo")
                        continue
                    if dato_error == 1:
                        mes = str(input("Mes:\n"))
                    if dato_error == 2:
                        liga = str(input("Liga:\n"))
                    if dato_error == 3:
                        local = str(input("Local:\n"))
                    if dato_error == 4:
                        visitante = str(input("Visitante:\n"))
                    if dato_error == 5:
                        linea = str(input("Linea\n"))
                    if dato_error == 6:
                        inversion = int(input("Inversion\n"))
                    if dato_error == 7:
                        cuota = float(input("Cuota\n"))
                    if dato_error == 8:
                        resultado = str(input("Resultado, W (gananancias) L "
                                              "(perderdidas)\n"))
                    if dato_error == 9:
                        ganancia = float(input("ganancia\n"))
                if validar == 1:
                    estadisticas = open("estadisticas.csv", "a", newline='')
                    header = ["Mes", "Liga", "Local", "Visitante", "Linea",
                              "Inversion", "Cuota", "Resultado", "Ganancia"]
                    writer = csv.DictWriter(estadisticas, fieldnames=header)
                    writer.writerow({"Mes": mes, "Liga": liga, "Local": local,
                                     "Visitante": visitante, "Linea": linea,
                                     "Inversion": inversion, "Cuota": cuota,
                                     "Resultado": resultado,
                                     "Ganancia": ganancia})
                    estadisticas.close()
                    print("datos agregados correctamente")
                    break
        if seleccion == 2:
            while True:
                try:
                    accion = int(input("Esta en la seccion de estadisticas\nSi"
                                       " desea continuar escriba 1\nSi deasea"
                                       " volver atras escriba 2\n"))
                    if accion == 1:
                        pass
                    if accion == 2:
                        break
                    if accion != 1 and accion != 2:
                        print("Error, vuelva a intentarlo")
                        continue
                except:
                    print("Error, vuelva a intentarlo")
                    continue
                try:
                    liga_total = int(input("Para ver estadisticas totales"
                                           " presione 1\nPara ver estadisticas"
                                           " por liga presione 2\n"))
                    if liga_total == 1:
                        win = 0
                        lose = 0
                        total_invertido = 0
                        total_ganancia = 0
                        with open('estadisticas.csv') as csvfile:
                            data = list(csv.DictReader(csvfile))
                        inversion = len(data)
                        ganancia = len(data)
                        win_lose = len(data)
                        for i in range(inversion):
                            row = data[i]
                            inversion = int(row.get('inversion'))
                            total_invertido += inversion
                            ganancia = float(row.get('Ganancia'))
                            total_ganancia += ganancia
                            win_lose = str(row.get('Resultado'))
                            if win_lose == "W":
                                win += 1
                            if win_lose == "L":
                                lose += 1
                        yield_total = (total_ganancia / total_invertido)*100
                        total = win + lose
                        winrate = win / total * 100
                        print(f"Se han invertido {total_invertido} unidades\n"
                               "El total de las ganancias es de "
                              f"{total_ganancia:.4} unidades\nEl yield es del"
                              f" {yield_total:.4}%\nEl porcentaje de winrate "
                              f"es de {winrate:.4}%")
                        break
                    if liga_total == 2:
                        with open('estadisticas.csv') as csvfile:
                            total_ligas = []
                            data = list(csv.DictReader(csvfile))
                            liga = len(data)
                            for i in range(liga):
                                pais = data[i].get('Liga')
                                if pais not in total_ligas:
                                    total_ligas.append(pais)
                            print("Estas son las ligas que puede elegir\n"
                                  f"{total_ligas}")
                            liga_elegida = str(input("Copie exactamente como "
                                                     "figura arriba, "
                                                     "respentando la primer "
                                                     "letra mayuscula, la liga"
                                                     " que quiera\n"))
                            csvfile = open('temporal.csv', 'w', newline='')
                            header = ["Mes", "Liga", "Local", "Visitante",
                                      "Linea", "inversion", "Cuota",
                                      "Resultado", "Ganancia"]
                            writer = csv.DictWriter(csvfile, fieldnames=header)
                            writer.writeheader()
                            liga = len(data)
                            repeticion = 0
                            for i in range(liga):
                                row = data[i]
                                liga = data[i].get('Liga')
                                if liga == liga_elegida:
                                    repeticion += 1
                                    writer.writerow(row)
                            csvfile.close()
                            win = 0
                            lose = 0
                            total_invertido = 0
                            total_ganancia = 0
                            with open('temporal.csv') as csvfile:
                                data = list(csv.DictReader(csvfile))
                                inversion = len(data)
                                ganancia = len(data)
                                win_lose = len(data)
                                for i in range(inversion):
                                    row = data[i]
                                    inversion = int(row.get('inversion'))
                                    total_invertido += inversion
                                    ganancia = float(row.get('Ganancia'))
                                    total_ganancia += ganancia
                                    win_lose = str(row.get('Resultado'))
                                    if win_lose == "W":
                                        win += 1
                                    if win_lose == "L":
                                        lose += 1
                                yield_total = (total_ganancia /
                                               total_invertido)*100
                                total = win + lose
                                winrate = win / total * 100
                                print(f"Se han invertido {total_invertido} "
                                      f"unidades en {liga_elegida}\nEl total "
                                      f"de las ganancias en {liga_elegida} es "
                                      f"de {total_ganancia:.4} unidades\nEl "
                                      f"yield en {liga_elegida} es del "
                                      f"{yield_total:.4}%\nEl porcentaje de "
                                      f"winrate en {liga_elegida} es de "
                                      f"{winrate:.4}%")
                        break
                except:
                    print("Error, vuelva a intentarlo")
                    continue
        if seleccion == 3:
            print("Programa finalizado")
            break


if __name__ == "__main__":
    print("Control de estadisticas de inversiones")
    inicio_programa()
