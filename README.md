# Add websocket to Django without extra dependency

## Motivation

[Django Channels](https://channels.readthedocs.io/en/stable/) is very large.
It dependence on `cryptography` which depends on Rust compiler(https://cryptography.io/en/latest/faq/#why-does-cryptography-require-rust) ...

I found a simple solution from https://jaydenwindle.com/writing/django-websockets-zero-dependencies/
