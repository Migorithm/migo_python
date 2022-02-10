#For non-nested hash
class Hooker(object):
    # reading config file
    def __init__(self, **result):
        self.__dict__.update(result)

    def __repr__(self):
        return str(self.__dict__)

    @staticmethod
    def Hook(dict_data):
        return Hooker(**dict_data)

class Struct:
    def __init__(self, **entries):
        self.__dict__.update(entries)

#Struct(**data_data)


#For nested hash (also useful in object_hook when loading json)
class Struct(object):
    def __init__(self, data):
        for name, value in data.items():
            setattr(self, name, self._wrap(value))

    def _wrap(self, value):
        if isinstance(value, (tuple, list, set, frozenset)): 
            return type(value)([self._wrap(v) for v in value])
        else:
            return Struct(value) if isinstance(value, dict) else value
    
    def __repr__(self):
        return str(self.__dict__)