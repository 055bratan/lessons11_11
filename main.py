# def main(**kwargs):

#     print(kwargs)
#     for k,v in kwargs.items():
#         print(k,v)
#         return kwargs
# print(main(name='zhako',age='20',i=123,a=123.123))


# a=10
# for i in a:
#     print(i)

# def rec(number:int):
#     if number==0:
#         return 0
#     return number*rec(number-1)
# # print(rec(5))
# num=int(input("Введите число"))
# factorial=rec(num)
# print("Факториал числа ",num,'равен',factorial )


def max_find_num(lists:list,n):
    
    if n==0:
        return "Куасынба"
    if n==1:
        return lists[0]
    return max(lists[n-1],max_find_num(lists,n-1))
arr=[1,2,3]
n=len(arr)
print(max_find_num(arr,n))
    

