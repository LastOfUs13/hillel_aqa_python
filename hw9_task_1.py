class Business():

    def __init__(self, title=None, foundation_year=None, specialize=None, regional_offices=None,
                 ceo=None):
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
            raise TypeError

    @foundation_year.setter
    def foundation_year(self, new_foundation_year):
        if isinstance(new_foundation_year, int) and len(str(new_foundation_year)) == 4:
            self.__foundation_year = new_foundation_year
        else:
            raise TypeError

    @specialize.setter
    def specialize(self, new_specialize):
        if isinstance(new_specialize, str):
            self.__specialize = new_specialize
        else:
            raise TypeError

    @regional_offices.setter
    def regional_offices(self, new_regional_offices):
        if isinstance(new_regional_offices, str):
            self.__regional_offices = new_regional_offices
        else:
            raise TypeError

    @ceo.setter
    def ceo(self, new_ceo):
        if isinstance(new_ceo, str):
            self.__ceo = new_ceo
        else:
            raise TypeError

    @staticmethod
    def tell_about_ceo():
        return f"{company.ceo} was a engineer, and born leader."

    @staticmethod
    def tell_about_company():
        return f"{company.title} was created in {company.foundation_year} by {company.ceo} and few his friends"

    @staticmethod
    def calculate_how_old_company():
        import datetime
        nova_days = datetime.datetime.now().year
        res = nova_days - 1976
        return f"Company {company.title} is a {res} years success continuous development"

    @classmethod
    def describe_company_shortly(cls, title, specialize, regional_offices):
        return f"{title} specialized on {specialize},two most developed company regional offices in {regional_offices}"


if __name__ == '__main__':
    company = Business()

