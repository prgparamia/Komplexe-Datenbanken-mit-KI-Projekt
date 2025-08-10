# Installations
* fastapi
* uvicorn
* sqlalchemy
* pymysql
* pydantic

## Modell
* Question
    * id: auto_increment,pk
    * question_text: String
    
  
* Option
    * id: auto_increment,pk
    * question id:int
    * text:string
    * is_correct:bool 
 
 
# Project Structure

databank_project/
│
├── backend/
│   ├── dbconfig.py        # Database connection and configuration
│   ├── database.py        # DB session handling (possibly the `engine` and `Base`)
│   ├── models.py          # SQLAlchemy models (tables, columns, etc.)
│   ├── schemas.py         # Pydantic schemas for validation
│   ├── crud.py            # CRUD operations (queries)
│   ├── routers.py         # API route definitions (FastAPI routers)
│   ├── main.py            # Entry point for the app (starts the FastAPI server)
│   
│
└── frontend/
    ├── app.py             # Client
    |__ funcs.py       

* Smartquiz mit SQliteDB,PostgresqlDB und RestAPI,Client,Timer_Sidebar,Flower-Effect
* start  by main.py (uvicorn.run("main:app",host="127.0.0.1",port=8000,reload=True))
* RestAPI Test: Swagger -> http://127.0.0.1:8000/docs#
* Client/Frontend: Smartquiz_Frontend:app.py
* To Run Client:  python -m streamlit run app.py
    
    












# Make input like this

 {
  "question_text": "What is the capital of France?",
  "options": [
    {
      "text": "Paris",
      "is_correct": true
    },
    {
      "text": "London",
      "is_correct": false
    },
    {
      "text": "Berlin",
      "is_correct": false
    }
  ]
}