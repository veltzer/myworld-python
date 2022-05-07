import config.project

package_name = config.project.project_name

install_requires = [
    "google-api-python-client",
    "click",
]
dev_requires = [
    "pymakehelper",
    "pydmt",
    "pyclassifiers",
]

python_requires = ">=3.9"
test_os = ["ubuntu-20.04"]
test_python = ["3.9"]
