# django_blog_api

## Users

When you login to put the username not the email

| Username         | Password           |
| ---------------- | ------------------ |
| admin            |                    |
| alex             | Password123#       |
| marwa            | Password123#       |

###  Register

[register](http://localhost:8000/api/v1/auth/register/)

The **username** is required

```json
{
    "email": "alex@example.com",
    "username": "alex@example.com",
    "password1": "Password123#",
    "password2": "Password123#"

}
```

204 No Content

The **username** is required

## Login

```json
{
    "username": "alex@example.com",
    "password": "Password123#"
}
```

### Errors to handle

```json
{"username":["A user with that username already exists."],"email":["A user is already registered with this e-mail address."]}
```

```json
{
    "password1": [
        "This field is required."
    ],
    "password2": [
        "This field is required."
    ]
}
```

```json
{
    "password1": [
        "This password is too common."
    ]
}
```

## Schemas  

To generate the schema as a standalone file we can use a management command and specify the name of the file, which will be be schema.yml.

```bash
python manage.py spectacular --file schema.yml
```
