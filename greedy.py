# Function to perform activity selection using a greedy approach
def activity_selection(activities):
    # Sort activities by their end time
    activities.sort(key=lambda x: x[1])

    print("Selected activities:")

    # The first activity is always selected
    last_selected = activities[0]
    print(last_selected)

    # Consider remaining activities
    for i in range(1, len(activities)):
        # If the start time of the current activity is greater or equal
        # to the end time of the last selected activity, select it
        if activities[i][0] >= last_selected[1]:
            print(activities[i])
            last_selected = activities[i]

# Driver code to test the function
if __name__ == "__main__":
    # List of activities with (start time, end time)
    activities = [(5, 9), (1, 2), (3, 4), (0, 6), (5, 7), (8, 9)]

    activity_selection(activities)
