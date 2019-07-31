from distutils.core import setup
import setuptools

with open('README.md', 'r', encoding='utf-8') as readme:
    long_description = readme.read()

setup(
    name='phone_email_verifier',
    version='0.0.4',
    description='Validation of the email or international or local telephone number',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Christian BOGRO',
    author_email='bogrolcr@gmail.com',
    license='MIT',
    url='https://github.com/Bogro/phone_email_verifier',
    packages=setuptools.find_packages(),
    download_url='https://github.com/Bogro/phone_email_verifier/tarball/master',
    keywords = ['email', 'phone number', 'filter', 'blocking', 'text', 'phone local', 'phone international'],
)