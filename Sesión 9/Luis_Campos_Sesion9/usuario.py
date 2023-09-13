import libraryE.contraseña as uc

usuario = input('Ingrese su nombre:')

correcto = True
while correcto ==True:
    contrasenia = input("ingrese contraseña:")
    if uc.clave(contrasenia) == True:
        print("Contraseña creada exitosamente!!!!")
        correcto = False