""" python deps for this project """

install_requires: list[str] = [
    "google-api-python-client",
    "click",
]
build_requires: list[str] = [
    "pydmt",
    "pymakehelper",
]
requires = install_requires + build_requires
