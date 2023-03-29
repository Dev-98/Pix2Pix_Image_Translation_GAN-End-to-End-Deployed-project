from setuptools import setup,find_packages


def fetch_libraries(path:str):
    '''
    Returns all dependencies that will be required
    '''
    reqs=[]
    HYPHEN_DOT = '-e .'
    with open(path) as f:
        reqs = f.readlines()
        reqs = [r.replace('\n','') for r in reqs if r != HYPHEN_DOT]
        
    return reqs

setup(
    name="Practice",
    version="0.0.1",
    author="Dev",
    author_email="devparker48@gmail.com",
    packages=find_packages(),
    install_requires=fetch_libraries('requirements.txt')
)