meva = ['olma ','uzum','nok','shaftoli']
for a in meva:
    print(a)
    if a==('nok') :
        break

list=[1,2,3,0,4,5,6]
for n in list:
    if n ==0:
        list.remove(n)
        list.append(n)
        print(list)

list=[1,2,3,4,5,6,7,100]
total=0
for num in list:
    total += num
    print("Ruyxatdagi sonlar yig'indisi: ", total)


list=[1,2,3,0,4,5,6,66,55 ]
for num in list:
    if  num % 2 == 0:
        print('juft son')
    else:
        print('toq son')    



list=[1,2,3,0,4,5,6,66,55 ]
kv=[]
for c in list:
    if c % 2 == 0:
        kv.append(c**2)
    else:
        print("Xatoli bor")    
print("Juft sonlarning kvadrati: " , kv)       

#Foydalanuvchi nechta ruyxat kiritishi suralsin va kiritilgan ma'lumot orasida takrorlangani kursatilsin
son=int(input("Xoxlagan sonni kiriting: "))
ruyxat=[int(x) for x in input("ruyxatni kirit ").split(",")]
count=0
for k in ruyxat:
    if k ==son:
        count+=1
        print(f"{son}soni ruyxatda{count}marta takrorlndi")