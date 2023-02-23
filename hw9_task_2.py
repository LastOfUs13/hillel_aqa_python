class Staff():

    def __init__(self, name: str = None, gender: str = None, age: int = None, job_position: str = None,
                 years_experience: int = None):
        self.__name = name
        self.__gender = gender
        self.__age = age
        self.__job_position = job_position
        self.__years_experience = years_experience

    @property
    def name(self):
        return self.__name

    @property
    def gender(self):
        return self.__gender

    @property
    def age(self):
        return self.__age

    @property
    def job_position(self):
        return self.__job_position

    @property
    def years_experience(self):
        return self.__years_experience

    @name.setter
    def name(self, staff_name):
        if isinstance(staff_name, str):
            self.__name = staff_name
        else:
            raise TypeError("this data must be a string")

    @gender.setter
    def gender(self, staff_gender):
        GENDER = ['male', 'female']
        if isinstance(staff_gender, str) and staff_gender in GENDER:
            self.__gender = staff_gender
        else:
            raise TypeError("this data must be a string ('male' or 'female')")

    @age.setter
    def age(self, staff_age):
        condition = staff_age >= 18 and staff_age <= 65
        if isinstance(staff_age, int) and condition:
            self.__age = staff_age
        else:
            raise TypeError("this data must be an int (available diapason: 18-65 years)")

    @job_position.setter
    def job_position(self, staff_job_position):
        if isinstance(staff_job_position, str):
            self.__job_position = staff_job_position
        else:
            raise TypeError("this data must be a string")

    @years_experience.setter
    def years_experience(self, staff_years_experience):
        if isinstance(staff_years_experience, int) and staff_years_experience > 0 and len(
                str(staff_years_experience)) == 4:
            self.__years_experience = staff_years_experience
        else:
            raise TypeError("this data must be an int")

    @staticmethod
    def calculate_allowance_percentage(years_experience):
        allowance_percentage = years_experience * 0.5
        return allowance_percentage

    @classmethod
    def create_new_staff(cls, job_position, name):
        return cls(job_position, name)

    def hi_to_new_staff(self):
        return f"Say 'Hello' to our new {self.job_position}-{self.name}"


if __name__ == '__main__':
    Staff.create_new_staff('Misha', 'cleaner')

