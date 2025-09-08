def Jaccard(A,B):
    A = set(A)
    B = set(B)
    overlap = len(A.intersection(B))
    union = len(A.union(B))
    return overlap / union

def kShingles(k, string):
    cleaned_string = str(string.replace(',', ''))
    shingles = set()
    words = cleaned_string.split()
    n = len(words)

    for i in range(n - k + 1):
        shingle = " ".join(words[i:i+k])
        shingles.add(shingle)

    return shingles

A = "Do not worry about your difficulties in Mathematics"
B = "i would not worry about your difficulties, you can easily learn what is needed"
k = 3
A_shingle = kShingles(3, A)
B_shingle = kShingles(3, B)
result = Jaccard(A_shingle, B_shingle)
print(result)




