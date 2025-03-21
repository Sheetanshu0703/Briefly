import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Briefly"
AUTHOR_USER_NAME = "Sheetanshu0703"
SRC_REPO = "Briefly"
AUTHOR_EMAIL = "Sheetanshu0703@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for (NLP) Text Summarization app",
    long_description=long_description,  # ✅ Fixed capitalization
    long_description_content_type="text/markdown",  # ✅ Fixed argument name
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},  # ✅ Fixed package_dir format
    packages=setuptools.find_packages(where="src"),
)
