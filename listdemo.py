"listdemo.py"
l0=(33,76,98,99,99)
l1=[1,2,3,4,5,5,7,8,8,8,2,9,3,6]
l2=['priyanchu','faizan','jeet']
l3={"name":"oggy","age":20,"regno":120,"branch":"BTIT"}
set1={'a','b','c','d','h','m','l'}
set2={'b','c','d','p','q','r','z'}
print(len(l1))
print(max(l1))
print(min(l1))
print(sum(l1))
print(sorted(l1))
print(l1.count(5))
print(l1.index(7))
print(l1[:4])
print(l1.append(1))
print("the list items are \n")
for i in l1:
    print(i)
print(l1+l2)
print(l1*2)
print(l2[2])
print('cpp' in l2)
print('cpp' not in l1)
print(l1.index(8))
print("the list items are\n")
for i in l2 :
    print(i)
l2.sort()
print(l2)
l2.append('priyanchu')
print(l2)
l2.reverse()
print(l2)
l2.extend(l2)
print(l2)
l2.pop(2)
print(l2)
l2.remove('faizan')
print(l2)
print("name:",l3["name"])
print("age:",l3["age"])
print("branch:",l3["branch"])
l3['age']=31
print("modified dictionary:",l3)
print(set1|set2)
print(set1&set2)
print(set1-set2)