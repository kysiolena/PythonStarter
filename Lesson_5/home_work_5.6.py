from collections import namedtuple

Feedback = namedtuple('Feedback', 'menu gym service')

print('Програма для аналізу фідбеку від відвідувачів курорту «Морська зірка»')

discount = 0
feedback_temp = tuple()
for realm in Feedback._fields:
    feedback_realm = input(f'Please describe your impressions of the {realm}. Or press ENTER to skip this question: ')

    if feedback_realm:
        feedback_temp += (feedback_realm,)

        discount += 5
    else:
        feedback_temp += ('',)

feedback = Feedback(feedback_temp[0], feedback_temp[1], feedback_temp[2])

discount += 15 if len((feedback.menu + feedback.gym + feedback.service)) >= 60 else 0

print(f'Your {discount=}')
