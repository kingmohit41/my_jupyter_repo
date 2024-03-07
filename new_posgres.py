import random
import string

def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters, k=length))

def generate_list_of_dicts():
    length=100
    data = []
    for _ in range(length):
        person = {
            "name": generate_random_string(8),
            "age": random.randint(18, 80),
            "city": generate_random_string(6)
        }
        data.append(person)
    return data
