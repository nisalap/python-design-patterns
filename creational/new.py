class New:
    a = None

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, *args, **kwargs):
        pass

    # def a(self):

n = New(a=1)
print(n.a)

nn = New(a=2)
print(nn.a)
print(n.a)
