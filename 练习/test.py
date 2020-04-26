# t = "18:00:00"
t = list("18:00:00")
t[4] = 1
print(t[4])
print(t)
print(''.join([str(i) for i in t]))