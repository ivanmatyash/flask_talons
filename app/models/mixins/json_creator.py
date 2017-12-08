
class WithJsonCreate(object):

    def get_properties(self):
        return ""

    def get_json(self):
        JSON_dict = {key : self.__getattribute__(key)  for key in self.get_properties()}
        return JSON_dict