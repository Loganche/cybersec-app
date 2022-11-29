import sys

import atheris

atheris.instrument_all()

atheris.Setup(sys.argv)
atheris.Fuzz()
