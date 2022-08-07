

def multiplo(num):
    a =[]
    for i in range(2,num):
        if  i%3 == 0 or i%5 == 0:
            a.append(i)
    print ("a",a,)                
    return sum(set(a)) 

print(multiplo(16))

#def solution(number):
 #   return sum([i for i in range(number) if i % 3 == 0 or i % 5 == 0])

#print(solution(4))