from annoy import AnnoyIndex
import pickle

vectors = pickle.load(open('./model/data/vectors.pkl', 'rb'))

f = 5000  # Length of item vector that will be indexed

t = AnnoyIndex(f, 'angular')
for i in range(4808):
    v = vectors[i]
    t.add_item(i, v)

t.build(10) # 10 trees
t.save('vectors.ann')

# ...

u = AnnoyIndex(f, 'angular')
u.load('vectors.ann') # super fast, will just mmap the file
print(u.get_nns_by_item(0, 7)) # will find the 1000 nearest neighbors
