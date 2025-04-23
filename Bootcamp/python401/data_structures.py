# %%
"""

Numbers and String

"""
from pyarrow import dictionary

print("Hello World")
print("hi")

type(9)
type(9.2)
type("hello")

float(9.2)
int(9.2)
float(9)



# %%

"""
variables and assignments

"""

a = 9
c = 4
b = "hello"

a * c
a / c # direkt boler
a // c # bolumu yuvarlar
a % c # kalani soyler

# %%

"""
String Methods
"""
name = "Melih"
dir(str)

len(name)
name.upper()
name.lower()
name.replace("l","p")
name.split("i")

"ofofof".strip("o")
"foo".capitalize()
"foo".startswith("f")

# %%

"""
List Methods

* Degistirilebilir
* Siralidir. Index islemi yapabilir.
* Kapsayicidir

"""

notes = [1,2,3,4,5]
notes

type(notes)

names = ["a","b","c"]

not_nam = [1,2,3, "A","B","C", True, [4,5,6]]
not_nam

not_nam[0] = 99

not_nam[0:4] # 4 e kadar

dir(notes)
len(notes)
notes.append("a")

notes.pop(0) # belirtilen indexi siler
notes.insert(0, "a") # indexe ekler
notes

# %%

"""
Dictionary Methods

* Degistirilebilir
* Sirasiz
* Kapsayicidir

"""

dic = {"X": 10,
       "Y": 20,
       "Z": ["test",40]}

dic["Z"][0]

"X" in dic

dic.get("Z") # Z nin valuesini cagirir

dic["Z"][0] = "melih"

dic

dic.keys() # keysleri verir
dic.values() # valuelari verir
dic.items() # tuple seklinde verir

dic.update({"T": 10}) # varsa gunceller yoksa olusturur


# %%

"""
Tuples Methods

* Degistirilemez.
* Siralidir. Index islemi yapabilir.
* Kapsayicidir (yani birden farkli veri yapisini tutabiliyor demek)

"""

t = ("melih", "emin", 1, 2)

t[0]

t[0] = 99 # error

# index degisimi yapmak icin listeye cevrilip oyle yapilir

# %%

"""
Set Methods

* Degistirilebilir.
* Siralidir, Essizdir. Index islemi yapabilir.
* Kapsayicidir

hiz gerektiren islemler yapilabilir
"""

set1 = {1, 2, 3, 4, 5}
set2 = set([1,2,3,4,5,6,7,8,9])

type(set1)

set2.difference(set1) # birinde elemani olup digerinde olmayan
set1.difference(set2)

# iki kumede de birbirlerine gore olmayanlar
set1.symmetric_difference(set2)
set2.symmetric_difference(set1)

# iki kumenin kesisimi
set1.intersection(set2)
set2.intersection(set1)

# kesisim kisa yolu
set1 & set2

# iki kumenin birlesimi
set2.union(set1)
set1.union(set2)

# kesisimler bos mu sorusu ?
set1.isdisjoint(set2)
set2.isdisjoint(set1)

# bir kume diger kumenin alt kumesimi
set1.issubset(set2)

# bir kume diger kumeyi kapsiyor mu
set2.issuperset(set1)

# %%

# Fonksiyona docstring(bilgi notu) ekleme

def test(a):
       """
       standard

       :param a:
       :return a nin parse:
       """
       return a**2

#######################
# Uygulama - Mülakat Sorusu
#######################

# Amaç: Aşağıdaki şekilde string değiştiren fonksiyon yazmak istiyoruz.

# before: "hi my name is john and i am learning python"
# after: "Hi mY NaMe iS JoHn aNd i aM LeArNiNg pYtHoN"

text = "hi my name is john and i am learning python"
n = ""
for i in range(len(text)):
       if i % 2 == 0:
              n += text[i].upper()
       else:
              n += text[i].lower()


# cozum 2

for index, char in enumerate(text):
       if index % 2 == 0:
              n += char.upper()
       else:
              n += char.lower()

# %%
"""
Enumerate Method

otomatik indexler.
"""

students = ["max", "micheal", "stone", "charlie"]

#for index, student in enumerate(students):
 #     print(index, student)

a = []
b = []

for index, student in enumerate(students):
       if index % 2 == 0:
              a.append(student)
       else:
              b.append(student)

print(a,b)

#######################
# Uygulama - Mülakat Sorusu
#######################
# divide_students fonksiyonu yazınız.
# Çift indexte yer alan öğrencileri bir listeye alınız.
# Tek indexte yer alan öğrencileri başka bir listeye alınız.
# Fakat bu iki liste tek bir liste olarak return olsun.


def divide_students(list):
       l1 = []
       l2 = []

       for index, item in enumerate(list):
              if index % 2 == 0:
                     l1.append(item)
              else:
                     l2.append(item)

       c = l1 + l2
       return c

print(divide_students(students))

# %%

"""
Zip method

birlestirici
"""

students = ["John", "Mark", "Venessa", "Mariam"]

departments = ["mathematics", "statistics", "physics", "astronomy"]

ages = [23, 30, 26, 22]

list(zip(students, departments, ages))

# %%

"""
lambda, map, filter, reduce method

"""


def summer(a, b):
    return a + b

summer(1, 3) * 9

new_sum = lambda a, b: a + b

new_sum(4, 5)

# map
salaries = [1000, 2000, 3000, 4000, 5000]

def new_salary(x):
    return x * 20 / 100 + x

new_salary(5000)

for salary in salaries:
    print(new_salary(salary))

list(map(new_salary, salaries))


# del new_sum
list(map(lambda x: x * 20 / 100 + x, salaries))
list(map(lambda x: x ** 2 , salaries))

# FILTER
list_store = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(filter(lambda x: x % 2 == 0, list_store))

# REDUCE
from functools import reduce
list_store = [1, 2, 3, 4]
reduce(lambda a, b: a + b, list_store)

# %%

"""
Comprehensions

 * List
 * Dict

"""


a= ["melih", "emre", "mami"]
b = [1,2,3]

dictm = {k.upper():v for k,v in zip(a,b)}


numbers = range(1,11)

mdict = {x:x**2 for x in numbers if x % 2 == 0}
