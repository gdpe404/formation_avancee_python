# pip install cx_Freeze
# Creer un executable: python setup.py build
from cx_Freeze import setup, Executable

setup(
    name="Entreprise",
    version="0.1",
    description="Gestion d'entreprise",
    executables=[Executable('app.py')]
)
