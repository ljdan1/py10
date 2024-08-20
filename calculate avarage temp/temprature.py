#calculates the daily average temprature relative to other days

Input = int(input("How many day's of temperatures:"))
total=0
for i in range(1,Input+1):
  values=int(input("day "+str(i)+"'s daily temperature:"))
  total +=values
average=round(total/Input,2)
print("the average temperature is "+str(average)+ " degrees.")
