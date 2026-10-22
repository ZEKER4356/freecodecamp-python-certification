test_settings = {
    'setting1': 10,
    'setting2': 20
}

def add_setting(dict_settings, tuple_key_value):

    key, value = tuple_key_value
    key_lower = key.lower()
    value_lower = value.lower()

    if key_lower in dict_settings:
        return f"Setting '{key_lower}' already exists! Cannot add a new setting with this name."
    else:
        dict_settings.update({key_lower: value_lower})
        return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(dict_settings, tuple_key_value):

    key, value = tuple_key_value
    key_lower = key.lower()
    value_lower = value.lower()

    if key_lower in dict_settings:
        dict_settings.update({key_lower: value_lower})
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(dict_settings, key):
    dict(dict_settings)
    key_lower = key.lower()

    if key_lower in dict_settings:
        dict_settings.pop(key_lower)
        return f"Setting '{key_lower}' deleted successfully!"
    else:
        return 'Setting not found!'

def view_settings(dict_settings):
    if dict_settings == {}:
        return f'No settings available.'
    else:
        result = f'Current User Settings:\n'
        for keys, values in dict_settings.items():
            setting = f'{keys.capitalize()}: {values}\n'
            result += setting
        return print(result)

add_setting({'theme': 'light'}, ('volume', 'high'))
update_setting({'theme': 'light', 'language': 'English'}, ('theme', 'dark'))
view_settings({'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'})