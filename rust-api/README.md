# Rust API Service

A minimal Rust web API using Actix-web.

## Endpoints

| Method | Path           | Response                    |
| ------ | -------------- | --------------------------- |
| GET    | `/`            | `Hello, World!`             |
| GET    | `/hello/<name>`| `Hello, <name>!`            |

## Requirements

- Rust 1.70+ and Cargo

## Build

```bash
cargo build
```

## Running

```bash
cargo run
```

The app starts on <http://localhost:8080>.

## Try it

```bash
curl http://localhost:8080/
# Hello, World!

curl http://localhost:8080/hello/world
# Hello, world!
```
