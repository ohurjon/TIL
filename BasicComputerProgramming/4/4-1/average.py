a= [3,2,2]
b= [4.5,3.5,4.0]

sa= 0
sab =0

for i in range(len(a)):
    sab += a[i]*b[i]
    sa += a[i]

print(f'{sab/sa:.2f}')

