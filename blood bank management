#python code for dash board for blood bank
import os
import webbrowser
def Admin(en,z1,z2,z3,z4,z5,z6,z7,z8):
    x=0
    listn=[]
    listp=[]
    lists=[]
    listc=[]
    c=input('please enter your name :')
    en=input('please enter your password :')
    while(1):
        if(en=='enter'):
            print('welcome '+c+':')
            c1=input('enter the type of blood group :')
            c2=c1.lower()
            break
        else:
            en=input('enter correct password :')
    if(c2=='a+'):
        while(1):
            listn.append(input('enter the name of donor :'))
            p=input('enter the phone number of donor :')
            while(1):
                if(len(p)==10):
                    break
                else:
                    p=input('enter a valid  phone number of donor :')
            listp.append(p)
            listc.append(c2.upper())
            x2=(input('do you want to add another a+ blood group details if yes enter yes else no'))
            z1.write('                  DONOR DETAILS                   \n')
            z1.write('\n'+'DONOR NAME -'+listn[x]+'\n')
            z1.write('\nDONOR PHONE NUMBER -'+listp[x]+'\n')
            x=x+1
            if(x2=='no'):
                webbrowser.open('A+.txt')
                break
    elif(c2=='a-'):
        while(1):
            listn.append(input('enter the name of donor :'))
            p=input('enter the phone number of donor :')
            while(1):
                if(len(p)==10):
                    break
                else:
                    p=input('enter a valid  phone number :')
            listp.append(p)
            lists.append(c2.upper())
            x2=(input('do you want to add another a- blood group details if yes enter yes else no :'))
            z2.write('                  DONOR DETAILS                   \n')
            z2.write('\n'+'DONOR NAME -'+listn[x]+'\n')
            z2.write('\nDONOR PHONE NUMBER -'+listp[x]+'\n')
            x=x+1
            if(x2=='no'):
                webbrowser.open('A-.txt')
                break
    elif(c2=='b+'):
        while(1):
            listn.append(input('enter the name of donor :'))
            p=input('enter the phone number of donor :')
            while(1):
                if(len(p)==10):
                    break
                else:
                    p=input('enter a valid phone number of donor :')
            listp.append(p)
            listc.append(c2.upper())
            x2=(input('do you want to add another b+ blood group details if yes enter yes else no :'))
            z3.write('                  DONOR DETAILS                   \n')
            z3.write('\n'+'DONOR NAME -'+listn[x]+'\n')
            z3.write('\nDONOR PHONE NUMBER -'+listp[x]+'\n')
            x=x+1
            if(x2=='no'):
                webbrowser.open('B+.txt')
                break
    elif(c2=='b-'):
        while(1):
            listn.append(input('enter the name of donor :'))
            p=input('enter the phone number of donor :')
            while(1):
                if(len(p)==10):
                    break
                else:
                    p=input('enter a valid phone number of donor :')
            listp.append(p)
            lists.append(c2.upper())
            x2=(input('do you want to add another b- blood group details if yes enter yes else no :'))
            z4.write('                  DONOR DETAILS                   \n')
            z4.write('\n'+'DONOR NAME -'+listn[x]+'\n')
            z4.write('\nDONOR PHONE NUMBER -'+listp[x]+'\n')
            x=x+1
            if(x2=='no'):
                webbrowser.open('B-.txt')
                break
    elif(c2=='ab+'):
        while(1):
            listn.append(input('enter the name of donor :'))
            p=input('enter the phone number of donor :')
            while(1):
                if(len(p)==10):
                    break
                else:
                    p=input('enter a valid phone number of donor :')
            listp.append(p)
            listc.append(c2.upper())
            x2=(input('do you want to add another ab+ blood group details if yes enter yes else no :'))
            z5.write('                  DONOR DETAILS                   \n')
            z5.write('\n'+'DONOR NAME -'+listn[x]+'\n')
            z5.write('\nDONOR PHONE NUMBER -'+listp[x]+'\n')
            x=x+1
            if(x2=='no'):
                webbrowser.open('AB+.txt')
                break
    elif(c2=='ab-'):
        while(1):
            listn.append(input('enter the name of donor :'))
            p=input('enter the phone number of donor :')
            while(1):
                if(len(p)==10):
                    break
                else:
                    p=input('enter a valid phone number of donor :')
            listp.append(p)
            lists.append(c2.upper())
            x2=(input('do you want to add another ab- blood group details if yes enter yes else no :'))
            z6.write('                  DONOR DETAILS                   \n')
            z6.write('\n'+'DONOR NAME -'+listn[x]+'\n')
            z6.write('\nDONOR PHONE NUMBER -'+listp[x]+'\n')
            x=x+1
            if(x2=='no'):
                webbrowser.open('AB-.txt')
                break
    elif(c2=='o+'):
        while(1):
            listn.append(input('enter the name of donor :'))
            p=input('enter the phone number of donor :')
            while(1):
                if(len(p)==10):
                    break
                else:
                    p=input('enter a valid phone number of donor :')
            listp.append(p)
            lists.append(c2.upper())
            x2=(input('do you want to add another o+ blood group details if yes enter yes else no :'))
            z7.write('                  DONOR DETAILS                   \n')
            z7.write('\n'+'DONOR NAME -'+listn[x]+'\n')
            z7.write('\nDONOR PHONE NUMBER -'+listp[x]+'\n')
            x=x+1
            if(x2=='no'):
                webbrowser.open('O+.txt')
                break
    elif(c2=='o-'):
        while(1):
            listn.append(input('enter the name of donor :'))
            p=input('enter the phone number of donor :')
            while(1):
                if(len(p)==10):
                    break
                else:
                    p=input('enter a valid phone number of donor :')
            listp.append(p)
            lists.append(c2.upper())
            x2=(input('do you want to add another o- blood group details if yes enter yes else no :'))
            z8.write('                  DONOR DETAILS                   \n')
            z8.write('\n'+'DONOR NAME -'+listn[x]+'\n')
            z8.write('\nDONOR PHONE NUMBER -'+listp[x]+'\n')
            x=x+1
            if(x2=='no'):
                webbrowser.open('O-.txt')
                break
