def study_schedule(permanence_period, target_time):
    count = 0
    n = len(permanence_period)
    if target_time is None:
        return None
    for index in range(n):
        start_time = permanence_period[index][0]
        end_time = permanence_period[index][1]
        if (
            start_time is None
            or end_time is None
            or not isinstance(start_time, int)
            or not isinstance(end_time, int)
        ):
            return None
        if start_time <= target_time <= end_time:
            count += 1
    return count


# permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
# print(study_schedule(permanence_period, None))
