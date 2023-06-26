#Q1. Create one variable containing following type of data:
#(i) string
s="I am Feeling Good To Enroll in the Course of Data Science Masters 2.0"
print(s)
#(ii) list
l=[23,54,23,'a','t',3.14,"Ashir"]
print(l)
#(iii) float
f=3.14
print(f)
#(iv) tuple
t=(34,24,65,'ashir',[34,77,93,23])
print(t)
print(t[4][1])

# Q2. Given are some following variables containing data:
#What will be the data type of the above given variable.
# (i) 
var1 = ' '
print(type(var1))
#output
#<class 'str'>

# (ii) 
var2 = '[ DS , ML , Python]'
print(type(var2))
#output
#<class 'str'>

# (iii) 
var3 = [ 'DS' , 'ML' , 'Python' ]
print(type(var3))
#output
#<class 'list'>

# (iv) 
var4 = 1.
print(type(var4))
#output
#<class 'float'>

# Q3. Explain the use of the following operators using an example:
# (i) /
a=5/2
print(a)
#output
#2.5

# (ii) %
b=4%2
print(b)
#output
#0

# (iii) //
c=4//2
print(c)
#output
#2

# (iv) **
d=2**5
print(d)
#output
#32

# Q4. Create a list of length 10 of your choice containing multiple types of data. Using for loop print the
# element and its data type.

l=[34,52.3,53,'alam',64,64,'ashir','Physics', 'Skills','a']
for i in l:
    print(i,type(i))

#Output
# 34 <class 'int'>
# 52.3 <class 'float'>
# 53 <class 'int'>
# alam <class 'str'>
# 64 <class 'int'>
# 64 <class 'int'>
# ashir <class 'str'>
# Physics <class 'str'>
# Skills <class 'str'>
# a <class 'str'>

# Q5. Using a while loop, verify if the number A is purely divisible by number B and if so then how many
# times it can be divisible.

a=10
b=2

if(a%b==0):
    print("Divisible")
else:
    print("Not divisible")


# Q6. Create a list containing 25 int type data. Using for loop and if-else condition print if the element is
# divisible by 3 or not.

l=range(1,25)
for i in l:
    if(i%3==0):
        print(f"**{i} is divisible by 3**")
    else:
        print(f"{i} is not divisible by 3")

# Q7. What do you understand about mutable and immutable data types? Give examples for both showing
# this property.

# Solution:
# Mutable - The value can be changed in the Variable Example- List and Tuple are Mutable.
# Immuatble - The Value cannot be changed in the variable Example - Strings as Immuatble.
