"""Автотесты для сущности Student (добавление, изменение, удаление)."""
import pytest
from sqlalchemy.orm import Session
from database import Student


def test_add_student(db_session: Session) -> None:
    """Тест на успешное добавление новой сущности в БД."""
    new_student = Student(name="New Student", email="new_unique@example.com")
    db_session.add(new_student)
    db_session.commit()

    # Проверка успешности операции через чтение из БД
    db_student = db_session.query(Student).filter_by(email="new_unique@example.com").first()
    assert db_student is not None
    assert db_student.name == "New Student"

    # Очистка данных после теста (требование задания)
    db_session.query(Student).filter_by(id=db_student.id).delete()
    db_session.commit()


def test_update_student(created_student: Student, db_session: Session) -> None:
    """Тест на успешное изменение существующей сущности в БД."""
    new_name = "Updated Student Name"
    
    # Изменение сущности
    created_student.name = new_name
    db_session.commit()

    # Проверка успешности операции (сбрасываем кэш сессии для чистоты эксперимента)
    db_session.expire(created_student)
    updated_student = db_session.query(Student).filter_by(id=created_student.id).first()
    
    assert updated_student is not None
    assert updated_student.name == new_name
    # Данные удалятся автоматически фикстурой created_student


def test_delete_student(db_session: Session) -> None:
    """Тест на успешное удаление сущности из БД."""
    # 1. Создаем данные для удаления
    student_to_delete = Student(name="ToDelete Student", email="delete_unique@example.com")
    db_session.add(student_to_delete)
    db_session.commit()
    student_id = student_to_delete.id

    # 2. Выполняем удаление (Hard delete)
    db_session.query(Student).filter_by(id=student_id).delete()
    db_session.commit()

    # 3. Проверка успешности операции (сущности больше нет в БД)
    deleted_student = db_session.query(Student).filter_by(id=student_id).first()
    assert deleted_student is None

    # Примечание: если в вашей БД реализован Soft Delete, 
    # вместо .delete() нужно делать:
    # student_to_delete.is_deleted = True
    # db_session.commit()
    # И проверять: assert deleted_student.is_deleted is True