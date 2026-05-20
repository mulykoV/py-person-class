class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    list_of_persons = []
    for person in people:
        persona = Person(
            name=person["name"],
            age=person["age"]
        )
        list_of_persons.append(persona)
    for per in people:
        list_of_keys = per.keys()
        if "wife" in list_of_keys and per["wife"] is not None:
            Person.people[per["name"]].wife = Person.people[per["wife"]]
        elif "husband" in list_of_keys and per["husband"] is not None:
            Person.people[per["name"]].husband = Person.people[per["husband"]]

    return list_of_persons
