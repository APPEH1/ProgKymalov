#індивідуальна робота

"""В даному коді реалізовано 5 тестів для роботи з Базою Даних:
   Тест1: Тест реалізує отримання адреси користувача згідно
          його імені та робить перевірку очікуваої адреси
   Тест2: Тест опрацьовує метод, який надає адресу, яка
          не існує в БД. Також додаткова перевірка: чи є результат
          порожнім списком
   Тест3: Тест для отримання деталей замовлення. Присутня перевірка:
          чи не порожнє замовлення
   Тест4: Цей тест написаний для оновлення твоару за його ID.Також
          реалізована перевірка, чи відповідає нинішня кількість
          товару очікуваній кількості
   Тест5: Тест реалізує додавання та видалення доданого користувача.
          Також є перевірка, чи дійсно користувач був видалений
          
   Також кожен тест закривє з'єднання з БД для запобігання
   помилок при "блокуванні" одного тесту іншим.
   У випадку великої кількості тестів було б зручно використати
   фікстури, але враховуючи, що їх у нас небагато, то прописали
   закриття з'єднання в саміх тестах"""

import pytest
from modules.common.database import Database
    

@pytest.mark.database
def test_get_data_by_id_existing():
    db = Database()
    db.insert_user(1, 'Sergii', 'Maydan Nezalezhnosti 1', 'Kyiv', '3127', 'Ukraine')
    result = db.get_user_address_by_name('Serg  ii')
    assert result == [('Maydan Nezalezhnosti 1', 'Kyiv', '3127', 'Ukraine')]
    db.close()

@pytest.mark.database
def test_get_data_by_id_non_existing():
    db = Database()
    result = db.get_user_address_by_name(999)
    assert len(result) == 0
    db.close()

@pytest.mark.database
def test_get_detailed_orders():
    db = Database()
    orders = db.get_detailed_orders()
    assert len(orders) > 0  
    db.close()

@pytest.mark.database
def test_update_product_quantity():
    db = Database()
    db.update_product_qnt_by_id(2, 50)  
    product_quantity = db.select_product_qnt_by_id(2)
    assert product_quantity[0][0] == 50 
    db.close()

@pytest.mark.database
def test_delete_user_by_id():
    db = Database()
    db.insert_user(700, 'David', '987 Lane', 'City', '67890', 'Country')
    existing_user_before_deletion = db.get_user_address_by_name('David')
    assert len(existing_user_before_deletion) > 0 
    db.delete_user_by_id(700)
    deleted_user_address = db.get_user_address_by_name('David')
    assert len(deleted_user_address) == 0
    db.close()