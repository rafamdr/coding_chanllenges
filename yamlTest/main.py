import yaml
# ----------------------------------------------------------------------------------------------------------------------


class DictAsMember(dict):
    def __getattr__(self, name):
        value = self[name]
        if isinstance(value, dict):
            value = DictAsMember(value)
        elif isinstance(value, list):
            new_list = []
            for item in value:
                new_list.append(DictAsMember(item))
            value = new_list
        return value
# ----------------------------------------------------------------------------------------------------------------------


with open(r'./variables.yaml') as user_config_file:
    user_config = yaml.load(user_config_file, Loader=yaml.FullLoader)
    user_config2 = DictAsMember(user_config)
    print(user_config)

a = 0