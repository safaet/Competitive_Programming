def activity_selection(activities):
    
    activities.sort(key=lambda x: x[1])

    selected_activities = []
    last_end_time = 0

    for start, end in activities:
        if start >= last_end_time:
            selected_activities.append((start, end))
            last_end_time = end

    return selected_activities

activities = [(1, 3), (2, 5), (3, 9), (6, 8), (5, 7)]
result = activity_selection(activities)

print("Selected Activities: ",  result)