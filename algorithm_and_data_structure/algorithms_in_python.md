
# Problem Solving with Algorithms and Data Structures using Python

[url](https://interactivepython.org/runestone/static/pythonds/index.html)

## 1.8. Getting Started with Data


```python
print(2 ** 10)
print(2** 100)
print(7//3)
print(7/3)
print(7%3)
```

### 1.8.2. Built-in Collection Data Types

### 1. lists

** Lists are heterogeneous, meaning that the data objects need not all be from the same class and the collection can be assigned to a variable as below. **

| **Operation Name** | **Operator** | **Explanation** |
| --- | --- | --- |
| indexing | [ ] | Access an element of a sequence |
| concatenation | + | Combine sequences together |
| repetition | * | Concatenate a repeated number of times |
| membership | in | Ask whether an item is in a sequence |
| length | len | Ask the number of items in the sequence |
| slicing | [ : ] | Extract a part of a sequence |


```python
fakeList = ['str', 12, True, 1.232] # heterogeneous
print(fakeList)
myList = [1,2,3,4]
A = [myList]*3
print(A)
myList[2]=45454545
print(A)
```

| **Method Name** | **Use** | **Explanation** |
| --- | --- | --- |
| ` append ` | ` alist.append(item) ` | Adds a new item to the end of a list |
| ` insert ` | ` alist.insert(i,item) ` | Inserts an item at the ith position in a list |
| ` pop ` | ` alist.pop() ` | Removes and returns the last item in a list |
| ` pop ` | ` alist.pop(i) ` | Removes and returns the ith item in a list |
| ` sort ` | ` alist.sort() ` | Modifies a list to be sorted |
| ` reverse ` | ` alist.reverse() ` | Modifies a list to be in reverse order |
| ` del ` | ` del alist[i] ` | Deletes the item in the ith position |
| ` index ` | ` alist.index(item) ` | Returns the index of the first occurrence of ` item ` |
| ` count ` | ` alist.count(item) ` | Returns the number of occurrences of ` item ` |
| ` remove ` | ` alist.remove(item) ` | Removes the first occurrence of ` item ` |


```python
myList = [1024, 3, True, 6.5]
myList.append(False)
print(myList)
myList.insert(2,4.5)
print(myList)
print(myList.pop())
print(myList)
print(myList.pop(1))
print(myList)
myList.pop(2)
print(myList)
myList.sort()
print(myList)
myList.reverse()
print(myList)
print(myList.count(6.5))
print(myList.index(4.5))
myList.remove(6.5)
print(myList)
del myList[0]
print(myList)
```


```python
print(list(range(10)))
print(list(range(5,10)))
print(list(range(5,10,2)))
print(list(range(10,1,-1)))
```

### 2. Strings

| **Method Name** | **Use** | **Explanation** |
| --- | --- | --- |
| `  center  ` | `  astring.center(w)  ` | Returns a string centered in a field of size `  w  ` |
| `  count  ` | `  astring.count(item)  ` | Returns the number of occurrences of `  item  ` in the string |
| `  ljust  ` | `  astring.ljust(w)  ` | Returns a string left-justified in a field of size `  w  ` |
| `  lower  ` | `  astring.lower()  ` | Returns a string in all lowercase |
| `  rjust  ` | `  astring.rjust(w)  ` | Returns a string right-justified in a field of size `  w  ` |
| `  find  ` | `  astring.find(item)  ` | Returns the index of the first occurrence of `  item  ` |
| `  split  ` | `  astring.split(schar)  ` | Splits a string into substrings at `  schar  ` |


```python
myName= "David"
print(myName[3])
print(myName*2)
print(len(myName))
print(myName.upper())
print('.' + myName.center(10) + '.')
print('.' + myName.ljust(10) + '.')
print('.' + myName.rjust(10) + '.')
print(myName.find('v'))
print(myName.split('v'))
```

 ** A major difference between lists and strings is that lists can be modified while strings cannot. This is referred to as mutability. Lists are mutable; strings are immutable. For example, you can change an item in a list by using indexing and assignment. With a string that change is not allowed. **

### 3. Tuples

** Tuples are very similar to lists in that they are heterogeneous sequences of data. The difference is that a tuple is immutable, like a string. A tuple cannot be changed.  **


```python
myTuple = (2,True,4.96)
print(myTuple)
print(len(myTuple))
```

**However, if you try to change an item in a tuple, you will get an error. Note that the error message provides location and reason for the problem.**


```python
myTuple[1]=False
```

### 4. Set

**A set is an unordered collection of zero or more immutable Python data objects. Sets do not allow duplicates and are written as comma-delimited values enclosed in curly braces. The empty set is represented by set(). Sets are heterogeneous, and the collection can be assigned to a variable as below.**


```python
print({3,6,"cat",4.5,False})
mySet = {3,6,"cat",4.5,False}
print(mySet)
```

| **Operation Name** | **Operator** | **Explanation** |
| --- | --- | --- |
| membership | in | Set membership |
| length | len | Returns the cardinality of the set |
| &#124; | aset &#124; otherset | Returns a new set with all elements from both sets |
| ` & ` | ` aset & otherset ` | Returns a new set with only those elements common to both sets |
| ` - ` | ` aset - otherset ` | Returns a new set with all items from the first set not in second |
| ` <= ` | ` aset <= otherset ` | Asks whether all elements of the first set are in the second |

| **Method Name** | **Use** | **Explanation** |
| --- | --- | --- |
| ` union ` | ` aset.union(otherset) ` | Returns a new set with all elements from both sets |
| ` intersection ` | ` aset.intersection(otherset) ` | Returns a new set with only those elements common to both sets |
| ` difference ` | ` aset.difference(otherset) ` | Returns a new set with all items from first set not in second |
| ` issubset ` | ` aset.issubset(otherset) ` | Asks whether all elements of one set are in the other |
| ` add ` | ` aset.add(item) ` | Adds item to the set |
| ` remove ` | ` aset.remove(item) ` | Removes item from the set |
| ` pop ` | ` aset.pop() ` | Removes an arbitrary element from the set |
| ` clear ` | ` aset.clear() ` | Removes all elements from the set |


```python
mySet = {3,6,"cat",4.5,False}
print(mySet)
yourSet = {99,3,100}
print(yourSet)

print( mySet.union(yourSet))
print( mySet | yourSet)

print( mySet.intersection(yourSet))
print( mySet & yourSet)

print( mySet.difference(yourSet))
print( mySet - yourSet)

print( {3,100}.issubset(yourSet))
print( {3,100}<=yourSet)

mySet.add("house")
print( mySet)

mySet.remove(4.5)
print( mySet)

mySet.pop()
print( mySet)

mySet.clear()
print( mySet)
```

### 5. Dictionary

**Dictionaries are collections of associated pairs of items where each pair consists of a key and a value. This key-value pair is typically written as key:value. Dictionaries are written as comma-delimited key:value pairs enclosed in curly braces. For example,**


```python
capitals = {'Iowa':'DesMoines','Wisconsin':'Madison'}
print(capitals)
print(capitals['Iowa'])
capitals['Utah']='SaltLakeCity'
print(capitals)
capitals['California']='Sacramento'
print(len(capitals))
for k in capitals:
   print(capitals[k]," is the capital of ", k)
```

| **Operator** | **Use** | **Explanation** |
| --- | --- | --- |
| ` [] ` | ` myDict[k] ` | Returns the value associated with ` k `, otherwise its an error |
| ` in ` | ` key in adict ` | Returns ` True ` if key is in the dictionary, ` False ` otherwise |
| ` del ` | del ` adict[key] ` | Removes the entry from the dictionary |


| **Method Name** | **Use** | **Explanation** |
| --- | --- | --- |
| ` keys ` | ` adict.keys() ` | Returns the keys of the dictionary in a dict_keys object |
| ` values ` | ` adict.values() ` | Returns the values of the dictionary in a dict_values object |
| ` items ` | ` adict.items() ` | Returns the key-value pairs in a dict_items object |
| ` get ` | ` adict.get(k) ` | Returns the value associated with ` k `, ` None ` otherwise |
| ` get ` | ` adict.get(k,alt) ` | Returns the value associated with ` k `, ` alt ` otherwise |


```python
phoneext={'david':1410,'brad':1137}
print(phoneext)
print(phoneext.keys())
print(list(phoneext.keys()))
print(phoneext.values())
print(list(phoneext.values()))
print(phoneext.items())
print(list(phoneext.items()))
print(phoneext.get("kent"))
print(phoneext.get("kent","NO ENTRY"))

```

## 1.9. Input and Output


```python
aName = input("Please enter your name ")
print("Your name in all capitals is",aName.upper(),
      "and has length", len(aName))
```


```python
sradius = input("Please enter the radius of the circle ")
radius = float(sradius)
diameter = 2 * radius
print(diameter)
```

### 1.9.1. String Formatting


```python
print("Hello","World")
print("Hello","World", sep="***")
print("Hello","World", end="***")
```


```python
aName = "Anas"
age = 10
print(aName, "is", age, "years old.")
print("%s is %d years old." % (aName, age)) # The % operator is a string operator called the format operator.
```

| **Character** | **Output Format** |
| --- | --- |
| ` d `, ` i ` | Integer |
| ` u ` | Unsigned integer |
| ` f ` | Floating point as m.ddddd |
| ` e ` | Floating point as m.ddddde+/-xx |
| ` E ` | Floating point as m.dddddE+/-xx |
| ` g ` | Use ` %e ` for exponents less than <span class="math"><span class="MathJax_Preview" style="color: inherit; display: none;"> <span class="MathJax" id="MathJax-Element-1-Frame" tabindex="0" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><nobr aria-hidden="true"><span class="math" id="MathJax-Span-1" style="width: 1.432em; display: inline-block;"><span style="display: inline-block; position: relative; width: 1.193em; height: 0px; font-size: 120%;"><span style="position: absolute; clip: rect(1.729em 1001.19em 2.86em -999.997em); top: -2.557em; left: 0em;"><span class="mrow" id="MathJax-Span-2"><span class="mo" id="MathJax-Span-3" style="font-family: STIXGeneral-Regular;">− <span class="mn" id="MathJax-Span-4" style="font-family: STIXGeneral-Regular;">4 <span style="display: inline-block; width: 0px; height: 2.562em;"> <span style="display: inline-block; overflow: hidden; vertical-align: -0.211em; border-left: 0px solid; width: 0px; height: 1.146em;"> </nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>−</mo><mn>4</mn></math> <mo>&amp;#x2212;</mo><mn>4</mn></math>" role="presentation" style="position: relative;"> <script type="math/tex" id="MathJax-Element-1">-4</script> or greater than <span class="math"><span class="MathJax_Preview" style="color: inherit; display: none;"> <span class="MathJax" id="MathJax-Element-2-Frame" tabindex="0" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><nobr aria-hidden="true"><span class="math" id="MathJax-Span-5" style="width: 1.432em; display: inline-block;"><span style="display: inline-block; position: relative; width: 1.193em; height: 0px; font-size: 120%;"><span style="position: absolute; clip: rect(1.67em 1001.13em 2.801em -999.997em); top: -2.557em; left: 0em;"><span class="mrow" id="MathJax-Span-6"><span class="mo" id="MathJax-Span-7" style="font-family: STIXGeneral-Regular;">+ <span class="mn" id="MathJax-Span-8" style="font-family: STIXGeneral-Regular;">5 <span style="display: inline-block; width: 0px; height: 2.562em;"> <span style="display: inline-block; overflow: hidden; vertical-align: -0.139em; border-left: 0px solid; width: 0px; height: 1.004em;"> </nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo>+</mo><mn>5</mn></math> <mo>+</mo><mn>5</mn></math>" role="presentation" style="position: relative;"> <script type="math/tex" id="MathJax-Element-2">+5</script> , otherwise use ` %f ` |
| ` c ` | Single character |
| ` s ` | String, or any Python data object that can be converted to a string by using the ` str ` function. |
| ` % ` | Insert a literal % character |

| **Modifier** | **Example** | **Description** |
| --- | --- | --- |
| number | ` %20d ` | Put the value in a field width of 20 |
| ` - ` | ` %-20d ` | Put the value in a field 20 characters wide, left-justified |
| ` + ` | ` %+20d ` | Put the value in a field 20 characters wide, right-justified |
| ` 0 ` | ` %020d ` | Put the value in a field 20 characters wide, fill in with leading zeros. |
| ` . ` | ` %20.2f ` | Put the value in a field 20 characters wide with 2 characters to the right of the decimal point. |
| ` (name) ` | ` %(name)d ` | Get the value from the supplied dictionary using ` name ` as the key. 


```python
price = 24
item = "banana"
print("The %s costs %d cents"%(item,price))
print("The %+10s costs %5.2f cents"%(item,price))
print("The %+10s costs %10.2f cents"%(item,price))
itemdict = {"item":"banana","cost":24}
print("The %(item)s costs %(cost)7.1f cents"%itemdict)

```

## 1.10. Control Structures

** algorithms require two important control structures: iteration and selection. **

#### - Iteration 
#### 1. While


```python
counter = 1
while counter <= 5:
   print("Hello, world")
   counter = counter + 1
```

#### 2. for


```python
for item in [1,3,6,2,5]:
    print(item)
```


```python
for item in range(5):
...    print(item**2)
```


```python
wordlist = ['cat','dog','rabbit']
letterlist = [ ]
for aword in wordlist:
    for aletter in aword:
        if(aletter not in letterlist):
            letterlist.append(aletter)
print(letterlist)
```

### list comprehension


```python
sqlist=[]
for x in range(1,11):
         sqlist.append(x*x)
print(sqlist)        

sqlist2=[x*x for x in range(1,11)] # list comprehension
print(sqlist2)
```


```python
sqlist=[x*x for x in range(1,11) if x%2 != 0]
print(sqlist)
```


```python
[ch.upper() for ch in 'comprehension' if ch not in 'aeiou']
```


```python
wordlist = ['cat','dog','rabbit']

uniqueLetters = [letter for word in wordlist for letter in word]
print(uniqueLetters)
```

## 1.12. Defining Functions

#### problem 
Here’s a self check that really covers everything so far. You may have heard of the infinite monkey theorem? The theorem states that a monkey hitting keys at random on a typewriter keyboard for an infinite amount of time will almost surely type a given text, such as the complete works of William Shakespeare. Well, suppose we replace a monkey with a Python function. How long do you think it would take for a Python function to generate just one sentence of Shakespeare? The sentence we’ll shoot for is: “methinks it is like a weasel”

You’re not going to want to run this one in the browser, so fire up your favorite Python IDE. The way we’ll simulate this is to write a function that generates a string that is 27 characters long by choosing random letters from the 26 letters in the alphabet plus the space. We’ll write another function that will score each generated string by comparing the randomly generated string to the goal.

A third function will repeatedly call generate and score, then if 100% of the letters are correct we are done. If the letters are not correct then we will generate a whole new string.To make it easier to follow your program’s progress this third function should print out the best string generated so far and its score every 1000 tries.


```python
import string
import random
import time

start_time = time.time()

def generate_new_sentense():
    sentense = [random.choice(string.ascii_lowercase + " ") for x in range(28) ]
    return "".join(sentense)

def compare_sentences(guess):
    target_sentence = "methinks it is like a weasel"
    return guess == target_sentence

def main():
    i= 0
    print (i)
    guess = generate_new_sentense()
    print (guess)
    while not compare_sentences(guess):
        guess = generate_new_sentense()
        print (guess)
        i+= 1
        print (i)
# main()

print("--- %s seconds ---" % (time.time() - start_time))
```

## 1.13. Object-Oriented Programming in Python: Defining Classes

### 1.13.1. A Fraction Class


```python
class Fraction:
    
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def show(self):
     print(self.num,"/",self.den)
    
    # Overriding the default __str__ function
    def __str__(self):
        return str(self.num)+"/"+str(self.den)
    
    def __add__(self,otherfraction):

     newnum = self.num*otherfraction.den + self.den*otherfraction.num
     newden = self.den * otherfraction.den

     return Fraction(newnum,newden)
        
myfraction = Fraction(3,5)
print(myfraction)
print(myfraction.show())
f1=Fraction(1,4)
f2=Fraction(1,2)
f3=f1+f2
print(f3)
    
```

### 1.13.2. Inheritance: Logic Gates and Circuits


```python
class LogicGate:

    def __init__(self,n):
        self.name = n
        self.output = None

    def getName(self):
        return self.name

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output


class BinaryGate(LogicGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter Pin A input for gate "+self.getName()+"-->"))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter Pin B input for gate "+self.getName()+"-->"))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self,source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                print("Cannot Connect: NO EMPTY PINS on this gate")


class AndGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a ==1 or b==1:
            return 1
        else:
            return 0

class UnaryGate(LogicGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pin = None

    def getPin(self):
        if self.pin == None:
            return int(input("Enter Pin input for gate "+self.getName()+"-->"))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self,source):
        if self.pin == None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")


class NotGate(UnaryGate):

    def __init__(self,n):
        UnaryGate.__init__(self,n)

    def performGateLogic(self):
        if self.getPin():
            return 0
        else:
            return 1


class Connector:

    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate


def main():
   g1 = AndGate("G1")
   g2 = AndGate("G2")
   g3 = OrGate("G3")
   g4 = NotGate("G4")
   c1 = Connector(g1,g3)
   c2 = Connector(g2,g3)
   c3 = Connector(g3,g4)
   print(g4.getOutput())

main()

```

# 2. Algorithm Analysis

## 2.2. What Is Algorithm Analysis?


```python
def sumOfN(n):
   start = time.time()

   theSum = 0
   for i in range(1,n+1):
      theSum = theSum + i

   end = time.time()

   return theSum,end-start

for i in range(5):
       print("Sum is %d required %10.7f seconds"%sumOfN(1000000))
```

## 2.3. Big-O Notation

**  The order of magnitude function describes the part of T(n) that increases the fastest as the value of n increases. Order of magnitude is often called Big-O notation (for “order”) and written as O(f(n)).**

** It provides a useful approximation to the actual number of steps in the computation. The function f(n) provides a simple representation of the dominant part of the original T(n).**

- The parameter n is often referred to as the “size of the problem,” and we can read this as “T(n) is the time it takes to solve a problem of size n” 

As another example, suppose that for some algorithm, the exact number of steps is

**T(n)=5nˆ2+27n+1005**

When n is small, say 1 or 2, the constant 1005 seems to be the dominant part of the function. However, as n gets larger, the nˆ2 term becomes the most important.

In fact, when n is really large, the other two terms become insignificant in the role that they play in determining the final result

Again, to approximate T(n) as n gets large, we can ignore the other terms and focus on 5nˆ2.

In addition, the coefficient 5 becomes insignificant as n gets large. 

We would say then that the function T(n) has an order of magnitude **f(n)=n2**, or simply that it is **O(n2)**.

- Although we do not see this in the summation example, sometimes the performance of an algorithm depends on the exact values of the data rather than simply the size of the problem.
- For these kinds of algorithms we need to characterize their performance in terms of **best case**, **worst case**, or **average case** performance. 
- The worst case performance refers to a particular data set where the algorithm performs especially poorly. Whereas a different data set for the exact same algorithm might have extraordinarily good performance. However, in most cases the algorithm performs somewhere in between these two extremes (average case). It is important for a computer scientist to understand these distinctions so they are not misled by one particular case.

- ** A number of very common order of magnitude functions will come up over and over as you study algorithms **

| **f(n)** | **Name** |
| --- | --- |
| 1 | Constant |
| log⁡ n | Logarithmic |
|n|Linear|
|n log n|Log Linear|
|nˆ2|Quadratic|
|nˆ3|Cubic|
|2ˆn|Exponential|


```python
# import matplotlib.pyplot as plt
# import math
# 
# n = 50
# 
# x = list(range(1,n))
# 
# linear = [x for x in range(1, n)]
# Quadratic = [x**2 for x in range(1, n)]
# LogLinear = [x * math.log(x) for x in range(1, n)]
# Cubic = [x**3 for x in range(1, n)]
# Exponential = [2**x for x in range(1, n)]
# logarithmic = [math.log(x) for x in range(1, n)]
# 
# plt.plot(x, linear,'k--', label='linear')
# plt.plot(x, Quadratic, 'k:', label='Quadratic')
# plt.plot(LogLinear, x,  'y', label='LogLinear')
# plt.plot(Cubic, x,  'b', label='Cubic')
# plt.plot(Exponential, x,  'r', label='Exponential')
# plt.plot(logarithmic, x,  'g', label='logarithmic')
#     
# legend = plt.legend(shadow=True)
# 
# plt.grid(True)
# plt.show()
```


```python
a=5
b=6
c=10
for i in range(n):
   for j in range(n):
      x = i * i
      y = j * j
      z = i * j
for k in range(n):
   w = a*k + 45
   v = b*b
d = 33
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-1-6b28947f7f99> in <module>()
          2 b=6
          3 c=10
    ----> 4 for i in range(n):
          5    for j in range(n):
          6       x = i * i


    NameError: name 'n' is not defined


The number of assignment operations is the sum of four terms.
- The first term is the constant 3, representing the three assignment statements at the start of the fragment. 
- The second term is 3nˆ2, since there are three statements that are performed nˆ2 times due to the nested iteration.
- The third term is 2n, two statements iterated n times. 
- Finally, the fourth term is the constant 1, representing the final assignment statement. 

** This gives us T(n)=3+3n2+2n+1=3nˆ2+2n+4.**
- By looking at the exponents, we can easily see that the n2 term will be dominant and therefore this fragment of code is **O(n2)**. 
- Note that all of the other terms as well as the coefficient on the dominant term can be ignored as n grows larger.

## 2.6. Lists


```python
import timeit

def test1():
    l = []
    for i in range(1000):
        l = l + [i]

def test2():
    l = []
    for i in range(1000):
        l.append(i)

def test3():
    l = [i for i in range(1000)]

def test4():
    l = list(range(1000))

t1 = timeit.Timer("test1()", "from __main__ import test1")
print("concat ",t1.timeit(number=1000), "milliseconds")
t2 = timeit.Timer("test2()", "from __main__ import test2")
print("append ",t2.timeit(number=1000), "milliseconds")
t3 = timeit.Timer("test3()", "from __main__ import test3")
print("comprehension ",t3.timeit(number=1000), "milliseconds")
t4 = timeit.Timer("test4()", "from __main__ import test4")
print("list range ",t4.timeit(number=1000), "milliseconds")
    
    
```

    concat  1.7699696729996504 milliseconds
    append  0.13472631799959345 milliseconds
    comprehension  0.06414369599951897 milliseconds
    list range  0.027503831001013168 milliseconds


### Big-O efficiency of all the basic list operations.

| Operation | Big-O Efficiency |
| --- | --- |
| index [] | O(1) |
| index assignment | O(1) |
| append | O(1) |
| pop() | O(1) |
| pop(i) | O(n) |
| insert(i,item) | O(n) |
| del operator | O(n) |
| iteration | O(n) |
| contains (in) | O(n) |
| get slice [x:y] | O(k) |
| del slice | O(n) |
| set slice | O(n+k) |
| reverse | O(n) |
| concatenate | O(k) |
| sort | O(n log n) |
| multiply | O(nk) |


```python
popzero = timeit.Timer("x.pop(0)",
                       "from __main__ import x")
popend = timeit.Timer("x.pop()",
                      "from __main__ import x")

x = list(range(2000000))
print(popzero.timeit(number=1000))

x = list(range(2000000))
print(popend.timeit(number=1000))

```

    2.0001414050002495
    0.0001734589986881474


### 2.7. Dictionaries

| operation | Big-O Efficiency |
| --- | --- |
| copy | O(n) |
| get item | O(1) |
| set item | O(1) |
| delete item | O(1) |
| contains (in) | O(1) |
| iteration | O(n) |


```python
import timeit
import random

for i in range(10000,1000001,20000):
    t = timeit.Timer("random.randrange(%d) in x"%i,
                     "from __main__ import random,x")
    x = list(range(i))
    lst_time = t.timeit(number=1000)
    x = {j:None for j in range(i)}
    d_time = t.timeit(number=1000)
    print("%d,%10.3f,%10.3f" % (i, lst_time, d_time))
```

    10000,     0.103,     0.002
    30000,     0.301,     0.002
    50000,     0.529,     0.002
    70000,     0.877,     0.003
    90000,     0.929,     0.002
    110000,     1.110,     0.002
    130000,     1.376,     0.002
    150000,     1.527,     0.002
    170000,     1.962,     0.002
    190000,     1.979,     0.002
    210000,     2.175,     0.002
    230000,     2.721,     0.005
    250000,     2.985,     0.002
    270000,     2.802,     0.002
    290000,     3.118,     0.002
    310000,     3.164,     0.002
    330000,     4.165,     0.003
    350000,     3.769,     0.002
    370000,     3.790,     0.002
    390000,     4.084,     0.002
    410000,     4.605,     0.002
    430000,     4.605,     0.002
    450000,     4.950,     0.002
    470000,     6.394,     0.002
    490000,     5.430,     0.002
    510000,     6.333,     0.003
    530000,     6.862,     0.014
    550000,     7.888,     0.005
    570000,     7.595,     0.002
    590000,     7.948,     0.003
    610000,     7.080,     0.002
    630000,     7.594,     0.002
    650000,     7.462,     0.007
    670000,    12.589,     0.002
    690000,     7.865,     0.002
    710000,     8.667,     0.003
    730000,    11.376,     0.002
    750000,     8.795,     0.004
    770000,     8.360,     0.002
    790000,    11.220,     0.003
    810000,     9.495,     0.002
    830000,     9.586,     0.002
    850000,     9.897,     0.004
    870000,     9.893,     0.002
    890000,    11.427,     0.005
    910000,    11.262,     0.002
    930000,    13.372,     0.002
    950000,    10.997,     0.002
    970000,    14.072,     0.002
    990000,    13.917,     0.002


# 3. Basic Data Structures

## 3.2. What Are Linear Structures?

- Stacks, queues, deques, and lists are examples of data collections whose items are ordered depending on how they are added or removed. Once an item is added, it stays in that position relative to the other elements that came before and came after it. Collections such as these are often referred to as linear data structures.

- Linear structures can be thought of as having two ends. Sometimes these ends are referred to as the “left” and the “right” or in some cases the “front” and the “rear.” You could also call them the “top” and the “bottom.” The names given to the ends are not significant.

- What distinguishes one linear structure from another is the way in which items are added and removed, in particular the location where these additions and removals occur. For example, a structure might allow new items to be added at only one end. Some structures might allow items to be removed from either end.

## 3.3. What is a Stack?

- A stack (sometimes called a “push-down stack”) is an ordered collection of items where the addition of new items and the removal of existing items always takes place at the same end. 
- This end is commonly referred to as the “top.” The end opposite the top is known as the “base.”
- **LIFO, last-in first-out.**
- Stacks are fundamentally important, as they can be **used to reverse the order of items.** The order of insertion is the reverse of the order of removal.


## 3.4. The Stack Abstract Data Type

#### The stack operations are given below:
- `Stack()` creates a new stack that is empty. It needs no parameters and returns an empty stack.
- `push(item)` adds a new item to the top of the stack. It needs the item and returns nothingpush(item) adds a new item to the top of the stack. It needs the item and returns nothing-.
- `pop()` removes the top item from the stack. It needs no parameters and returns the item. The stack is modifiedpop() removes the top item from the stack. It needs no parameters and returns the item. The stack is modified.
- `peek()` returns the top item from the stack but does not remove it. It needs no parameters. The stack is not modified.
- `isEmpty()` tests to see whether the stack is empty. It needs no parameters and returns a boolean value.
- `size()` returns the number of items on the stack. It needs no parameters and returns an integer.

## 3.5. Implementing a Stack in Python


```python

```
