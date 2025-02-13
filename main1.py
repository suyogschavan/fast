# # from fastapi import FastAPI
# # from typing import Optional
# # from pydantic import BaseModel
# # from pymongo import MongoClient
# # from pymongo.server_api import ServerApi
# # from dotenv import load_dotenv
# # from enum import Enum
# # from datetime import datetime
# # from bson import json_util
# # import json
# # def parseData(data): return json.loads(json_util.dumps(data))
# # import os
# # load_dotenv()

# # app = FastAPI()
# # uri = os.getenv("MONGO_URI")

# # db_conn = MongoClient(uri,server_api=ServerApi('1'))

# # database = db_conn["fastAPIproject"]

# # try:
# #     database.create_collection("user")
# # except:
# #     print("user collection aleady exists")

# # collection = database["user"]
# # @app.get('/')
# # def landing():
# #     return {"data":"Yo world"}

# # @app.get('/checkdb')
# # def checkconnection():
# #     return []
    
# # class User(BaseModel):
# #     admin:bool = False
# #     username:str
# #     joinedAt:str  = str(datetime.now())
# #     following : list[str] | None    #contain usernames
# #     followers : list[str] | None
# #     password : str
# #     bio:str | None
    
# # # Crud operation
# # @app.post('/newUser')
# # def newUser(user:User):
# #     collection.insert_one(dict(user))
# #     result = collection.find_one({"username":user.username})
# #     # print(type(result))
# #     # result['_id'] = str(result['_id'])
# #     data = parseData(result)
# #     return {"count":collection.count_documents({}), "inserted":data}

# # @app.get('/allusers')
# # def getAllUsers():
# #     result = collection.find({})
# #     data = []
# #     for i in result:
# #         i['_id'] = str(i['_id'])
# #         data.append(i)
# #     return data


# # # @app.get('/')
# # # def index():
# # #     return {
# # #             'data': {'name':'Suyog'}}
    
# # # @app.get('/blog/unpublished')
# # # def uppublished():
# # #     return {}

# # # @app.get('/blog/{id}')
# # # def about(id:int):
# # #     return {'data': {'name': 'Suyog', 'page':'About', 'id':id}}

# # # @app.get('/blogs')
# # # def getAllBlogs(published:bool = True, limit=10, sort:str | None = None):
# # #     if published:
# # #         return {"data":f"{limit} published blogs from database", "sorting":sort}
# # #     else: return {"data": f"{limit} blogs from database"}
    
    
# # # class for body params 
# # # class Blog(BaseModel):
# # #     title:str
# # #     body:str
# # #     published: Optional[bool] = False


# # # @app.post('/blog')
# # # def postBlog(blogInfo:Blog):
# # #     return {"data":f"Blog name: {blogInfo.title} inserted into database"}


# from fastapi import FastAPI
# from 
