import random, string

size = 8

unit = strin.ascii_letters + string.digits + '@#$!%*()-_+=''?/;:.|\|,'

rand = random.SystemRando()

print(''.join(rand.choice(unit)for i in range(size)))