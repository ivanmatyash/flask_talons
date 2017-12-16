from app.models.user import User
from app.models.doctors import Doctor
from app.models.speciality import Speciality
from app.models.poly import Polyclinic
from app.models.timetable import Timetable
from app.models.week_timetable import WeekTimetable

all_models =[
    User,
    Doctor,
    Speciality,
    Polyclinic,
    Timetable,
    WeekTimetable
]

__all__ = [item.__name__ for item in all_models]