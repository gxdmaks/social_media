from database.models import User
from datetime import datetime

from database import get_db

# Регистрация пользователя
def register_user_db(name, email, phone_number, password, users_city):
    db = next(get_db())
    # Создаем класс нового пользователя
    new_user = User(name=name, email=email, phone_number=phone_number,
                    password=password, users_city=users_city, reg_date=datetime.now())

    # Добавляем в базу
    db.add(new_user)
    db.commit()

    return new_user.id


# Проверка на наличие в базе пользователя
def check_user_data_db(phone_number, email):
    db = next(get_db())
    # Проверка данных на наличие записи в базе
    checker = db.query(User).filter_by(phone_number=phone_number, email=email).first()
    # Если есть совпадение
    if checker:
        return False
    # Если нет совпадений
    return True
# Проверка пароля пользователя
def check_user_password_db(email, password):
    db = next(get_db())
    # Попробуем найти пользователя
    checker = db.query(User).filter_by(email=email).first()
    # Если нашел проверяем правильность
    if checker:
        # Начинаем сверку пароля
        if checker.password == password:
            return checker.id

        else:
            return 'Неверный пароль'

    # Если не находят данные в базе
    return 'Неверная почта'

# Получить инфу о пользователе
def profile_info_db(user_id):
    db = next(get_db())

    # Нахождение пользователя через id
    exact_user = db.query(User).filter_by(id=user_id).first()

    # Если нашел пользователя передовай всю информацию про него
    if exact_user:
        return exact_user.email,\
            exact_user.phone_number,\
            exact_user.id,exact_user.name, \
            exact_user.reg_date, exact_user.users_city

    return 'Пользователь не найден'

# Изменение данных пользователя
def change_user_data(user_id, change_info, new_data):
    db = next(get_db())
    # Находим пользователя
    exact_user = db.query(User).filter_by(id=user_id).first()
    # Проверка того какую информацию хочет изменить пользователь
    if exact_user:
        if change_info == 'email':
            exact_user.email = new_data

        elif change_info == 'number':
            exact_user.phone_number = new_data

        elif change_info == 'name':
            exact_user.name = new_data

        elif change_info == 'city':
            exact_user.users_city = new_data

        elif change_info == 'password':
            exact_user.password = new_data

        db.commit()

        return 'Данные успешно изменены'

    return  'Пользователь не найден'

# Сброс пароля
