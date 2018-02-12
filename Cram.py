print("WELCOME")
print("LET'S START")
a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
x = "true"
y = 1
z = 15
j = 2
b = [1,2,3,4]
c = [5,6,7,8]
d = [9,10,11,12]
e = [13,14,15,16]
while (x == "true"):
        print("Player ",y)
        m = int(input("Enter First number: "))
        n = int(input("Enter Second number: "))

        if ((n - m == 1 and m%4!=0) or (n - m == 4)or(m - n == 1 and n%4!=0)or(m - n == 4)):
                a.remove(m)
                a.remove(n)
                z = z-2

                if z==1:
                        j = 1
                
                if (n<=4):
                        b.remove(n)
                        b.insert(n-1,'*')
                else:
                        if(n<=8):
                                c.remove(n)
                                w = (n+3)%4
                                c.insert(w,'*')
                        else:
                                if (n<=12):
                                        d.remove(n)
                                        w = (n+3)%4
                                        d.insert(w,'*')
                                else:
                                        e.remove(n)
                                        w = (n+3)%4
                                        e.insert(w,'*') 
                if (m<=4):
                        b.remove(m)
                        b.insert(m-1,'*')
                else:
                        if(m<=8):
                                c.remove(m)
                                w = (m+3)%4
                                c.insert(w,'*')
                        else:
                                if (m<=12):
                                        d.remove(m)
                                        w = (m+3)%4
                                        d.insert(w,'*')
                                else:
                                        e.remove(m)
                                        w = (m+3)%4
                                        e.insert(w,'*') 
                
       
        else:
            
            print("Try Again")

        for i in range(0,z):

            if (a[i+1] - a[i] == 1  or a[i+1] - a[i] == 4 or a[i+j] - a[i] == 1  or a[i+j] - a[i] == 4):
                x = "true"
                break

            else:
                x = "false"
                o = y
            
        if a==[]:
            x = "false"
            o = y

        if y == 2:
            y = 1

        else:
            y += 1

        print(b)
        print(c)
        print(d)
        print(e)

print("THE WINNER IS PLAYER ",o)
