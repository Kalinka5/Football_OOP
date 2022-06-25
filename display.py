# create class AttrDisplay
class AttrDisplay:
    # function where print class of footballer and his name
    def __repr__(self):
        return f'[{self.__class__.__name__}: {getattr(self, "name")}]'
