n = 72
f = 4.03
s = 'string cheese'

print('%d %f %s' % (n, f, s))
print('%10d %10f %10s' % (n, f, s))
print('%10.4d %10.4f %10.4s' % (n, f, s))
print('%-10.4d %-10.4f %-10.4s' % (n, f, s))
print('%*.*d %*.*f %*.*s' % (10, 4, n, 10, 2, f, 10, 6, s))

print('{0:<10d} {1:>10.2f} {2:!^10}'.format(n, f, 'SALE'))
