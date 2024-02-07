# create class AttrDisplay
class AttrDisplay:
    # function footballer speaking about him
    def speak(self):
        print(f'I`m {getattr(self, "name")} and I`m the best {getattr(self, "position")} in the world!')

    # function to print favourite player
    def print_idol(self):
        print(f'My favourite footballer is {getattr(self, "idol")}.')

    # function where print class of footballer and his name
    def __repr__(self):
        return f'[{self.__class__.__name__}: {getattr(self, "name")}]'
