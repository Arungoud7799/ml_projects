from setuptools import find_packages, setup

from typing import List

HYPEN_E_DOT = "-e ."
def get_requirements(file_path:str)->List[str]:
    """_summary_

    Args:
        It takes a requirements.txt

    Returns:
        List[str]: returns all requirements
    """
    
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
    name = "mlproject",
    version="0.0.1",
    author = "Arun",
    author_email="thallapallyarun49@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements("requirements.txt"),
)