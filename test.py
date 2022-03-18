from requests import get, post, delete
import random

# print(post('http://127.0.0.1:8070/api/jobs').json())  # пустой запрос
#
# print(post('http://127.0.0.1:8070/api/jobs',  # incorrect tables
#            json={'title': 'Заголовок',
#                  'content': 'Текст новости',
#                  'user_id': 1,
#                  'is_private': False}).json())
#
# print(post('http://127.0.0.1:8070/api/jobs',  # корректно
#            json={'id': random.randint(5, 10000000),
#                  'team_leader': 1,
#                  'job': 'тестовая работа',
#                  'work_size': 2,
#                  'collaborators': '2, 4, 6',
#                  'is_finished': 0}).json())
#
# print(post('http://127.0.0.1:8070/api/jobs',  # is_finished not Boolean
#            json={'id': random.randint(5, 10000000),
#                  'team_leader': 1,
#                  'job': 'тестовая работа',
#                  'work_size': 2,
#                  'collaborators': '2, 4, 6',
#                  'is_finished': 2}).json())
#
# print(post('http://127.0.0.1:8070/api/jobs',  # Id already exists
#            json={'id': 1,
#                  'team_leader': 2,
#                  'job': 'тестовая работа',
#                  'work_size': 2,
#                  'collaborators': '2, 4, 6',
#                  'is_finished': 1}).json())


print(get('http://127.0.0.1:8070/api/user').json())  # есть в базе
# print(get('http://127.0.0.1:8070/api/user/999').json())  # нет в базе
# print(get('http://127.0.0.1:8070/api/news'))

# print(delete('http://127.0.0.1:8070/api/user/4'))  # успешное удаление

print(post('http://127.0.0.1:8070/api/user', json={'name': 'test_user1',  # УДАЧНОЕ
                                                   'surname': 'dsfdssda',
                                                   'email': 'test_user11@gmail.com',
                                                   'password': 'Qwerty1234',
                                                   'age': 17,
                                                   'speciality': 'test1',
                                                   "position": 'test1',
                                                   'address': 'test1'}))
