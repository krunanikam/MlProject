#building our application as package itself

from setuptools import find_packages,setup
from typing import List


hypen_e_dot='-e .'
def get_req(file_path)->List[str]:
    #this function return list of req
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if hypen_e_dot in requirements:
            requirements.remove(hypen_e_dot)
    return requirements



setup(
    name="mlproject",
    version='0.001',
    author='Karuna',
    author_email='karunanikam379@gmail.com',
    packages=find_packages(),
    install_req=get_req('requirements.txt')
)