task_list = ['awds', 'asdwa', 1, 12,3123, 123,123, 'awd', 'awdas']

class ToDoList():
    def __init__(self, todo_list):
        # self.name = name
        self.todo_list = todo_list
    def add_task(self):
        self.todo_list.append(input("New Task"))
    def view_task(self):
        for i in range(len(self.todo_list)):
            print(f'{i+1}: {self.todo_list[i]}')
    def strike(self, number):
        text = str(self.todo_list[number])
        return ''.join([u'\u0336{}'.format(c) for c in text])

test = ToDoList(task_list)

test.view_task()
print(test.strike(3))



