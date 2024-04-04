if __name__ == '__main__':
    arr= []
    score_arr = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr.append([name, score])
        score_arr.append(score)
    min_2 = sorted(set(score_arr))[1]
    result = [x[0] for x in arr if x[1] == min_2]
    print(*sorted(result), sep = "\n")
