tuplefruits=("apple","banana","cherry")#tuple
listfruits=["apple","banana","cherry"]#list
print("original tuple:",tuplefruits)
print("original list:",listfruits)
#เปลี่ยนค่าในtuple
x=list(tuplefruits)#แปลงเป็นlistแล้วเก็บในตัวแปรx
x[1]="blueberry"
tuplefruits=tuple(x)
print("เปลี่ยนค่าtuple:",tuplefruits)
#เพิ่มค่าในtuple
x=list(tuplefruits)
x.append("melon")
tuplefruits=tuple(x)
print("เพิ่มค่าtuple:",tuplefruits)
#ลบtuple
x=list(tuplefruits)
x.remove("cherry")
tuplefruits=tuple(x)
print("ลบtuple:",tuplefruits)
#join tuple
vege=("tomato","cucumber","onion")
fruitVege=tuplefruits+vege
print(fruitVege)
x=range(3,6)#จะหยุดก่อนค่าstop
for n in x:
    print("range x:",n)
y=range(3,20,2)
for m in y:
    print("range y:",m)
    #สุหัชชา สุทธศิริ ม.6/11  เลขที่18 