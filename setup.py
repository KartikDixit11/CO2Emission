from setuptools import setup,find_packages
HYPEN_DOT_E="-e."

def req(file_path):
    requirement=[]
    with open(file_path) as file_obj:
            requirement=file_obj.readlines()
            [r.replace("\n","") for r in requirement]

    if HYPEN_DOT_E in requirement:
                  requirement.remove(HYPEN_DOT_E)
    
    return requirement

    



setup(
    name="CO2EmissionPredication",
    version='0.0.1',
    author="Kartik",    
    author_email="kpd1111@gmail.com",
    install_requires=req("requirements.txt"),
    packages=find_packages()
)