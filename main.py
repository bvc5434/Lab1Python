#Author Brendan Corso bvc5434@psu.edu
#Collaborator Wenjun Ju wkj5070@psu.edu
#Collaborator Hanbit Kim hqk5400@psu.edu
temp = input("Enter temperature: ")
temp = float(temp)
units = input("Enter unit in F/f or C/c: ")
if (units == "C" or units == "c"):
  print(f"{temp}° in Celsius is equivalent to {32+((temp/5)*9)}° Fahrenheit.")
elif (units == "F" or units == "f"):
  print(f"{temp}° in Fahrenheit is equivalent to {5*(temp-32)//9}° Celsius.")
else:
  print(f"Invalid unit({units}).")