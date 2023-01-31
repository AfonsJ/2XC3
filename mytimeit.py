import timeit


def f1(arg1, arg2):
    for i in range(0,1000000):
        sum = arg1 + arg2



start =  timeit.default_timer()
f1(2,2)
stop = timeit.default_timer()

print(start)
print(stop)
print(stop-start)

print("TOTOAL")
total = 0
start_total =  timeit.default_timer()
f1(2,2)
total += timeit.default_timer() - start_total 
print(total)