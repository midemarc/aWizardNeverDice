# A Wizard Never Dice

## How to run
- Install requirements
- Start the server
```bash
export FLASK_APP=endpoints.py
export FLASK_ENV=development
flask run
```
- Connect using a http client:
    - Using `curl` :
        ```bash
        curl http://127.0.0.1:5000/roll_dice/element
        ```

    - Using `HTTPie` : 
        ```bash
        http :5000/roll_dice/element
        ```
