for i in range(5):#start, end, step(+1 or +2)

    print("code")
print("goodbye")

#i = 0, i < 5 = T; code; i++
#i = 1, i < 5 = T; code; i++
#i = 2, i < 5 = T; code; i++
#i = 3, i < 5 = T; code; i++
#i = 4, i < 5 = T; code; i++
#i = 5, i < 5 = (False);

def foo():
    for num in range(10, 0, -2):
        print(num)

print("begin")
foo()
print("end")
foo()

#Loop Map
#num = 10; 10 > 0 = T; num =10; num-= 2
#num = 8; 8 > 0 = T; num =8; num-= 2
#num = 6; 6 > 0 = T; num =6; num-= 2
#num = 4; 4 > 0 = T; num =4; num-= 2
#num = 2; 2 > 0 = T; num =2; num-= 2
#num = 0; 0 > 0 = F; 

#Loo