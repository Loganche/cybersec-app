from pythonfuzz.main import PythonFuzz
from requests import post


@PythonFuzz
def fuzz(buf):
    try:
        string = buf.decode('ascii')
        form = {'username': string[:len(string) // 2], 'password': string[len(string) // 2:]}
        post(url='http://127.0.0.1:8000/auth/token', data=form)
    except Exception:
        pass


if __name__ == '__main__':
    fuzz()
