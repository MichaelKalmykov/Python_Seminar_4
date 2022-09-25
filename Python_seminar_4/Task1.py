# Вычислить число c заданной точностью d Пример: d = 0.001, π = 3.141.
import math
from math import pi
d = str(input('Введите точность для числа π \n'))
if len(d) == 1 or len(d) == 2:
    print(f'π с заданой точностью {d} ровно: ',3)
else:
    print(f'π с заданой точностью {d} ровно: ',{round(pi, len(d)-2)})