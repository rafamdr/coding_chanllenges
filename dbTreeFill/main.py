from collections import Counter

# ----------------------------------------------------------------------------------------------------------------------


memory_data_array = [
    {'jira': '123', 'stb': 'STB_06', 'type': 'GPT01', 'uptime': 13, 'freemem': 0.0, 'model': 'HS17', 'rack': 'F20_HUMw7'},
    {'jira': '123', 'stb': 'STB_06', 'type': 'GPT01', 'uptime': 11, 'freemem': 2.0, 'model': 'HS17', 'rack': 'F20_HUMw7'},
    {'jira': '123', 'stb': 'STB_06', 'type': 'GPT02', 'uptime': 13, 'freemem': 0.0, 'model': 'HS17', 'rack': 'F20_HUMw7'},
    {'jira': '123', 'stb': 'STB_07', 'type': 'GPT02', 'uptime': 14, 'freemem': 0.1, 'model': 'HS19', 'rack': 'asdfasdfa'}
]

keys_order = ['jira', 'model', 'rack', 'stb']
dict_mem_data = {}
for memory_data_row in memory_data_array:
    temp_dict = dict_mem_data
    uptime = memory_data_row.pop('uptime')
    freemem = memory_data_row.pop('freemem')
    for key in keys_order:
        if memory_data_row[key] not in temp_dict:
            temp_dict[memory_data_row[key]] = {}
        temp_dict = temp_dict[memory_data_row[key]]

    if 'dataset' not in temp_dict:
        temp_dict['dataset'] = []

    temp_dict['dataset'].append({'uptime': uptime, 'freemem': freemem})


a = 0
# ----------------------------------------------------------------------------------------------------------------------
