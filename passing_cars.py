# PassingCars
# 0 = car going east, 1 = car going west
# count how many pairs of cars pass each other

def solution(A):
    # first loop: count all the west cars
    west = 0
    for car in A:
        if car == 1:
            west = west + 1

    # second loop: each east car passes every west car still ahead of it
    passing = 0
    for car in A:
        if car == 0:
            passing = passing + west
        else:
            # this west car is behind us now
            west = west - 1

    # the problem says to return -1 if the number is too big
    if passing > 1000000000:
        return -1

    return passing

print(solution([0, 1, 0, 1, 1]))  # should be 5
