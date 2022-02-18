from setuptools import setup,find_packages
setup(name='WooCommerceProject',
      version='1.0',
      description='Woocommerce Project',
      author='PK',
      packages= find_packages(),
      zip_safe=False,
      install_requires=[
        "pytest==6.2.5",
        "pytest-html==3.1.1",
        "requests==2.26.0",
        "requests-oauthlib==1.3.0",
        "PyMySQL==1.0.2",
        "WooCommerce==3.0.0",
      ]
)
