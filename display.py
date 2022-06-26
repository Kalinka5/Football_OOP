# create class AttrDisplay
class AttrDisplay:
    # function to print favourite player
    def print_idol(self):
        print(f'My favourite footballer is {getattr(self, "idol_name")}.')

    # function where print class of footballer and his name
    def __repr__(self):
        return f'[{self.__class__.__name__}: {getattr(self, "name")}]'
