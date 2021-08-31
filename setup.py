from setuptools import find_packages, setup

setup(
    name='netbox-workflow',
    version='0.1',
    description = "Netbox Plugins - add workflow to Netbox",
    url='https://github.com/zerdliu/netbox-plugin-workflow',
    author='Ezra Liu',
    license='Apache 2.0',
    install_requires=['viewflow'],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
