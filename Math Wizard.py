#!/usr/bin/env python
# coding: utf-8

# In[1]:


from array import*
from tabulate import tabulate
from sympy import*
from scipy.misc import derivative
x=Symbol('x')
print("Math Wizard")
c=5
while(c != 4):
    print("1.Newton-Ruphson Method")
    print("2.Bi-section Method")
    print("3.SLE")
    print("4.cancel")
    c=int(input("Enter your choice:"))
    if (c==1):
        print("Newton-Ruphson Method")
        print("a*x**3 + b*x**2+c*x+d")
        a=int(input("enter a="))
        b=int(input("enter b="))
        c=int(input("enter c="))
        d=int(input("enter d="))
        e=a*x**3 + b*x**2 + c*x +d
        print("f(x) : ",e)
        d1=diff(e)
        print("f'(x) : ",d1)
        print("Choose two number such that f(n1)*f(n2)<0")
        n1=int(input("enter n1="))
        n2=int(input("enter n2="))
        di=1
        x2=float(n1)
        ct=0
        t=[]
        while(di>0.0001):
            x1=x2
            x2=x1-float((e.subs(x,x1))/(d1.subs(x,x1)))
            x2=round(x2,4)
            t.insert(ct,[ct,x2])
            di=abs(x2-x1)
            ct+=1
        h=["No. of iterations","value"]  
        print(tabulate(t,headers=h,tablefmt="grid"))
        print("Root: ",x2)
    elif c==2:
        print("Bi-section Method")
        print("a*x**3 + b*x**2+c*x+d")
        a=int(input("enter a="))
        b=int(input("enter b="))
        c=int(input("enter c="))
        d=int(input("enter d="))
        e=a*x**3 + b*x**2 + c*x +d
        print("f(x) : ",e)
        print("Choose two number such that f(n1)*f(n2)<0")
        n1=int(input("enter n1="))
        n2=int(input("enter n2="))
        if(float(e.subs(x,n1))>0 and float(e.subs(x,n2))<0):
                 n1,n2=n2,n1
        xm=float((n1+n2)/2)
        di=1
        ct=1
        t=[]
        while(di>0.0001):     
            r=float((e.subs(x,xm)))
            if r<0:
                    n1=xm
            elif r>0:
                    n2=xm 
            xm1=xm
            xm=float((n1+n2)/2)
            xm=round(xm,3)
            t.insert(ct,[ct,xm])
            di=abs(xm-xm1)
            ct+=1
        h=["No. of iterations","value"]  
        print(tabulate(t,headers=h,tablefmt="grid"))
        print("Root: ",xm)
    elif c==3:
        x=Symbol('x')
        y=Symbol('y')
        z=Symbol('z')
        print("SLE")
        print("a1*x+b1*y+c1*z=d1")
        a1=int(input("enter a1="))
        b1=int(input("enter b1="))
        c1=int(input("enter c1="))
        d1=int(input("enter d1="))
        print("a2*x+b2*y+c2*z=d2")
        a2=int(input("enter a2="))
        b2=int(input("enter b2="))
        c2=int(input("enter c2="))
        d2=int(input("enter d2="))
        print("a3*x+b3*y+c3*z=d3")
        a3=int(input("enter a3="))
        b3=int(input("enter b3="))
        c3=int(input("enter c3="))
        d3=int(input("enter d3="))
        dc=int(input("enter the decimal point="))
        ex=(d1-b1*y-c1*z)/a1
        ey=(d2-a2*x-c2*z)/b2
        ez=(d3-b3*y-a3*x)/c3
        z1=0.0
        y1=0.0
        x1=0.0
        di1=1
        di2=1
        di3=1
        ct=1
        t=[]
        while(di1>0.0001 and di2>0.0001 and di3>0.0001):
            x2=x1
            y2=y1
            z2=z1
            x1=float((ex.subs([(y, y1), (z, z1)])))
            y1=float((ey.subs([(x, x1), (z, z1)])))
            z1=float((ez.subs([(y, y1), (x, x1)])))
            x1=round(x1,dc)
            y1=round(y1,dc)
            z1=round(z1,dc)
            di1=abs(x1-x2)
            di2=abs(y1-y2)
            di3=abs(z1-z2)
            t.insert(ct,[ct,x1,y1,z1])
            ct+=1
        h=["No. of iterations","value of x","value of y","value of z"]  
        print(tabulate(t,headers=h,tablefmt="grid"))
        print("Root: x= ",x1," y= ",y1," z= ",z1)
    else:
        break


# In[ ]:





# In[ ]:




