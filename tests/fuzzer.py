import sys

import atheris

with atheris.instrument_imports():
    import cybersec


def TestOneInput(data):
    cybersec.parse(data)


atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()
