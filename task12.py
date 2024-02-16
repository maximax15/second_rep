class Todo:
    def __init__(self) -> None:
        self.things = []
        self.by_priority = []
        self.low_priority = []
        self.high_priority = []

    def add(self, thing, num):
        tpl = (thing, num)
        self.things.append(tuple(tpl))

    def get_by_priority(self, n):
        for el in self.things:
            if el[1] == n:
                self.by_priority.append(el[0])

        return self.by_priority

    def get_low_priority(self):
        low_priority = min([el[1] for el in self.things])
        for el in self.things:
            if el[1] == low_priority:
                self.low_priority.append(el[0])
        return self.low_priority

    def get_high_priority(self):
        high_priority = max([el[1] for el in self.things])
        for el in self.things:
            if el[1] == high_priority:
                self.high_priority.append(el[0])
        return self.high_priority


todo = Todo()
todo.add("Ответить на вопросы", 5)
todo.add("Сделать картинки", 1)
todo.add("Доделать задачи", 4)
todo.add("Дописать конспект", 5)
print(todo.get_low_priority())
print(todo.get_high_priority())
print(todo.get_by_priority(3))
