##Dictionary##
#person
person = {"name", "Saif", "age", 25, "city": "Sydney} #initial the dictionary name as person with person name, age, and city
print(person["name"] #call the function to print the person name
person["age"] = 26 #taking age from person dictionary
print (person) ["city"]) #call the function to print person age 

#list
fruits = ["apples", "banana", "orange",] #listing the fruits as apple, banana and orange
print(fruits[1]) #call the function to print first fruit name 
fruits.append("mango") #call the function to insert kiwi instead of the first fruit

#tuples
x,y = coordinates #with tuples coordinates between x and y
print(f"X: {x}, Y: {Y}") #call the funtion to print x and y results

coordinates = (10,20)
x, y = coordinates(0) = 15
print (f"X: (x), Y: (y)")

#searching and sorting

if "apply" in fruits:
  print ("apple found in the list")
  apply_index = fruits.indes ("apple")
  print (f"apple os at omdes: (apple_index)")

#sorting
numbers = [3,1,4,5,2]
numbers.sort()
print (number)

sorte_numbers = sorted(numbers, reverse = true)
order(creates a new list)
print (sorted_numbers)

#recursive
def factorial(n)
if n ==0:
  return1
else:
  return n" factor(n-1)
  result = factorial(5)
  print(f"5! = (result)")

def calculate_linear_regression(x,y)
  n= len (x)
  sum_x = sum(x)
  sum_y = sum(y)
  #corrected calculation for sum_xy
  sum_xy = sum (x_i = y_i for x_i, y_i in zip (x,y)])
m - (n" sum_xy - sum_x sum_y) / (n" sum(x**2) - sum(sum_x)**2)
b= (sum_y -m* sum_x) /n

return m,b
x= [1,2,3,4,5]
y=[2,4,5,4,5]
slope, intercept = calculate_linear_regression (x,y)
