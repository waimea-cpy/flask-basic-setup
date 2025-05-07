# Flask Basic Setup

This is template for a simple [Flask](https://flask.palletsprojects.com) application. It includes config for deployment to [Railway.app](https://railway.app/)

## What is Flask?

Flask is a **web back-end framework**. It uses the **Python** programming language and provides features such as:

- Handling **HTTP requests**:
    - **GET** (to read data)
    - **POST** (to create new data)
    - **PUT** (to update existing data)
    - **DELETE** (to remove data)
- **URL routing**, allowing the use of simple and meaningful URLs
- Serving of **static files** (e.g. CSS, images, etc.)
- **Templating** via [Jinja2](https://jinja.palletsprojects.com/templates/)

## Features of this Setup

This repo provides a simple Flask app that includes:

- A simple way to serve up basic HTML pages
- A simple routing system
- A simple templating system for pages

## Setting up a Development Environment

To develop locally, you need to setup a **Python virtual enviroment (venv)** to keep your Python configuration isolated from the rest of your system.


### Create the Virtual Environment

1. In your terminal, navigate to the project root folder

2. **Create** the virtual environment with:

    ```
    python -m venv venv
    ```

2. **Activate** the virtual environment

    *Note: If using VS Code's terminal, VS Code will offer to use / activate the virtual environment for you - select Yes*

    Windows PowerShell:

    ```
    .\venv\Scripts\activate
    ```

    Linux:

    ```
    source venv/bin/activate
    ```

3. **Install** all required Python libraries:

    ```
    pip install -r requirements.txt
    ```

### Using a Previously Created Virtual Environment

If you are returning to your project, you do not need to recreate your virtual environment, just activate and update it.

*Note: If using VS Code as mentioned above, VS Code will automatically activate the environment as time you open its Terminal*


## Launching the Server

The Flask project is configured as a module called **app** (with main code in **\_\_init__.py**), which allows the the server to be run very easily with:

```
flask run
```

Or to get full debug info:

```
flask run --debug
```

## Deploying to Railway

Deploying to Railway from this repo with no additional tweaking should 'just work'. Once setup, every time you push changes to your repo, the deployed app will be updated.

### Railway Setup

1. Go to [railway.app](railway.app) and **Sign in with GitHub**

2. Create a new project

3. Link to your GH repo.

4. In the Railway project settings:

    - **Build**
        - Check that *Builder* is **DockerFile** (should be auto-detected)

    - **Deploy**
        - Set a *Custom Start Command*:

            ```
            flask run --host=0.0.0.0
            ```

    - **Networking**
        - Select *Generate a Domain* and make sure port is set to **5000** (should be auto-set)

