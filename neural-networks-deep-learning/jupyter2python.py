import numpy as np

a = np.random.randn(10,5);
b = np.random.rand(10,1);
c = a * b;
print(a);
print('\n')
print(b);
print('\n')
print(c);

d = np.dot(a.T,b);
print(d);

