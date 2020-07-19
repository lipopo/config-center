import sys

from model import database, Config


class Task:
    __doc__ = "Please Enter Task"

    @classmethod
    def run(cls, arg_list):
        tasks = Task.__subclasses__()
        for task in tasks:
            if len(arg_list) > 0 and \
               task.name == arg_list[0]:
                task.run(arg_list[1:])
                break
        else:
            for task in tasks:
                print(f"{task.name} - {task.__doc__}")


class ModelTask(Task):
    name = "db"
    __doc__ = "You Can Handler Database"

    def task_create(self, *args, **kwargs):
        """Create a table in database"""
        database.connect()
        database.create_tables([Config])

    @classmethod
    def help(cls):
        tasks = filter(
            lambda item: item[0].startswith("task_"),
            cls.__dict__.items())
        for name, func in tasks:
            print(f"{name} - {func.__doc__}")
        print("help - Print help data")

    @classmethod
    def run(cls, arg_list):
        instance = cls()
        if not arg_list:
            instance.help()
        else:
            func = cls.__dict__.get(arg_list[0])
            if func is None:
                return
            func(instance, arg_list[1:])


if __name__ == "__main__":
    Task().run(sys.argv[1:])
