# FastAPI & React Application

## How to Run the App

### Backend (FastAPI)

1. Open the terminal and navigate to the **FastAPI** directory:
   ```bash
   cd FastAPI
   pip install annotated-types==0.6.0
   pip install anyio==4.3.0
   pip install click==8.1.7
   pip install fastapi==0.110.0
   pip install h11==0.14.0
   pip install idna==3.6
   pip install pydantic==2.6.4
   pip install pydantic_core==2.16.3
   pip install sniffio==1.3.1
   pip install SQLAlchemy==2.0.29
   pip install starlette==0.36.3
   pip install typing_extensions==4.10.0
   pip install uvicorn==0.29.0

2. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload


### Frontend (React)

1. Open a new terminal (keeping the FastAPI terminal running) and navigate to the **React/finance-app** directory:
   ```bash
   cd React/finance-app
   npm install
   npm start