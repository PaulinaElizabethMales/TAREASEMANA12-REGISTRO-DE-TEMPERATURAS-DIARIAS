# Lista de ciudades
nombres_ciudades = ["Quito", "Otavalo", "Cuenca"]

# Matriz 3D de temperaturas
temperaturas = [
    [  # Quito
        [{"dia": "Lunes", "temp": 78}, {"dia": "Martes", "temp": 80}, {"dia": "Miércoles", "temp": 82},
         {"dia": "Jueves", "temp": 79}, {"dia": "Viernes", "temp": 85}, {"dia": "Sábado", "temp": 88},
         {"dia": "Domingo", "temp": 92}],
        [{"dia": "Lunes", "temp": 76}, {"dia": "Martes", "temp": 79}, {"dia": "Miércoles", "temp": 83},
         {"dia": "Jueves", "temp": 81}, {"dia": "Viernes", "temp": 87}, {"dia": "Sábado", "temp": 89},
         {"dia": "Domingo", "temp": 93}],
        [{"dia": "Lunes", "temp": 77}, {"dia": "Martes", "temp": 81}, {"dia": "Miércoles", "temp": 85},
         {"dia": "Jueves", "temp": 82}, {"dia": "Viernes", "temp": 88}, {"dia": "Sábado", "temp": 91},
         {"dia": "Domingo", "temp": 95}],
        [{"dia": "Lunes", "temp": 75}, {"dia": "Martes", "temp": 78}, {"dia": "Miércoles", "temp": 80},
         {"dia": "Jueves", "temp": 79}, {"dia": "Viernes", "temp": 84}, {"dia": "Sábado", "temp": 87},
         {"dia": "Domingo", "temp": 91}]
    ],
    [  # Otavalo
        [{"dia": "Lunes", "temp": 62}, {"dia": "Martes", "temp": 64}, {"dia": "Miércoles", "temp": 68},
         {"dia": "Jueves", "temp": 70}, {"dia": "Viernes", "temp": 73}, {"dia": "Sábado", "temp": 75},
         {"dia": "Domingo", "temp": 79}],
        [{"dia": "Lunes", "temp": 63}, {"dia": "Martes", "temp": 66}, {"dia": "Miércoles", "temp": 70},
         {"dia": "Jueves", "temp": 72}, {"dia": "Viernes", "temp": 75}, {"dia": "Sábado", "temp": 77},
         {"dia": "Domingo", "temp": 81}],
        [{"dia": "Lunes", "temp": 61}, {"dia": "Martes", "temp": 65}, {"dia": "Miércoles", "temp": 68},
         {"dia": "Jueves", "temp": 70}, {"dia": "Viernes", "temp": 72}, {"dia": "Sábado", "temp": 76},
         {"dia": "Domingo", "temp": 80}],
        [{"dia": "Lunes", "temp": 64}, {"dia": "Martes", "temp": 67}, {"dia": "Miércoles", "temp": 69},
         {"dia": "Jueves", "temp": 71}, {"dia": "Viernes", "temp": 74}, {"dia": "Sábado", "temp": 77},
         {"dia": "Domingo", "temp": 80}]
    ],
    [  # Cuenca
        [{"dia": "Lunes", "temp": 90}, {"dia": "Martes", "temp": 92}, {"dia": "Miércoles", "temp": 94},
         {"dia": "Jueves", "temp": 91}, {"dia": "Viernes", "temp": 88}, {"dia": "Sábado", "temp": 85},
         {"dia": "Domingo", "temp": 82}],
        [{"dia": "Lunes", "temp": 89}, {"dia": "Martes", "temp": 91}, {"dia": "Miércoles", "temp": 93},
         {"dia": "Jueves", "temp": 90}, {"dia": "Viernes", "temp": 87}, {"dia": "Sábado", "temp": 84},
         {"dia": "Domingo", "temp": 81}],
        [{"dia": "Lunes", "temp": 91}, {"dia": "Martes", "temp": 93}, {"dia": "Miércoles", "temp": 95},
         {"dia": "Jueves", "temp": 92}, {"dia": "Viernes", "temp": 89}, {"dia": "Sábado", "temp": 86},
         {"dia": "Domingo", "temp": 83}],
        [{"dia": "Lunes", "temp": 88}, {"dia": "Martes", "temp": 90}, {"dia": "Miércoles", "temp": 92},
         {"dia": "Jueves", "temp": 89}, {"dia": "Viernes", "temp": 86}, {"dia": "Sábado", "temp": 83},
         {"dia": "Domingo", "temp": 80}]
    ]
]

# Cálculo de temperaturas
def calcular_promedio_ciudades(nombres_ciudades, temperaturas):
    """
    Calcula el promedio de temperatura por ciudad durante todo el período.

    Parámetros:
    - nombres_ciudades: lista de nombres de ciudades
    - temperaturas: matriz 3D con temperaturas por ciudad, semana y día

    Retorna:
    - Diccionario con el nombre de la ciudad como clave y su promedio como valor
    """
    promedios_por_ciudad = {}

    for i, ciudad in enumerate(temperaturas):
        suma_total = 0
        conteo_dias = 0

        for semana in ciudad:
            for dia in semana:
                suma_total += dia['temp']
                conteo_dias += 1

        promedio_ciudad = suma_total / conteo_dias
        promedios_por_ciudad[nombres_ciudades[i]] = round(promedio_ciudad, 2)

    return promedios_por_ciudad

# LLaar a la funcion y manda parámetros determinados
resultados = calcular_promedio_ciudades(nombres_ciudades, temperaturas)

for ciudad, promedio in resultados.items():
    print(f"{ciudad}: {promedio}°F")
