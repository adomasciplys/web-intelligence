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

def readFile(filePath):
    f = open(filePath)
    text = f.read()
    f.close()
    return text

def nearDuplicate(fileA, fileB):
    k = 3
    A_shingle = kShingles(k, fileA)
    B_shingle = kShingles(k, fileB)
    result = Jaccard(A_shingle, B_shingle)
    print(result)

nearDuplicate(readFile("File_A.txt"), readFile("File_B.txt"))


