def test_function():

    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function()

test_function() # вызов функции 

#inner_function() # функция не может быть вызвана вне функции test_function, т.к. находится в другом пространстве





