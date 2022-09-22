while True:
   jan = float(input("Balance de cierre de ENERO"))
   feb = float(input("Balance de cierre de FEBRERO"))
   mar = float(input("Balance de cierre de MARZO"))
   aph = float(input("Balance de cierre de ABRIL"))
   may = float(input("Balance de cierre de MAYO"))
   jun = float(input("Balance de cierre de JUNIO"))
   jul = float(input("Balance de cierre de JULIO"))
   aug = float(input("Balance de cierre de AGOSTO"))
   sep =float(input("Balance de cierre de SEPTIEMBRE"))
   oct = float(input("Balance de cierre de OCTUBRE"))
   nov = float(input("Balance de cierre de NOVIEMBRE"))
   dec = float(input("Balance de cierre de DICIEMBRE"))

   sum = jan+feb+mar+aph+may+jun+jul+aug+sep+oct+nov+dec
   prom = sum/4
   print ("El promedio del balance general del año es", sum)

   x = input("¿Quieres volver a calcular?")
   if (x == "no"):
    break
  

 
      
