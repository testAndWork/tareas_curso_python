def clave(password):

        validar=False
        long=len(password) 
        espacio=False  
        minuscula=False 
        numeros=False 
        correcto=True 
        
        for carac in password: 

            if carac.isspace()==True: 
                espacio=True 
    
            if carac.islower()== True: 
                minuscula=True 
                
            if carac.isdigit()== True: 
                numeros=True 
                            
        if espacio==True: 
                print("La contraseña no puede contener espacios")
        else:
            validar=True 
                       
        if long <8 and validar==True:
            print("Mínimo 8 caracteres")
            validar=False 

        if  minuscula ==True and numeros == True and validar ==True:
           validar = True
        else:
           correcto=False 
           
        if validar == True and correcto==False:
           print("Debe contener al menos una letra y un números ")

        if validar == True and correcto ==True:
           return True