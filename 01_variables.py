# Variables

my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = True
print(my_bool_variable)

# Concatenación de variables en un print
print(my_string_variable, my_int_to_str_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable)

# Algunas funciones del sistema
print(len(my_string_variable))# Suma caracteres espacios incluidos

# Variables en una sola linea (Se puede hacer pero no es muy buena practica)
name, surname, alias, age = "Minerva", "Pedret", "Nervs", 40
print("Me llamo:", name, surname, ". Mi edad es:" , age, ".Y mi alias es:", alias)

# Inpunts
'''name = input("¿Cual es tu nombre?")
age = input("¿Cuantos años tienes?")
print(name)
print(age)
'''

# Cambiamos su tipo
name = 35
age = "Minerva"
print(name)
print(age)

# ¿Forzamos el tipo?
address: str = "Mi dirección"
address = 32
print(type(address))