inventario = []
def agregar_inventario(codigo, producto, cantidad,fecha):
    inventario.append({'Codigo':codigo,'Producto':producto,'Cantidad':cantidad,'Fecha':fecha})
def mostrar_inventario():
    for it in inventario:
        print(f"Codigo:{it['Codigo']},Producto:{it['Producto']},Cantidad:{it['Cantidad']} fecha entrada{it['Fecha']}")


    
def eliminar_inventario(codigoproducto):
    eliminar = False
    for it in inventario:
        if codigoproducto.lower() in it ['Codigo'].lower():
            print(f"Codigo:{it['Codigo']},Producto:{it['Producto']},Cantidad:{it['Cantidad']} fecha entrada{it['Fecha']}")
            inventario.remove(it)
            eliminar = True
            break
    if not eliminar:
        print('no exite el producto')


    