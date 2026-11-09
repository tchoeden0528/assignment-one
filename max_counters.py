# N counters start at 0
# if X is between 1 and N, add 1 to counter X
# if X is N + 1, set all counters to the biggest counter

def solution(N, A):
    # make a list of N zeros
    counters = []
    for i in range(N):
        counters.append(0)

    # go through each operation
    for X in A:
        if X >= 1 and X <= N:
            # increase counter X (lists start at 0, so use X - 1)
            counters[X - 1] = counters[X - 1] + 1
        else:
            # find the biggest counter
            biggest = 0
            for value in counters:
                if value > biggest:
                    biggest = value

            # set every counter to the biggest
            for i in range(N):
                counters[i] = biggest

    return counters

print(solution(5, [3, 4, 4, 6, 1, 4, 4]))  # should be [3, 2, 2, 4, 2]
