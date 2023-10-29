def study_schedule(permanence_period, target_time):
    count = 0
    n = len(permanence_period)
    for index in range(n):
        if (
            permanence_period[index][0] == target_time
            or permanence_period[index][1] == target_time
        ):
            count += 1
        if permanence_period[index][0] < target_time < permanence_period[index][1]:
            count += 1
    return count


permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
print(study_schedule(permanence_period, 2))
