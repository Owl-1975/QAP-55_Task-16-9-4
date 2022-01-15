class Volunteer:
    def __init__(self, surname='', name='', city=''):
        self.surname = surname
        self.name = name
        self.city = city

class Guest(Volunteer):
    def __init__(self, surname, name, city, status):
        super().__init__(name, surname, city)
        self.status = status
    def guest_list(self):
        return f'{self.name} {self.surname}, г.{self.city}, статус {self.status}'

list_employees = [{'surname': 'White', 'name': 'John', 'city': 'Boston', 'job': 'Staff Member', 'status': 'Shareholder'},
    {'surname': 'Green', 'name': 'Philip', 'city': 'London', 'job': 'Staff Member', 'status': 'Auditor'},
    {'surname': 'Black', 'name': 'Roger', 'city': 'Cupertino', 'job': 'Staff Member', 'status': 'Bookkeeper'},
    {'surname': 'Белявский', 'name': 'Евгений', 'city': 'Санкт-Петербург', 'job': 'Volunteer', 'status': 'Наставник'},
    {'surname': 'Зеленков', 'name': 'Филипп', 'city': 'Москва', 'job': 'Volunteer', 'status': 'Наставник'},
    {'surname': 'Черных', 'name': 'Роман', 'city': 'Омск', 'job': 'Volunteer', 'status': 'Координатор'}
]

print()
print('Список приглашённых: ')
print()
for list_e in list_employees:
    for e in list_e:
        if e == 'job' and list_e['job'] == 'Volunteer':
            guest = Guest(list_e['name'], list_e['surname'], list_e['city'], list_e['status'])
            print(guest.guest_list())
