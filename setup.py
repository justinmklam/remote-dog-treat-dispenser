import platform
from setuptools import find_packages, setup

required_pkgs = [
    "flask",
]

# Raspberry Pi specific packages
if "arm" in platform.uname().machine:
    required_pkgs.append(
        ["picamera"]
    )

setup(
    name="petcam",
    version="1.0.0",
    description="Remote pet camera and treat dispenser",
    author="Justin Lam",
    author_email="contact@justinmklam.com",
    url="https://github.com/justinmklam/remote-dog-treat-dispenser",
    packages=find_packages(),
    scripts=[],
    install_requires=required_pkgs,
    zip_safe=False,
)
