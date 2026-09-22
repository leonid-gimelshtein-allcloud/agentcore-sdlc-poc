# Node.js Express Health API

A minimal Node.js Express web API.

## Endpoints

| Method | Path            | Response                          |
| ------ | --------------- | --------------------------------- |
| GET    | `/health`       | `{"status": "healthy"}`           |
| GET    | `/hello/:name`  | `{"message": "Hello, <name>!"}`   |

## Requirements

- Node.js 18+

## Setup

Install the dependencies:

```bash
npm install
```

## Running

```bash
npm start
```

The app starts on <http://localhost:3001>.

## Try it

```bash
curl http://localhost:3001/health
# {"status":"healthy"}

curl http://localhost:3001/hello/world
# {"message":"Hello, world!"}
```
