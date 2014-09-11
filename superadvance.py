#function
#addenum operation
def add(a,b):  #defining add function of parameters a and b
    return a+b
print add(3,5)
print add(4+5j,7+10j)
print add("deepak","victor")
print add([2,3,'d'],[3,4,'p'])
    
#if else statements
a=10
b=20
c=30
if a is 40:
    print a
if b is 20:
    print b
if c is 30:
    print c

#if else ladder #no switch case in python
a=10
b=20
c=30
if a is 40:
    print a
elif b is 20:
    print b
elif c is 30:
    print c

#iterative demo
#In this demo we will systematically fill a list

l1=[]
for i in xrange(10):
    l1.append(i)
    print l1
print l1

#test
l1=[]
for i in xrange(10):
    l1.append(str(i))
    print l1
print l1

#test2
vamshi= "my phone number is:"
for i in xrange(9,-1,-1):
    vamshi=vamshi+str(i)
print vamshi

#list insertion demo
l1=[]
for i in xrange(10):
    l1.insert(0,i)
    print l1

#while logic
d=[]
q=9
while q>-1:
    d.append(str(q))
    q=q-1
    print d

#insert
d=[]
q=0
while q<10:
    d.insert(0,q)
    q=q+1
    print d
    



