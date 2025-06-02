import setuptools

setuptools.setup(
    name='audio-speech-to-sign-language-converter',
    version='0.1.0',
    description='Python project',
    author='Mukesh Negi',
    author_email='negimukesh2056@gmail.com',
    url='https://github.com/Mukesh-Negi/Audio-to-signed-language---Mukesh-and-Sanya.git',
    packages=setuptools.find_packages(),
    setup_requires=['nltk', 'joblib','click','regex','sqlparse','setuptools'],
)