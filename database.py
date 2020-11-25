# coding=utf-8
import pyrebase
import random

def noquote(s):
    return s
pyrebase.pyrebase.quote = noquote

firebaseConfig = {'apiKey': "AIzaSyCcFUTbszDhbcZxCuXqM85MWr80FPhvY58",
   'authDomain': "dormitory-c5829.firebaseapp.com",
    'databaseURL': "https://dormitory-c5829.firebaseio.com",
    'projectId': "dormitory-c5829",
    'storageBucket': "dormitory-c5829.appspot.com",
    'messagingSenderId': "282371830331",
    'appId': "1:282371830331:web:c8c5c754d20184a045221e",
    'measurementId': "G-QZSM07QZ73"}

db = pyrebase.initialize_app(firebaseConfig).database()

# def init_firebase(firebaseConfig):
#
#     return firebase.database()

# функции общежития
def add_dormitory(number,address):
    dormitoryData = {'number': number, 'Rooms': {0:''}, 'name': 'Общежитие ' + str(number), 'Адрес':address}
    db.child('dormitory' + str(number)).set(dormitoryData)


def list_of_dormitories():
    '''отдает массив с общагами формат – '''
    pass


def update_number_of_rooms():
    pass


# функции комнаты
def add_room(dormitory, number, capacity):
    roomData = {'number': number, 'capacity': capacity, 'occupied': 0, 'status': 'Свободна'}
    db.child('dormitory' + str(dormitory)).child('Rooms').child(roomData['number']).set(roomData)


def list_off_all_rooms():
    '''список комнат формата'''
    pass


def update_rooms_status():
    pass


# функции студента
def add_student(fio, phone, passport, address, educ_form, gender, dormitory):
    '''добавление студента'''
    student_data = {'ФИО': fio, 'Телефон': phone, 'Паспорт': passport, 'Адрес регистрации': address,
                    'Форма обучения': educ_form, 'Пол': gender, 'Комната':'queue', 'Общежитие':dormitory}

    fio_mas = student_data['ФИО'].split()
    name_tag = fio_mas[0] + fio_mas[1][0] + fio_mas[2][0]
    # добавление в бд
    db.child('clients').child(name_tag).set(student_data)

# добавить в бомжатник

def edit_student():
    # = найти, удалить добавить
    pass


def delete_student(fio):
    '''удаление студента'''
    searched_mas = search_student(fio)


def search_student(fio):
    '''данные формата [(фио,№_общаги,комната,{данные}),(...)]'''
    name_mas = fio.split()
    name = name_mas[0] + name_mas[1][0] + name_mas[2][0]

    searched_names = db.child('clients').order_by_child('ФИО').equal_to(fio).get()
    print(searched_names.each())

    # searched_students = []
    # for dormitory in searched_mas.each():
    #     dorm_number = dormitory.val()['number']
    #     rooms = dormitory.val()['Rooms']
    #     for room_ind in rooms.keys():
    #         room = rooms[room_ind]
    #         if 'Residents' in room.keys():
    #             residents = room['Residents']
    #             if name in residents.keys():
    #                 searched_students.append((name,str(dorm_number),room_ind,residents[name]))
    # return searched_students




def list_off_all_students():
    '''список список студентов по всем обежитиям'''
    pass




# функции договора


# # инициализирование бд
# # Данные договора
# contractData = {'number': 'ОБ1'}
#
# # Данные студента
# studentData = {'lastname': 'Романенко', 'name': 'Владимир', 'contract': contractData}
# residentsData = {studentData['lastname'] + studentData['name'][0]: studentData}
#
# # Данные комнаты
# roomData = {'number': 315, 'capacity': 3, 'occupied': 0, 'status':'свободна', 'residents': residentsData}
# roomsData = {roomData['number']: roomData}
#
# # Данные общежития
# dormitoryData = {'number': 1, 'Rooms': roomsData, 'name': 'Общежитие 1'}
# dormitorysData = {'dormitory' + str(dormitoryData['number']): dormitoryData}
#
# db.set(dormitorysData)

# создаю комнаты

# for number in range(100,106):
#     dormitory = 2
#     capacity = random.randint(2,3)
#     add_room(dormitory,number,capacity)
#
# for number in range(200,206):
#     dormitory = 2
#     capacity = random.randint(2, 3)
#     add_room(dormitory,number,capacity)
#
# for number in range(300,306):
#     dormitory = 2
#     capacity = random.randint(2, 3)
#     add_room(dormitory,number,capacity)
#
# for number in range(400,406):
#     dormitory = 2
#     capacity = random.randint(2, 3)
#     add_room(dormitory,number,capacity)
#
# for number in range(500,506):
#     dormitory = 2
#     capacity = random.randint(2, 3)
#     add_room(dormitory,number,capacity)

# добавляю жителей

if __name__ == '__main__':
    # a = {'ab':{'e':'f'}, 'c':{'j':'h'}}
    #
    # for r in a.keys():
    #     print(a[r])
    # add_student('Romanenko V Y','88005553535','324343234','Москва','бюджет','мужской',1)

    # search_student('Романенко Владимир Юрьевич')

    print(db.child('dormitories').order_by_child('number').equal_to(1).get())



    # for each in searched_mas.each():
    #     if 'Residents' in each.val().keys():
    #         if name in each.val()['Residents'].keys():
    #             print(each.val()['Residents'][name])
    #         else:
    #             print('Не найдено')
