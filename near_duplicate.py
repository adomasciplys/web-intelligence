def Jaccard(A,B):
    A = set(A)
    B = set(B)
    overlap = len(A.intersection(B))
    union = len(A.union(B))
    return overlap / union

A = {"do not worry", "not worry about", "worry about your", "about your difficulties", "your difficulties in", "difficulties in mathematics"}
B = {"i would not", "would not worry", "not worry about", "worry about your", "about your difficulties", "your difficulties you", "difficulties you can", "you can easily", "can easily learn", "easily learn what", "learn what is", "what is needed"}

print(Jaccard(A,B))