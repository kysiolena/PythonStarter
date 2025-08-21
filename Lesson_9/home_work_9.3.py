def get_count_of_ways_to_climb_the_step(step: int) -> int:
    if step < 1:
        return 0
    elif step == 1 or step == 2 or step == 3:
        return step
    else:
        return get_count_of_ways_to_climb_the_step(step - 1) + get_count_of_ways_to_climb_the_step(step - 2)


# result
print(get_count_of_ways_to_climb_the_step(5))
