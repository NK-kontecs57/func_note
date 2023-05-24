from random import *
cl_1 = [randint(1, 20) for _ in range(30)]
cl_2 = [randint(1, 20) for _ in range(30)]
print(sum(cl_1) / len(cl_1), sum(cl_2) / len(cl_2), max([sum(cl_1) / len(cl_1), sum(cl_2) / len(cl_2)]), sep='\n')