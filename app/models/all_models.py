from app.models.roles import Role
from app.models.user import User
from app.models.doctors import Doctor
from app.models.speciality import Speciality
from app.models.poly import Polyclinic
from app.models.timetable import Timetable

all_models =[
    Role,
    User,
    Doctor,
    Speciality,
    Polyclinic,
    Timetable
]

__all__ = [item.__name__ for item in all_models]