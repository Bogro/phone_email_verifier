from distutils.core import setup

with open('README.md', 'r') as readme:
    long_description = readme.read()

setup(
    name='phone_email_verifier',
    version='0.0.1',
    description='Validation of the email or international or local telephone number',
    long_description=long_description,
    author='Christian BOGRO',
    author_email='bogrolcr@gmail.com',
    license='MIT',
    url='https://github.com/Bogro/phone_email_verifier',
    download_url='https://github.com/Bogro/phone_email_verifier/tarball/master',
    keywords = ['email', 'phone number', 'filter', 'blocking', 'text', 'phone local', 'phone international'],
)