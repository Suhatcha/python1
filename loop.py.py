#for จะเป็น definite loop หรือ loop ที่มีการทำงานที่ชัดเจน
#forกับ
for i in range(1,11,1):
    print(i)
print('finish')
#for กับ list
list1 = ['apple','blueberry','kiwi']
for element in list1:
    print(element)
#loop กับ dic
dic1 ={'name':'soranun','age':30,'้hobbies':'football'}
for key,value in dic1.items():
    print(key,':',value)   
#while indefinite loop หรือ loopที่ทำงานไม่ชัดเจน   
i=1
while i<10:
    print(i)
    i+=1
#นายสุหัชชา สุทธศิริ ม.6/11 เลขที่18