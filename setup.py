from setuptools import setup, find_packages
import sys

# This appears to be necessary so that versioneer works:
sys.path.insert(0, ".")  # noqa
import versioneer


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="git-workout",
    version=versioneer.get_version(),
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=[
        "Click ~= 7.0",
        "gitpython ~= 2.1.11",
        "arrow >= 0.12.1,< 0.16.0",
    ],
    python_requires=">=3.6",
    entry_points="""
        [console_scripts]
        git-workout=workout:main
    """,
    author="Mark Smith",
    author_email="judy@judy.co.uk",
    description="Prove that you only work on your own stuff out of hours.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/judy2k/git-workout",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    cmdclass=versioneer.get_cmdclass(),
)
