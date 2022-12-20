import json
import datetime
import matplotlib.pyplot as plt
import sys
log_file = sys.argv[1]
with open(log_file, "r") as f:
    tasks = json.load(f)
    
    data = {}
    for task in tasks:
        if "status_convert" not in task:
            continue
        if task["status_convert"] not in data:
            data[task["status_convert"]] = [ float(task["time_process"]) ]
        else:
            data[task["status_convert"]].append(float(task["time_process"]))
    x_axis, y_axis = [], []
    number_request = []
    for key in data:
        x_axis.append(key)
        y_axis.append(sum(data[key])/len(data[key]))
        number_request.append(len(data[key]))
    # plt.bar(x_axis, y_axis)
    # plt.title("Average time process")
    # plt.xlabel("Status")
    # plt.ylabel("Time (s)")
    # plt.show()
    
    figure, axis = plt.subplots(1, 2)
    axis[0].bar(x_axis, y_axis)
    axis[0].set_title("Average time process")
    axis[0].set_xlabel("Status")
    axis[0].set_ylabel("Time (s)")
    
    def my_fmt(x):
        print(x)
        return '{:.4f}%\n({:.0f})'.format(x, total*x/100)
    total = sum(number_request)
    explode = [0, 0 ,0 , 0.3]
    axis[1].pie(number_request, labels=x_axis, autopct=my_fmt,explode=explode)
    
    plt.show()
    
    # print(y_axis)
    # print(len(x_axis), len(y_axis))
    # plt.plot(x_axis, y_axis)
    # plt.xticks(rotation=45, ha='right')
    # plt.title("Resquest per minute")
    # plt.xlabel("Time")
    # plt.ylabel("Number of request")
    # plt.savefig("statistic.png")
    # plt.show()