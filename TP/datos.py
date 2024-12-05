#Servicios
A = "Ensobrado"
B = "Etiquetado"
C = "Diarios"
servicios = [A, B]

M1 = "Maquina 1"
M2 = "Maquina 2"
maquinas = [M1]

LIMITES_PRODUCCION = {
    A: 500_000, # 500.000
    B: 700_000, # 700.000
    C: 500_000 # 500.000
}

PRECIO_VENTA = {
    A: 3.20, # 3.20
    B: 1.28, # 1.28
    C: 3.5 # 3.5 
}

# Recursos
PRECIO_TINTA = 10 # por litro: 10
TINTA_DIARIO = 0.5 # cuantos litros se neceistan para un diario: 0.5

PRECIO_CAJAS = 15
CAPACIDAD_CAJA = { # Cantidad que entra por cada caja que compro del producto
    A: 300,
    B: 450
}

# Maquina
LIMITE_HORAS_MAQUINA = {
    M1: 48, # 48
    M2: 48 # 48
}
PRODUCCION_MAQUINA = {
    M1: 5_000, # Cantidad que puede doblar en una hora: 5.000
    M2: 4_000 # Diaros que puede producir 4.000
}

# Horas hombre
PERSONAL = 13 # 13
DIAS_LABORABLES = 24 # 24
HORAS_BASE = 8 # 8
LIMITE_HORAS_HOMBRE = HORAS_BASE*DIAS_LABORABLES*PERSONAL

PRODUCCION_HORA = {
    A: 600, # 600
    B: 800, # 800
    C: 400 # 400
}
REPARACION_HORA = { # cantidad de reparaciones por hora
    A: 100, # 100
}
PRECIO_HORA_EXTRA = 50 # 50
MAX_CANTIDAD_HORAS_EXTRA_PERSONA = 20 # 20
MAX_HORAS_EXTRA_PERSONAL = PERSONAL * MAX_CANTIDAD_HORAS_EXTRA_PERSONA

PORCENTAJE_RECHAZO_MAQUINA = {
    M1: 0.02 #0.02
}
COSTO_REPARACION_SOBRES = 1.2 # 1.2

# Translado
PRECIO_TRANSLADO = {
    A: 10_000, # 10.000
    C: 12_000 # 12.000
}
CAPACIDAD_TRANSLADO = {
    A: 7_000, # 7.000
    C: 6_000 # 6.000
}

PERSONAL_NECESARIO_MAQUINA = {
    M1: 2, # 2
    M2: 1 # 1
}
COSTOS_FIJOS = 600_000 #600.000