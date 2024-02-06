# BookMyShow FastAPI Project

## Overview

This project is a demonstration of building a backend for a ticket booking application using FastAPI, a modern, fast (high-performance), web framework for building APIs with Python 3.7+.

## Directory Structure

bookmyshow/
│
├── .env/ # Directory for environment variables
├── app/ # Main application directory
│ ├── api/ # API routers and handlers
│ ├── dependencies/ # Dependencies for the project
│ ├── models/ # Database models
│ ├── repo/ # Data access layer
│ ├── schemas/ # Pydantic schemas for data validation
│ ├── settings.py # Application settings
│ ├── init.py
│ └── main.py # Main FastAPI application entry point
│
├── .gitignore # Git ignore file
├── LICENSE # License file
├── README.md # This README file
└── bookmyshow - public.png # BookMyShow logo

## Schema Design

![Schema Design](../bookmyshow/bookmyshow%20-%20public.png)

## Setup and Installation

1. **Clone the repository:**
```
git clone 
```


2. **Activate the virtual environment:**
- On Windows:
  ```
  venv\Scripts\activate
  ```
- On macOS and Linux:
  ```
  source venv/bin/activate
  ```

3. **Install dependencies:**
```
pip3 install requirements.txt
```

4. **Set up environment variables:**
- Create a `.env` file in the root directory.
- Add necessary environment variables.

5. **Run the application:**
```
uvicorn app.main:app --reload
```

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).