def print_natural_nums(n,count):
    if count>n:
        return
    print(" ",count)
    count+=1
    print_natural_nums(n,count)
n = int(input("please enter number"))    
print_natural_nums(n,1)    

