from setuptools import setup


setup(
      name='my_custom_sklearn_transforms_achermida',
      version='1.0',
      description='''
            This is a sample python package for encapsulating custom
            tranforms from scikit-learn into Watson Machine Learning
            based on Vanderlei Munhoz's - vnderlev@protomail.ch 
            version
      ''',
      url='https://github.com/achermidabr/sklearn_transforms_achermida/',
      author='Alexandre Hermida',
      author_email='achermida@gmail.com',
      license='BSD',
      packages=[
            'my_custom_sklearn_transforms_achermida'
      ],
      zip_safe=False
)
