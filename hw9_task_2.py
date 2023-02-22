class Staff():

    def __init__(self, name=None, gender=None, age=None, job_position=None, years_experience=None):
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
            raise TypeError

    @gender.setter
    def gender(self, staff_gender):
        if isinstance(staff_gender, str) and staff_gender == 'male' or staff_gender == 'female':
            self.__gender = staff_gender
        else:
            raise TypeError

    @age.setter
    def age(self, staff_age):
        condition = staff_age >= 18 and staff_age <= 65
        if isinstance(staff_age, int) and condition:
            self.__age = staff_age
        else:
            raise TypeError

    @job_position.setter
    def job_position(self, staff_job_position):
        if isinstance(staff_job_position, str):
            self.__job_position = staff_job_position
        else:
            raise TypeError

    @years_experience.setter
    def years_experience(self, staff_years_experience):
        self.__years_experience = staff_years_experience

    @staticmethod
    def hi_to_new_staff():
        return f"Say 'Hello' to our new {employee.job_position}-{employee.name}"

    @classmethod
    def create_new_staff(cls, job_position, name):
        return f"{job_position} {name} was created"

    def calculate_allowance_percentage(self):
        allowance_percentage = self.years_experience * 0.5
        return f"current allowance percentage for relevant employee is equal {allowance_percentage}"


if __name__ == '__main__':
    employee = Staff()

