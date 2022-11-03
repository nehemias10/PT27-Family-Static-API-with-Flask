"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
            {
                "name": "John",
                "id": self._generateId(),
                "last_name": self.last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "name": "Jane",
                "id": self._generateId(),
                "last_name": self.last_name,
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "name": "Jimmy",
                "id": self._generateId(),
                "last_name": self.last_name,
                "age": 5,
                "lucky_numbers": [1, 2]
            }
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        if member["age"] >= 0 and member["name"] != None and member["lucky_numbers"] != None:
            member["last_name"] = self.last_name
            member["id"] = self._generateId()
            self._members.append(member)
            return "Registro agregado con exito"
        else:
            return "Falta información"
        ##pass

    def delete_member(self, member_id):
        for x in range (len(self._members)):
            if self._members[x]["id"] == member_id:
                self._members.pop(x)
                return "Registro eliminado con exito"
        ##pass

    def get_member(self, member_id):
        for x in range (len(self._members)):
            if self._members[x]["id"] == member_id:
                return self._members[x]
        pass

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members