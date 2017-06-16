class CoolT(str):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def __format__(self, format_spec):
        print ('formatting')

s = CoolT("abcd")
s.format(**{})