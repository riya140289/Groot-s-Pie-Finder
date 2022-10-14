import collections
def findPies1(list_val, n):
    list1=list_val
    res_lis=[]
    if n in list1:
        res1=list1.index(n)
        res_lis.append(res1)
    return res_lis

def findPies2(list_val, n):
    list1=list_val
    res_list=[]
    res_list1=[]
    for i in list1:
        for j in list1:
            index_i= list1.index(i)
            index_j=list1.index(j)
            res1=sum(i,j)
            if(res1==n):
                if(index_i!=index_j):
                    res_list.append(index_i)
                    res_list.append(index_j)
                    return res_list
                elif(index_i==index_j):
                    python_indices=duplicateindex(list_val,i)
                    for i in python_indices:
                        thiselem=python_indices[i]
                        nextelem=python_indices[i+1]
                        res_list.append(index_i)
                        res_list.append(thiselem)
                        res_list1.append(index_i)
                        res_list1.append(nextelem)
                        return res_list, res_list1
                    
def findPies3(list_val, n):
    list1=list_val
    res_list=[]
    res_list1=[]
    for i in list1:
        for j in list1:
            for k in list1:
                index_i= list1.index(i)
                index_j=list1.index(j)
                index_k=list1.index(k)
                res1=sum1(i,j,k)
                if(res1==n):
                    if(index_i!=index_j!=index_k):
                        res_list.append(index_i)
                        res_list.append(index_j)
                        res_list.append(index_k)
                        return res_list, res_list[::-1]
                        
                    
def sum(a,b):
    return a+b
def sum1(a,b,c):
    return a+b+c
def duplicateindex(list_val,i):
    python_indices  = [index for (index, item) in enumerate(list_val) if item == i]
    return python_indices
def findPies(list_val, n):
    size=len(list_val)
    if size%2!=0:
        res1=findPies1(list_val,n)
        res2=findPies3(list_val,n)
        if(res1==[]):
            return res2
        else:
            return res1, res2
    if size%2==0:
        res3 = findPies1(list_val2,n)
        res4 = findPies2(list_val2,n)
        if(res3==[]):
            return res4
        else:
            return res3, res4
list_val=[1, 2, 3, 2, 1]
n=6
list_val2=[8, 4, 3, 2, 6, 5]
print(findPies(list_val,n))
print(findPies(list_val2,n))


