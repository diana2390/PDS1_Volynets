class MyCustomError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        print('calling str')
        if self.message:
            return f'MyCustomError, {self.message} '
        else:
            return 'MyCustomError has been raised'


# raise MyCustomError("Something goes wrong:(")
