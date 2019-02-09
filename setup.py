from setuptools import setup, find_packages

setup(
  name='selenium-locust',
  packages=find_packages(),
  version='0.1.dev0',
  description=(
    'Minimal set of real browser (Firefox, Chrome and PhantomJS) locusts to be used in conjunction with locust.io'
  ),
  author='Nick Bocuart',
  author_email='nboucart@gmail.com',
  url='https://github.com/nickboucart/realbrowserlocusts',
  download_url='https://github.com/nickboucart/realbrowserlocusts/tarball/0.3',
  keywords=['testing', 'locust'],
  classifiers=[],
  install_requires=[
    'selenium',
  ]
)
