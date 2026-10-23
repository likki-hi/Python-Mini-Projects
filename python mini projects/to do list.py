
tasks = []
completed = []

while True:
    print("\n--- TO-DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Remove Task")
    print("5. Show Progress")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        completed.append(False)
        print("Task added!")

    elif choice == "2":
        for i, task in enumerate(tasks):
            status = "Done" if completed[i] else "Pending"
            print(i + 1, task, "-", status)

    elif choice == "3":
        n = int(input("Enter task number: ")) - 1
        if 0 <= n < len(tasks):
            completed[n] = True
            print("Task completed!")

    elif choice == "4":
        n = int(input("Enter task number: ")) - 1
        if 0 <= n < len(tasks):
            tasks.pop(n)
            completed.pop(n)
            print("Task removed!")

    elif choice == "5":
        total = len(tasks)
        done = sum(completed)
        percent = int(done / total * 100) if total else 0
        bar = "#" * (percent // 10) + "-" * (10 - percent // 10)
        print(f"Progress: {percent}% [{bar}]")

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
