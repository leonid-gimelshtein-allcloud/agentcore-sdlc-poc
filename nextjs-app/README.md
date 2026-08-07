# Next.js Hello World Application

A minimal Next.js web application using the App Router.

## Endpoints

| Method | Path           | Response                          |
| ------ | -------------- | --------------------------------- |
| GET    | `/`            | Hello, World! page                |
| GET    | `/api/health`  | `{"status": "ok"}`                |

## Requirements

- Node.js 18.17+
- npm

## Setup

Install the dependencies:

```bash
npm install
```

## Running

### Development Mode

```bash
npm run dev
```

The app starts on <http://localhost:3000>.

To use a custom port, set the PORT environment variable:

```bash
PORT=4000 npm run dev
```

### Production Mode

Build the application:

```bash
npm run build
```

Start the production server:

```bash
npm start
```

## Try it

```bash
# Visit the home page
curl http://localhost:3000/
# Returns HTML with "Hello, World!"

# Check the health endpoint
curl http://localhost:3000/api/health
# {"status":"ok"}
```
