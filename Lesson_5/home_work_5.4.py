from collections import deque, namedtuple

Score = namedtuple('Score', 'algebra geometry history computer_science geography')

students_scores = deque([])

students_scores.append(Score(5, 5, 5, 5, 4))
students_scores.append(Score(5, 3, 3, 5, 4))
students_scores.append(Score(5, 4, 5, 3, 4))
students_scores.append(Score(5, 5, 5, 5, 4))
students_scores.append(Score(5, 5, 3, 5, 4))
students_scores.append(Score(4, 5, 5, 4, 4))
students_scores.append(Score(5, 3, 5, 5, 4))
students_scores.append(Score(4, 5, 4, 5, 4))
students_scores.append(Score(5, 5, 3, 5, 4))

for index, student in enumerate(students_scores):
    print(f'Student #{index}: {student}')
