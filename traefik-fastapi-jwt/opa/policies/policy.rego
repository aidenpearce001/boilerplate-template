package traefik-fastapi-jwt

default allow = false

# Public endpoint
allow {
    input.path == "/"
    input.method == "GET"
}

# API-1 access
allow {
    input.path == "/api-1"
    input.method == "GET"
    input.user.role == "api-1-users"
}

# API-2 access
allow {
    input.path == "/api-2"
    input.method == "GET"
    input.user.role == "api-2-users"
}
