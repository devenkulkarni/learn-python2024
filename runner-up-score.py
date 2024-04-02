n = int(input("Enter number of participants to find the runner up scorer:"))
arr = map(int, input("Enter scores for above participants").split())
numbers = list(arr)
numbers = list(set(numbers))
numbers.sort(reverse=True)
#print(numbers)
#print(len(numbers))
runner_up = numbers[1]
print(runner_up)
