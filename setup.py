from setuptools import setup, find_packages

setup(
    name="process-mining-ai-assistant",  # Название пакета
    version="0.1.0",  # Версия пакета
    author="Кирилл Лисенков",  # Ваше имя или имя команды
    author_email="lisenkov_kirill@mail.ru",  # Ваш email
    description="AI Assistant for Process Mining Research",  # Краткое описание проекта
    long_description=open("README.md").read(),  # Длинное описание из файла README.md
    long_description_content_type="text/markdown",  # Тип содержимого длинного описания
    url="https://github.com/lisenkovkv/process-mining-ai-assistant",  # URL репозитория проекта
    packages=find_packages(where="src"),  # Поиск и включение пакетов в папке src
    package_dir={"": "src"},  # Указание, что исходные коды находятся в папке src
    install_requires=[
        "pandas>=1.0.0",
        "numpy>=1.18.0",
        "scikit-learn>=0.22.0",
        # Добавьте другие зависимости, которые нужны вашему проекту
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',  # Минимальная версия Python
    entry_points={
        "console_scripts": [
            "process-mining-ai=src.cli:main",  # Например, добавление командной утилиты
        ],
    },
)