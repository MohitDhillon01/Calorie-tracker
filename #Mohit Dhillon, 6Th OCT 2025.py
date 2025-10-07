#Mohit Dhillon, 6Th OCT 2025 
#Daily Calorie Tracker
print('Welcome')
print('This is a Daily calorie tracker you can track your daily calorie input with it.')
#task2
Meal=[]
Calories=[]
num=int(input('enter the no. of meals you had today:'))
for i in range(1,num+1):
    Mealname=input('enter meal name:')
    Howcal=int(input('enter the number of calories in this meal:'))
    Meal.append(Mealname)
    Calories.append(Howcal)
print(Meal)
print(Calories)
#task3
dailyinput=int(input('enter your daily calorie input limit:'))
totalcalories=sum(Calories)
print('your total calorie input today is:',totalcalories)
#task4
if totalcalories>dailyinput:
    print('WARNING!!! you have exceeded your daily calorie input limit')
else:
    print('GOOD you are within your daily calorie input limit')
avgcalories=totalcalories/num
print('your average calorie input per meal is:',avgcalories)

#food calorie review table 
print("MEAL\t\tCALORIES\tREVIEW")
print('-'*35)

#now loop for both 
for i,j in zip(Meal,Calories):
    if j>1000:
        print(f'{i}\t\t{j}\t\tNot Healthy')
    else:
        print(f'{i}\t\t{j}\t\thealthy')


    
                

