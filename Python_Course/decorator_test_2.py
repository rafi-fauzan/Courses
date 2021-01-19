def burger_decorator(func):
    def wrapper(self, *args):
        return f'{args[0]}|{func(self, args[0], args[1])}|{args[1]}'
    return wrapper

class burger_generator:
    def __init__(self, name):
        self.name = name

    @burger_decorator
    def burger(self, top, bottom):
        return 'Beef'
    
# person_1 = burger_generator('Bill')
# person_1.burger('Cheese', 'Extra Chesse')

class sandwich_generator(burger_generator):
    def __init__(self, sandwich_preferable, *args):
        super(sandwich_generator, self).__init__(*args)
        self.sandwich_preferable = sandwich_preferable
    
    @classmethod
    @burger_decorator
    def burger(cls, top, bottom):
        return 'Beef'
    
    @classmethod
    @burger_decorator
    def hotdog(cls, top, bottom):
        return 'Sausage'
    
    @classmethod
    def not_available(cls):
        return 'Not Available'
    
    def sandwich(self, top='Tomatto', bottom='Salad'):
        if self.sandwich_preferable == 'Burger' or self.sandwich_preferable == 'burger' or self.sandwich_preferable == 'BURGER':
            sandwich = self.burger(top, bottom)
        elif self.sandwich_preferable == 'Hotdog' or self.sandwich_preferable == 'hotdog' or self.sandwich_preferable == 'HOTDOG':
            sandwich = self.hotdog(top, bottom)
        else:
            sandwich = self.not_available()
        return sandwich

person_1 = sandwich_generator('Hotdog', 'Marcus')
print(person_1.sandwich('Ketchup', 'Mustard'))
