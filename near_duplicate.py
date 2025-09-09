def Jaccard(A,B):
    A = set(A)
    B = set(B)
    overlap = len(A.intersection(B))
    union = len(A.union(B))
    return overlap / union

def clean_string(string):
    return string.translate(str.maketrans('', '', ',.!?;:-'))

def kShingles(k, string):
    cleaned_string = clean_string(string)
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
    result = ""
    k = 3
    A_shingle = kShingles(k, fileA)
    B_shingle = kShingles(k, fileB)
    similarity = Jaccard(A_shingle, B_shingle)
    if(similarity > 0.9):
        result = "Near Duplicate: "
    else:
        result = "Not a duplicate: "
    return result + str(similarity)

result = nearDuplicate(readFile("File_A.txt"), readFile("File_B.txt"))
print(result)


