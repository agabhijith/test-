temprature = int(input("enter the temprature"))
scale = str(input("Is this in (C)Celsius or (F)Fahrenheit?"))
if scale=="C" or scale=="c":
  Fahrenheit = (9/5*temprature)+32
  print(temprature,"celsius is ",Fahrenheit,"Fahrenhite")
elif scale=="F"or scale=="f":
 Celsius=(5/9*(temprature-32))
 print(temprature,"Fahrenhite is",Celsius,"Celsius")
