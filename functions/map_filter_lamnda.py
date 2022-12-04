f = lambda x : x * 5  # a lambda function
print (f(3), f(2142) , f(-231))

# actual usage of lambda function : when we have a huge data and we have to operate the same function on every data  
x = [23,45,67,22,87,41,82]


x2 = list(map(lambda i : i** 2, x))  # map function
print(x2)

a = [1,4,3,2,5,6]
b = [2,5,3,8,2,9]

ab = list(map(lambda i,j: i * j, a,b)) # map function with multiple list
print (ab)

# filter 
evens = list(filter(lambda i : i % 2 == 0 , x))
print(evens)