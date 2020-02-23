import json


def read_json(path):
    with open(path, 'r') as file:
        decoded_user = json.load(file)
    return decoded_user

# import doctest
# print(doctest.testmod())
if __name__ == '__main__':
    import pprint
    user_data = (read_json('res/elonmusk.json'))
    print(user_data.keys())
    print(user_data['ids'])
    print(user_data['next_cursor'])
    print(user_data['next_cursor_str'])
    print(user_data['previous_cursor'])
    print(user_data['previous_cursor_str'])
    print(user_data['total_count'])
