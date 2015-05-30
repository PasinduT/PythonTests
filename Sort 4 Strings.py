#This program was made on 5/30/2015
#By Pasindu Tennakoon

#-------Warning!------------------#
#-This program has undergone only-#
#-Alpha testing-------------------#



#This functions compares two strings (name1 , name2)
#Returns 'True' is name1 is alphabetically greater than name2
#Or in the case when name1 starts with name2 and is greater in length
#Otherwise the function returns 'False'

def biggerthan(name1,name2):
    lenA = len(name1)
    lenB = len(name2)
    if(lenA>=lenB):
        lenT = lenB
    else:
        lenT = lenA

    for i in range(lenT):
        if(ord(name1[i])>ord(name2[i])):
            return True
        elif (ord(name1[i])<ord(name2[i])):
            return False
        else:
            pass

    if(lenA>=lenB):
        return True
    else:
        return False



#The main program

a=[]

for i in range(4):
    c = raw_input("Enter a name: ")
    a.append(c)

for i in range(4):
    for j in range(i+1,4,1):
        if(biggerthan(a[i],a[j])):
            t= a[i]
            a[i]=a[j]
            a[j]=t

for j in range(4):
    print(a[j])
