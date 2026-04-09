def sum_even_n_nums(n,sum):
    if n<=0:
        print("sum is ",sum)
        return
    sum = sum+n
    n-=1
    sum_even_n_nums(n,sum)
num = int(input("please enter a number "))
sum_even_n_nums(num,0)
