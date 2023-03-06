from pythonfuzz.main import PythonFuzz
from requests import post


@PythonFuzz
def fuzz(buf):
    try:
        string = buf.decode(errors='replace')
        form = {'username': string[:len(string) // 2], 'password': string[len(string) // 2:]}
        post(url='http://127.0.0.1:8000/auth/token', data=form)
    except Exception as e:
        print(e.args)
        raise Exception("fuzzing stopped")


if __name__ == '__main__':
    fuzz()
