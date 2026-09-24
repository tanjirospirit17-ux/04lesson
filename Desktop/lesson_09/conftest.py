"""Фикстуры pytest для работы с базой данных."""
import pytest
from database import SessionLocal, Student


@pytest.fixture(scope="function")
def db_session():
    """Предоставляет сессию БД и закрывает её после теста."""
    session = SessionLocal()
    yield session
    session.close()


@pytest.fixture(scope="function")
def created_student(db_session):
    """Создает тестового студента и гарантирует его удаление после теста."""
    student = Student(name="Test Student", email="test_unique@example.com")
    db_session.add(student)
    db_session.commit()
    db_session.refresh(student)
    
    yield student
    
    # Teardown: гарантированное удаление созданных данных через БД
    db_session.query(Student).filter_by(id=student.id).delete()
    db_session.commit()