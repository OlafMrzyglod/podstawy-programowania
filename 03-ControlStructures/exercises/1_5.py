total_tasks = 20
tasks_ok = int(input("How many tasks were correct? "))
if tasks_ok >= total_tasks / 2:
    print("Congratulations! You passed the test.")
else:
    print("Unfortunately, you failed the test.")
