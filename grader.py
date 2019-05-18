def assigngrade(score, grades = ['A', 'B', 'C', 'D', 'F'],
                cutoffs = [90, 80, 70, 65, 0]):
    for item in range(len(cutoffs)):
        if score >= cutoffs[item]:
            print(grades[item])
            break

def droplowest(L):
    smallest = float('inf')
    for item in L:
        if item <= smallest:
            smallest = item
    L.remove(smallest)

def average(L):
    return sum(L)/len(L)

A = [1, 3, 2, 4, 1, 5, 1]
droplowest(A)

assigngrade(69)
