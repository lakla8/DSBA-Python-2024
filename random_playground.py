import random
import string
import pickle
random.seed(0)
x = [random.gauss() for _ in range(10_000)]
z = ''.join(random.choices(string.ascii_letters, k=10))

# g = {''.join(random.choices(string.ascii_letters, k=10)): random.gauss() for _ in range(100)}
# with open("data_gauss.pickle", 'wb') as file:
#     pickle.dump(g, file)

with open('data_gauss.pickle', 'rb') as f:
    g = pickle.load(f)
print(g)
