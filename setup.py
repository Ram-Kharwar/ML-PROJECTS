from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return a list of requirements.
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip()]  # Remove empty lines

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)  # Remove '-e .' if it exists

    return requirements



setup(
    name="ML-PROJECT",
    version= "0.0.1",
    author="RAMPRAVESH",
    author_email="ramkharwar52@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")

)
