# settings which indicate if the libraries 'pillow' and 'numba' are installed
settings = {
    "pil_installed": False,
    "numba_installed": False
}

# array that contains error messages
notes = []

try:
    import PIL
    settings["pil_installed"] = True
except ModuleNotFoundError:
    notes.append("Fast mode is disabled because PIL is not installed. To install PIL, run 'pip3 install pillow' in a terminal")

try:
    import numba
    settings["numba_installed"] = True
except ModuleNotFoundError:
    notes.append("The program wil run slower because numba is not installed. To install numba, run 'pip3 install numba' in a terminal")