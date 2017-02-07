#
# # Mutable Function
# # persistent local state
# def make_withdraw(balance):
#
#     def withdraw(amount):
#         nonlocal balance
#         balance-= amount
#         return balance
#     def deposit(amount):
#         nonlocal balance
#         balance+=amount
#         return balance
#
#     return withdraw,deposit
#
# withdraw,deposit = make_withdraw(100)
# print(withdraw(25))
# print(withdraw(30))
#
# print(deposit(25))
# print(deposit(30))
#
# #Mutable data & persistent local state
#
# def make_withdraw_list(balance):
#     list = [balance]
#     def withdraw(amount):
#         balance[0]-= amount
#         return balance[0]
#     def deposit(amount):
#         balance[0]+=amount
#         return balance[0]
#
#     return withdraw,deposit
#
# withdraw,deposit = make_withdraw(100)
# print(withdraw(25))
# print(withdraw(30))
#
# print(deposit(25))
# print(deposit(30))
#
#
# print(type(deposit))
#
# class Link:
#     empty=()
#     def __init__(self,first,rest=empty):
#         self.first = first
#         self.rest = rest
#     def __getitem__(self, item):
#         if item==0:
#             return self.first
#         else:
#             return self.rest[item-1]
#
#     def __len__(self):
#         return 1 + len(self.rest)
#
#     # def __repr__(self):
#     #     if self.rest:
#     #         return self.first

def fib(n):

    if n <=1:
        return n
    else:
        return fib(n-1)+fib(n-2)

def count(f):
    def counted(*args):
        counted.call_counts +=1
        return f(*args)
    counted.call_counts = 0
    return counted

def memo(f):
    cache = {}
    def memoization(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return memoization

counted_fib = count(fib)
print(counted_fib(10))
print(counted_fib.call_counts)
print(counted_fib(20))
print(counted_fib.call_counts)