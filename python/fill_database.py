import json
import random

import requests
from faker import Faker

faker = Faker()


def fill_database(quantity):
    """This script fills a database table

    Args:
        quantity (int): The quantity of registers to insert in database
    """
    for i in range(0, quantity):
        url = "http://localhost:4130/v1/client"
        headers = {
            "Content-Type": "application/json"
        }
        payload = {
            "life_style": faker.text(),
            "birth_date": faker.date(),
            "status": True,
            "genre": random.choice(["male", "female"]),
            "password": "123456",
            "taxpayer": faker.random_number(digits=10),
            "cell_phone": faker.phone_number(),
            "interests": random.choice(["male", "female"]),
            "sexual_orientation": random.choice(["male", "female"]),
            "email": faker.email(),
            "bio": faker.text(),
            "name": faker.name()
        }
        r = requests.post(url, headers=headers, data=json.dumps(payload))
        print(r.text)


fill_database(15)
