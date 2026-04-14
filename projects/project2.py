import json
 

task = []

#load task
def load_task():
    global task
    try:
        with open("task.json","r") as f:
            task = json.load(f)
    except:
        task=[]

#save task
def save_task():
    with open("task.json","w") as f:
        json.dump(task,f)


def add_task():
    tasks = input("enter u r task : ")
    task.append(tasks)
    save_task()
    print("task added ")

def view_task():
    if not task:
        print("not available...")
    else:
        with open("task.json","r") as f:
            print(f.read())
        #  for i, t in enumerate(task, 1):
        #     print(i, ".", t)



while True:
    print("1 for add task : ")
    print("2 for view task : ")
    print("3 for exit : \n")

    ch = input("\nenter u r chaice : ")

    if ch == '1':
        add_task()
    elif ch == '2':
        view_task()
    elif ch == '3':
        break
    else:
        print("\ninvalid shit bitch......\n")
