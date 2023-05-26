# Teacher's Version


class Item():
    def __init__(self, name, id):
        self.name = name
        self.completed = False
        self.id = id
    
    def print(self):
        print(f'{self.id}: {self.name}: ')
        if self.completed is True:
            print('Completed')
        else:
            print('not completed')


class ToDoListFunctions():
    def __init__(self, name):
       self.name = name
       self.items = []
       self.completed = []

    def add_task(self, task):
        item = Item(task, len(self.items) + 1)
        self.items.append(item)
        print(self.items)

    def view_tasks(self):
        print('=' * 15)
        print(f'{self.name} List')
        print('-' * 15)
        for i, item in enumerate(self.items):
            # print(f'{i+1}: {item.name}, {item.completed}')
            item.print()
        print('=' * 15)

    def mark_completed(self, task_id):
        try: 
            task_id < len(self.items)
        except IndexError:
            print('this is invalid') 
        self.items[task_id-1].completed = True

    def remove_task(self, task_id):
        self.items.pop(task_id-1)



class ToDoApp():
    def __init__(self):
        self.todolists = ToDoListFunctions('test')

    def run(self):
        cmd = input('enter your command (add, view, completed, remove)')
        if cmd == 'add':
            self.todolists.add_task(input('New task:'))
        if cmd == 'view':
            self.todolists.view_tasks()
        if cmd == 'completed':
            self.todolists.mark_completed(int(input('task number:')))
        if cmd == 'remove':
            self.todolists.remove_task(int(input('task number:')))

test = ToDoApp()

test.run()
test.run()
test.run()
test.run()
test.run()
test.run()
test.run()
test.run()




'''
while True: 
    print_commands()
    command = int(input('give your command'))
    if command == 1:
        task = input('what is your task to add?')
        pass

work_todo_list = ToDoListFunctions('My Work')
work_todo_list.add_task('awdoijawd')
work_todo_list.view_tasks()
work_todo_list.mark_completed(1)
work_todo_list.view_tasks()
work_todo_list.remove_task(1)
work_todo_list.view_tasks()
'''


