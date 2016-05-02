import json
import csv
import sys

columns = ["TASK","FOLDER","CONTEXT","GOAL","LOCATION","STARTDATE","STARTTIME","DUEDATE","DUETIME","REPEAT","LENGTH","TIMER","PRIORITY","TAG","STATUS","STAR","NOTE"]

recurrence_map = {"day" : "Daily", "week" : "Weekly", "month" : "Monthly", "year" : "Yearly"} 

def convert_wunderlist_csv(filename):
    js = json.load(open(filename))
    data = js["data"]
    lists = data["lists"]
    tasks = data["tasks"]
    notes = data["notes"]
    not_completed = [x for x in tasks if not x["completed"] ]

    lists_map = {}
    for x in lists:
        lists_map[x["id"]] = x["title"].encode("utf-8").strip()

    task_map = {}
    out_tasks = []
    for i in not_completed:
        a = { "TASK" : i["title"].encode("utf-8").strip(),
              "FOLDER" : lists_map[i["list_id"]] }

        if "due_date" in i:
            a["DUEDATE"] = i["due_date"].encode("utf-8")
        if i["starred"]:
            a["STAR"] = "Yes"

        if "recurrence_type" in i:
            a["REPEAT"] = recurrence_map[i["recurrence_type"]].encode("utf-8")

        out_tasks.append(a)
        task_map[i["id"]] = a

    for i in notes:
        t_id = i["task_id"]
        if t_id in task_map:
            t = task_map[t_id]
            t["NOTE"] = i["content"].encode("utf-8")

    with open("toodledo.csv", "wb") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columns)
        writer.writeheader()
        for i in out_tasks:
            writer.writerow(i)


    # print lists_map

    # print data.keys
    # print len(tasks)
    # print len(not_completed)
    # print not_completed[0]

if len(sys.argv) != 2:
    print("ERROR: no filename given")
    exit()

convert_wunderlist_csv(sys.argv[1])


