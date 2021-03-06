# Navedex API

API para gerenciamento de Navers e Projetos

## Como desenvolver?

1. Clone do  repositório.
2. Crie um virtualenv com Python 3
3. Ative o virtualenv.
4. Instale as dependências.
5. Execute os testes.
6. Execute as migrations
7. Execute a aplicação

```console
git clone #
cd navedex_api
python3 -m venv .env
source .env/bin/activate
pip install -r requirements.txt
python manage.py test
python manage.py migrate
python manage.py runserver
```


**Documentação da API**
----

OBS.:
	Através do software Insomnia, o arquivo `navedex_api_requests.json` pode ser importado e o ambiente
	para testes estará configurado, de forma que todas as rotas da API estarão disponíveis.
	Para as rotas que não são de autenticação, o token de acesso está pré-configurado nas preferências do ambiente,
	de forma que ele atualiza sempre com a rota de login.
	Nas preferências do ambiente também está configurada a base URL para ser usada em todas as rotas, e caso necessário,
	alterá-la, automaticamente configura todo o ambiente

**Signup**
----
  Cria usuário para fazer uso da API

* **URL**

  /signup

* **Method:**

  `POST`

* **Data Params**

  `{email: "test@test.com", password: "123$#45"}`

* **Success Response:**

  * **Code:** 201 CREATED <br />
    **Content:** `{email: test@test.com, password: hash}`
 
* **Error Response:**

  * **Code:** 400 BAD REQUEST <br />
    **Content:** `{ error : {email:["User with this email already exists."]}, }`

  OR

  * **Code:** 400 BAD REQUEST <br />
    **Content:** `{ error : {<field>:["This field cannot be empty."]}, }`


**Login**
----
  Gera o token de acesso à api

* **URL**

  /login

* **Method:**

  `POST`

* **Data Params**

  ```{email: "test@test.com", password: "123$#45"}```

* **Success Response:**

  * **Code:** 200 OK <br />
    **Content:** `{refresh: <refresh_token>, access: <access_token>}`
 
* **Error Response:**

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `{ error : {"detail": "No active account found with the given credentials"} }`

  OU

  * **Code:** 400 BAD REQUEST <br />
    **Content:** `{ error : {<field>:["This field cannot be empty."]}, }`


**Project Index**
----
  Lista os projects

* **URL**

  /project

* **Method:**

  `GET`

*  **URL Params**

   **Optional:**
 
   `name=[str]`

* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 OK <br />
    **Content:** `
    ```
    [
      {
        "id": 1,
        "name": "Projeto Teste",
        "navers": [
		  {
		    "id": 1,
		    "name": "Gustavo",
		    "birthdate": "1997-02-15",
		    "job_role": "Node Developer",
		    "admission_date": "2019-07-25"
		  },
		  {
		    "id": 2,
		    "name": "Marcos",
		    "birthdate": "1997-02-15",
		    "job_role": "Django Developer",
		    "admission_date": "2020-07-23"
		  }
        ]
      },
      {
        "id": 2,
        "name": "Projeto Teste 02",
        "navers": [
		  {
		    "id": 1,
		    "name": "Gustavo",
		    "birthdate": "1997-02-15",
		    "job_role": "Node Developer",
		    "admission_date": "2019-07-25"
		  }
        ]
      }
    ]
 
* **Error Response:**

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `{ error :{"detail": "Authentication credentials were not provided."}}`


**Show Project**
----
  Retorna os dados de um project.

* **URL**

  /project/:id

* **Method:**

  `GET`
  
*  **URL Params**

   **Required:**
 
   `id=[integer]`

* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:**
    ```
    {
      "id": 1,
      "name": "Projeto Teste",
      "navers": [
		{
		  "id": 1,
		  "name": "Gustavo",
		  "birthdate": "1997-02-15",
		  "job_role": "Node Developer",
		  "admission_date": "2019-07-25"
		}
     ]
    }
    
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{ error : "Project doesn't exist" }`

  OU

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `{ error :{"detail": "Authentication credentials were not provided."}}`


**Store Project**
----
  Cria um projeto.

* **URL**

  /project/

* **Method:**

  `POST`
  
*  **URL Params**
  None

* **Data Params**

  `{"name": "Projeto Teste", "navers": [1]}`