def User(j0):
    c1=input('enter the type of blood group you want')
    c2=c1.lower()
    print('welcome'+j0)
    p=input('enter the phone number of donor :')
    while(1):
        if(len(p)==10):
            break
        else:
            p=input('enter a valid phone number of donor :')
    if(c2=='a+'):
        a1=open('A+.txt','r')
        a2=a1.read()
        print(a2)
    elif(c2=='a-'):
        a1=open('A-.txt','r')
        a2=a1.read()
        print(a2)
    elif(c2=='b+'):
        a1=open('B+.txt','r')
        a2=a1.read()
        print(a2)
    elif(c2=='b-'):
        a1=open('B-.txt','r')
        a2=a1.read()
        print(a2)
    elif(c2=='ab+'):
        a1=open('AB+.txt','r')
        a2=a1.read()
        print(a2)
    elif(c2=='ab-'):
        a1=open('AB-+.txt','r')
        a2=a1.read()
        print(a2)
    elif(c2=='o+'):
        a1=open('O+.txt','r')
        a2=a1.read()
        print(a2)
    elif(c2=='o-'):
        a1=open('O-.txt','r')
        a2=a1.read()
        print(a2)
a1=open('A+.txt','a+')
a2=open('A-.txt','a+')
b1=open('B+.txt','a+')
b2=open('B-.txt','a+')
ab1=open('AB+.txt','a+')
ab2=open('AB-.txt','a+')
o1=open('O+.txt','a+')
o2=open('O-,txt','a+')
print('Welcome are you User or Admin')
x=int(input('If admin enter 1 if user enter 2'))
if(x==1):
    pd='enter'
    Admin(pd,a1,a2,b1,b2,ab1,ab2,o1,o2)
else:
    n1=input('enter yout name')
    User(n1)
