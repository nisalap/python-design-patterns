class Singleton:

    def __new__(cls, *args, **kwargs):
        print('new', cls, args, kwargs)
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, *args, **kwargs):
        print('init', self, args, kwargs)
        self.a = kwargs['a']
        Singleton.a = self.a + 1


n = Singleton(a=1)
print(n.a)

nn = Singleton(a=2)
print(nn.a)
print(n.a)