* **Success Response:**

  * **Code:** 201 CREATED <br />
    **Content:**
    ```
    {
    "id": 1,
    "name": "Projeto Teste",
    "navers": [
	    {
	      "id": 1,
	      "name": "Gustavo",
	      "birthdate": "1997-01-15",
	      "job_role": "Django Developer",
	      "admission_date": "2020-08-25"
	    }
    	]
    }
 
* **Error Response:**

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `{ error :{"detail": "Authentication credentials were not provided."}}`
  
  OU

  * **Code:** 400 BAD REQUEST <br />
    **Content:** `{ error : {<field>:["This field cannot be empty."]}, }`


**Update Navers**
----
  Atualiza um projeto.

* **URL**

  /project/

* **Method:**

  `PUT`
  
*  **URL Params**
  None

* **Data Params**

  `{"name": "Projeto Teste", "navers": [1]}`

* **Success Response:**

  * **Code:** 200 OK <br />
    **Content:**
    ```{
      "id": 1,
      "name": "Gustavo",
      "birthdate": "1997-01-15"
      "job_role": "Django Developer",
      "admission_date": "2020-08-25",
      "projects": [
		{
		  "id": 1,
		  "name": "Projeto Teste"
		},
		{
		  "id": 2,
		  "name": "Projeto Teste 02"
		}
      ]
    }
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{ error : "Project doesn't exist" }`

  OU

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `{ error :{"detail": "Authentication credentials were not provided."}}`

  OU

  * **Code:** 400 BAD REQUEST <br />
    **Content:** `{ error : {<field>:["This field cannot be empty."]}, }`


**Delete Project**
----
  Exclui um projeto.

* **URL**

  /project/:id

* **Method:**

  `DELETE`
  
*  **URL Params**

   **Required:**
 
   `id=[integer]`

* **Data Params**

  None

* **Success Response:**

  * **Code:** 204 NO CONTENT<br />
    **Content:** None
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{ error : "Project doesn't exist" }`

  OU

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `
    `{ error :{"detail": "Authentication credentials were not provided."}}`


**Naver Index**
----
  Lista os navers

* **URL**

  /naver

* **Method:**

  `GET`

*  **URL Params**

   **Optional:**
 
   `name=[str]`
   `job_role=[str]`
   `admission_date=[date]`

* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 OK <br />
    **Content:** `
    ```[
      {
        "id": 1,
        "name": "Gustavo",
        "birthdate": "1997-01-15",
        "job_role": "Django Developer",
        "admission_date": "2020-08-25",
        "projects": [
		  {
		    "id": 1,
		    "name": "Projeto Teste"
		  }
        ]
        },
        {
          "id": 2,
          "name": "Marcos",
          "birthdate": "1997-02-08",
          "job_role": "Node Developer",
          "admission_date": "2020-07-30",
          "projects": [
		    {
		      "id": 1,
		      "name": "Projeto Teste"
		    }
          ]
        }
      ]
 
* **Error Response:**

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `{ error :{"detail": "AAuthentication credentials were not provided."}}`


**Show Navers**
----
  Retorna os dados de um naver.

* **URL**

  /naver/:id

* **Method:**

  `GET`
  
*  **URL Params**

   **Required:**
 
   `id=[integer]`

* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:**
    ```{
      "id": 1,
      "name": "Gustavo",
      "birthdate": "1997-01-15",
      "job_role": "Django Developer",
      "admission_date": "2020-08-25",
      "projects":
      [
        {
          "id": 1,
          "name": "Projeto Teste"
        }
      ]
    }
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{ error : "Naver doesn't exist" }`

  OU

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `{ error :{"detail": "Authentication credentials were not provided."}}`


**Store Navers**
----
  Cria um naver.

* **URL**

  /naver/

* **Method:**

  `POST`
  
*  **URL Params**
  None

* **Data Params**

  ```{
	  "name": "Gustavp",
	  "birthdate": "1997-1-15",
	  "job_role": "Django Developer",
	  "admission_date"	: "2020-8-25",
	  "projects": [1]
  }

* **Success Response:**

  * **Code:** 201 CREATED <br />
    **Content:**
    ```{
      "id": 1,
      "name": "Gustavo",
      "birthdate": "1997-01-15"
      "job_role": "Django Developer",
      "admission_date": "2020-08-25",
      "projects": [
        {
          "id": 1,
          "name": "Projeto Teste"
        }
      ]
    }
 
* **Error Response:**

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `{ error :{"detail": "Authentication credentials were not provided."}}`
  
  OU

  * **Code:** 400 BAD REQUEST <br />
    **Content:** `{ error : {<field>:["This field cannot be empty."]}, }`

**Update Navers**
----
  Atualiza um naver.

* **URL**

  /naver/

* **Method:**

  `PUT`
  
*  **URL Params**
  None

* **Data Params**

  ```{
	  "name": "Gustavo",
	  "birthdate": "1997-1-15",
	  "job_role": "Django Developer",
	  "admission_date"	: "2020-8-25",
	  "projects": [1, 2]
  }

* **Success Response:**

  * **Code:** 200 OK <br />
    **Content:**
    ```{
      "id": 1,
      "name": "Gustavo",
      "birthdate": "1997-01-15"
      "job_role": "Django Developer",
      "admission_date": "2020-08-25",
      "projects": [
        {
          "id": 1,
          "name": "Projeto Teste"
        },
        {
          "id": 2,
          "name": "Projeto Teste 02"
        }
      ]
    }
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{ error : "Naver doesn't exist" }`

  OU

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `{ error :{"detail": "Authentication credentials were not provided."}}`

  OU

  * **Code:** 400 BAD REQUEST <br />
    **Content:** `{ error : {<field>:["This field cannot be empty."]}, }`


**Delete Navers**
----
  Exclui um naver.

* **URL**

  /naver/:id

* **Method:**

  `DELETE`
  
*  **URL Params**

   **Required:**
 
   `id=[integer]`

* **Data Params**

  None

* **Success Response:**

  * **Code:** 204 NO CONTENT<br />
    **Content:** None
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{ error : "Naver doesn't exist" }`

  OU

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `{ error :{"detail": "Authentication credentials were not provided."}}`
