import setuptools

with open('README.md', 'r', encoding="utf-8") as f:
    description = f.read()

__version__= "0.0.1"

NAME_REPO = "FaceSystemRecognition-DeepFake"
AUTHOR_USERNAME="dona-eric"
SRC_REPO="Face_Recognition_System"
AUTHOR_EMAIL="donaerickoulodji@gmail.com"

setuptools.setup(
    name=NAME_REPO,
    version=__version__,
    author=AUTHOR_USERNAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for Computer Vision App",
    long_description=description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USERNAME}/{NAME_REPO}",
    license= "MIT",
    project_urls = {
        "bug_tracker":f"https://github.com/{AUTHOR_USERNAME}/{NAME_REPO}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)