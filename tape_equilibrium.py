# TapeEquilibrium
# split the tape at every possible spot P (from 1 to N - 1)
# work out |left sum - right sum| and keep the smallest one

def solution(A):
    N = len(A)
    smallest = -1   # -1 means we haven't found a difference yet

    for P in range(1, N):
        # add up the left part: A[0] to A[P - 1]
        left = 0
        for i in range(0, P):
            left = left + A[i]

        # add up the right part: A[P] to A[N - 1]
        right = 0
        for i in range(P, N):
            right = right + A[i]

        # difference between the two parts (always positive)
        difference = left - right
        if difference < 0:
            difference = -difference

        # keep the smallest difference
        if smallest == -1 or difference < smallest:
            smallest = difference

    return smallest

print(solution([3, 1, 2, 4, 3]))   # should be 1
print(solution([-1000, 1000]))     # should be 2000
print(solution([1, -1, 1, -1]))    # should be 0
