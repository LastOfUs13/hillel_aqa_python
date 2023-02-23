class Business():

    def __init__(self, title: str = None, foundation_year: int = None, specialize: str = None,
                 regional_offices: list = None,
                 ceo: str = None):
        self.__title = title
        self.__foundation_year = foundation_year
        self.__specialize = specialize
        self.__regional_offices = regional_offices
        self.__ceo = ceo

    @property
    def title(self):
        return self.__title

    @property
    def foundation_year(self):
        return self.__foundation_year

    @property
    def specialize(self):
        return self.__specialize

    @property
    def regional_offices(self):
        return self.__regional_offices

    @property
    def ceo(self):
        return self.__ceo

    @title.setter
    def title(self, new_title):
        if isinstance(new_title, str):
            self.__title = new_title
        else:
            raise TypeError("this data must be a string")

    @foundation_year.setter
    def foundation_year(self, new_foundation_year):
        import datetime
        condition = new_foundation_year >= 1900 and new_foundation_year <= datetime.datetime.now().year
        if isinstance(new_foundation_year, int) and condition and len(str(new_foundation_year)) == 4:
            self.__foundation_year = new_foundation_year
        else:
            raise TypeError("this data must be an int (available diapason: 1900-current year)")

    @specialize.setter
    def specialize(self, new_specialize):
        if isinstance(new_specialize, str):
            self.__specialize = new_specialize
        else:
            raise TypeError("this data must be a string")

    @regional_offices.setter
    def regional_offices(self, new_regional_offices):
        if isinstance(new_regional_offices, list):
            self.__regional_offices = new_regional_offices
        else:
            raise TypeError("this data must be a list")

    @ceo.setter
    def ceo(self, new_ceo):
        if isinstance(new_ceo, str):
            self.__ceo = new_ceo
        else:
            raise TypeError("this data must be a string")

    @staticmethod
    def calculate_how_old_company(foundation_year):
        import datetime
        years_old = datetime.datetime.now().year - foundation_year
        return years_old

    @classmethod
    def create_company_shortly(cls, title, specialize):
        return cls(title, specialize)

    def tell_about_company(self):
        return f"{self.title} was created in {self.foundation_year} by {self.ceo} and few his friends"

    def tell_about_ceo(self):
        return f"{self.ceo} was a engineer, and born leader."


if __name__ == '__main__':
    Business.create_company_shortly('Sony Entertainment', 'game development')
