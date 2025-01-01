def calculate(expression):
    return eval(expression)

def checker(function):
    def checker(*args, **kwargs):
        try:
            result = function(*args, **kwargs)
        except Exception as exc:
            print("We have problem")
            raise exc
        else:
            print(f"No problem, result - {result}")
    return checker


@checker
def calculate(expression):
    return eval(expression)
calculate("34**3")