# FastAPI tutorial

Code for my video tutorial [FastAPI tutorial](https://youtu.be/GRD3z95vs-A)

## What is FastAPI?

FastAPI is a high-performant REST API framework for Python. It's built on top of 
[Starlette](https://www.starlette.io/) and it uses [Pydantic](https://pydantic-docs.helpmanual.io/) 
for data validation. It can generate OpenAPI documentation from your code and also produces 
a Swagger UI that you can use to test your application.

Check out FastAPI's GitHub [repository](https://github.com/tiangolo/fastapi) and give it a 
star! Also make sure to check out its excellent [documentation](https://fastapi.tiangolo.com/) online.

## What is JWT authorization?

JWT stands for JSON Web Token and it's the standard way to add authorization to an API. Notice that we say 
authorization and not authentication: JWT tokens are used to authorize access to an API. JWTs are not used 
for authentication. Authentication is the process of verifying a user identity, and as part of this process 
we issue a JWT token.

If you don't know what JWTs are and how they work, take a look at my tutorial "Working with JWTs in Python" 
(https://youtu.be/VRn8cPc7B_w).
