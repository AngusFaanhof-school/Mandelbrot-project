settings = {
    "pil_installed": False,
    "jit_installed": False
}

notes = []

try:
    import PIL
    settings["pil_installed"] = True
except ModuleNotFoundError:
    notes.append("Fast mode is disabled because PIL is not installed. To install PIL, run 'pip3 install pillow' in a terminal \n")

try:
    import numba
    settings["jit_installed"] = True
except ModuleNotFoundError:
    notes.append("The program wil run slower because numba is not installed. To install numba, run 'pip3 install numba' in a terminal")