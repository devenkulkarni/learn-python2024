if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split() ##name: Assigns the first word of the input to this variable *line: Assigns the remaining words (if any) to this list. The * symbol here is used for extended unpacking, which allows the variable to capture multiple values into a list..split(): Splits the input line into separate words, using spaces as the delimiter.
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print(student_marks)
    for i,j in student_marks.items():
        if i == query_name:
            total_sum = sum(j)
            average = total_sum / len(scores)
            print(average)
            average_rounded = format(average, ".2f")  #We use the format() function with the format specifier ".2f" to format the average to display exactly two decimal places.
            print(average_rounded)   
