# Flask Health Check API

A minimal Flask web API.

## Endpoints

| Method | Path           | Response                          |
| ------ | -------------- | --------------------------------- |
| GET    | `/health`      | `{"status": "healthy"}`           |
| GET    | `/hello/<name>`| `{"message": "Hello, <name>!"}`   |

## Requirements

- Python 3.8+

## Setup

Install the dependencies (a virtual environment is recommended):

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Running

```bash
python app.py
```

The app starts on <http://localhost:5000>.

## Try it

```bash
curl http://localhost:5000/health
# {"status": "healthy"}

curl http://localhost:5000/hello/world
# {"message": "Hello, world!"}
```
