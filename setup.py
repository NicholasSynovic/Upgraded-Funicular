from setuptools import setup

from writing_prompt_collector import version

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="writing-prompt-collector",
    packages=["writing_prompt_collector"],
    version=version.version(),
    description="writing-prompt-collector: Collect and store writing prompts from Reddit subreddits",
    author="Nicholas M. Synovic",
    author_email="nicholas.synovic@gmail.com",
    license="GNU Affero General Public License v3.0",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    project_urls={
        "Bug Tracker": "https://github.com/NicholasSynovic/wpc/issues",
        "GitHub Repository": "https://github.com/NicholasSynovic/wpc",
    },
    keywords=[
        "writing",
        "reddit"
    ],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
    ],
    python_requires=">=3.9",
    install_requires=[
        "pandas",
        "praw",
        "progress",
    ],
    entry_points={
        "console_scripts": [
            "wpc = writing_prompt_collector.main:main",
        ]
    },
)
