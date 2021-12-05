import numpy as np

np.random.seed(2021)
with open('./fake_data.txt', 'w') as f:
    for i in range(int(1e6)):
        n1 = np.random.randint(1000)
        n2 = np.random.randint(1000)
        v = np.random.rand() * 5
        f.write('%d\t%d\t%.1f\n' % (n1, n2, v))
print('done')