import pickle

import requests

from model.students.tech.TechMember import TechMember

if __name__ == "__main__":
    base_url = 'http://localhost:9000/'
    add_member_url = base_url + 'addMember'
    get_members_url = base_url + 'getMembers'

    while True:
        op = int(input("(1) Add member\n(2) List members\nSelect Operation: "))
        if op == 1:
            name = input("Enter name: ")
            major = input("Enter major: ")
            grad_date = input("Enter graduation year: ")
            member = TechMember(name, major, grad_date)
            serialized = pickle.dumps(member)
            print(requests.post(add_member_url,
                                headers={
                                    'Content-Length': str(len(serialized))
                                },
                                data=serialized).text)
        elif op == 2:
            print(pickle.loads(requests.get(get_members_url).content))
