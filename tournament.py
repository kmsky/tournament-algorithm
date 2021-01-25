# tournament algorithm to find max and second max value

# this source was used to create the code:
# http://users.csc.calpoly.edu/~dekhtyar/349-Fall2017/lectures/lec03.349.pdf

def tournament(i, j, array):
    if i == j:
        return array[i], []

    max1, compared1 = tournament(i, i + (j - i) // 2, array)
    max2, compared2 = tournament(1 + i + (j - i) // 2, j, array)

    if max1 > max2:
        compared1.append(max2)
        return max1, compared1
    else:
        if max1 != max2:
            compared2.append(max1)
        return max2, compared2


def find_second_max(array):
    final_max, compared = tournament(0, len(array) - 1, array)
    second_max, second_compared = tournament(0, len(compared) - 1, compared)

    return final_max, second_max


if __name__ == "__main__":
    array = [10, 2, 3, 4, 5, 6, 7, 8, 2, 4]
    print(find_second_max(array))
