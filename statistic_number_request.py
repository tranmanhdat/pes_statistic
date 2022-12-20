import json
import datetime
import matplotlib.pyplot as plt
with open("tasks.json", "r") as f:
    tasks = json.load(f)
    list_time = []
    for task in tasks:
        try:
            time = datetime.datetime.strptime(task["last_update"]["$date"], "%Y-%m-%dT%H:%M:%S.%fZ")
        except:
            time = datetime.datetime.strptime(task["last_update"]["$date"], "%Y-%m-%dT%H:%M:%SZ")
        list_time.append(time)
    alpha_time = (list_time[-1] - list_time[0])// datetime.timedelta(minutes=1)
    # print(alpha_time)
    # x_axis = [i for i in range(alpha_time+1)]
    x_axis = [list_time[0] + datetime.timedelta(hours=8) + datetime.timedelta(minutes=i) for i in range(alpha_time+1)]
    # print(x_axis)
    y_axis = []
    j = 0
    for i in range(alpha_time+1):
        count = 0
        if j < len(list_time):
            while list_time[j] <= list_time[0] + datetime.timedelta(minutes=i):
                count += 1
                j += 1
                if j >= len(list_time):
                    break
        y_axis.append(count)
    # print(y_axis)
    # print(len(x_axis), len(y_axis))
    plt.plot(x_axis, y_axis)
    plt.xticks(rotation=45, ha='right')
    plt.title("Resquest per minute")
    plt.xlabel("Time")
    plt.ylabel("Number of request")
    plt.savefig("statistic.png")
    plt.show()