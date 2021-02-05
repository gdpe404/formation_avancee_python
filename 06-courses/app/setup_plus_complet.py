# exemple d'un setup.py plus complet
# https://python.jpvweb.com/python/mesrecettespython/doku.php?id=cx_freeze

import sys
from cx_Freeze import setup, Executable

includefiles = []
#Inclure les fichiers specifiques au systemes
if sys.platform == "win32":
    # traitement pour window
    pass
elif sys.platform == "linux2":
    # traitement pour linux
    pass
else:
    # traitement pour linux
    pass

binpathincludes = []
if sys.platform == "linux2":
    binpathincludes += ["/usr/lib"]
 
setup(
    name="Entreprise",
    version="0.1",
    description="Gestion d'entreprise",
    author='LESUEUR Yohann',
    options={
        "include_files": includefiles,
        "bin_path_includes": binpathincludes,
    },
    executables=[Executable(
        script='app.py',
        icon="dawan-logo.ico",
    )]
)   