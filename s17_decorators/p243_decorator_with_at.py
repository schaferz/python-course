import functools

user = {'username': 'jose123', 'access_level': 'admin'}


def user_has_premission(func):
    @functools.wraps(func)
    def secure_func(*args, **kwargs):
        if user.get('access_level') == 'admin':
            return func(*args, **kwargs)

    return secure_func


@user_has_premission
def my_function(panel):
    return f'Password for admin {panel} is 1234'


print(my_function('movies'))
