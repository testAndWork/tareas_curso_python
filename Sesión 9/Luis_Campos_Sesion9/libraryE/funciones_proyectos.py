proyecto = []
def agregar_proyecto(proyecto, descripcion,fecha):
    proyecto.append({'Proyecto':proyecto,'Descripcion':descripcion,'Fecha':fecha})
def mostrar_proyecto():
    for it in proyecto:
        print(f"Proyectp:{it['Proyecto']},Descripcion:{it['Descripcion']},fecha Vencimiento{it['Fecha']}")


    
def eliminar_proyecto(proyecto):
    eliminar = False
    for it in proyecto:
        if proyecto.lower() in it ['Proyecto'].lower():
            print(f"Proyectp:{it['Proyecto']},Descripcion:{it['Descripcion']},fecha Vencimiento{it['Fecha']}")
            proyecto.remove(it)
            eliminar = True
            break
    if not eliminar:
        print('no exite el proyecto')

