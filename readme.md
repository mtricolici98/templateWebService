# Example Flask App Template with SQLAlchemy Database

## How to run

Run by executing the `main.py` file.

## How to add things

### New database entities (Models)

Create new classes for your new database entities inside the `models` package.

The new classes should extend `Base`

```python
class Example(Base):
    pass
```

### New api routes

Add new views or modify existing ones in the `api_views` package.

When you create a new module for your views, make sure to create a blueprint and register it inside the `main.py`.

See `example_blueprint.py` for reference.
