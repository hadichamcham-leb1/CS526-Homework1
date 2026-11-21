import sys


def longest_sequence(A, B):
    # "Notebooks": each answer is computed once, then looked up
    memo_A = {}     # position p -> longest valid sequence ending exactly at A[p]
    memo_B = {}     # position p -> longest valid sequence ending exactly at B[p]

    def end_A(p):
        if p in memo_A:                   # already computed: just look it up
            return memo_A[p]
        best = 1                          # A[p] by itself is a valid sequence
        for q in range(p):                # every EARLIER position
            # the previous element is B[q]: earlier position, smaller value
            if q < len(B) and B[q] < A[p]:
                best = max(best, 1 + end_B(q))
        memo_A[p] = best                  # write the answer in the notebook
        return best

    def end_B(p):
        if p in memo_B:
            return memo_B[p]
        best = 1
        for q in range(p):
            # the previous element is A[q]: earlier position, smaller value
            if q < len(A) and A[q] < B[p]:
                best = max(best, 1 + end_A(q))
        memo_B[p] = best
        return best

    # the answer is the best result over every position of both sequences
    best = 0
    for p in range(len(A)):
        best = max(best, end_A(p))
    for p in range(len(B)):
        best = max(best, end_B(p))
    return best


def main():
    filename = input("File name: ")
    with open(filename) as f:
        lines = f.read().splitlines()
    # lines[0] and lines[1] are the sizes; lines[2] and lines[3] are the values
    A = [int(x) for x in lines[2].split()]
    B = [int(x) for x in lines[3].split()]
    print("File Input:", filename)
    print("Longest Sequence:", longest_sequence(A, B))


if __name__ == "__main__":
    main()