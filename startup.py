from werkzeug.routing import Map, Rule

# Configure application middleware and services


class startup:
    def configure_services():
        return "Implement"

    def configure_middleware():
        return "Implement"

    def configure_domains():
        return Map([
            Rule('/', endpoint='index')
        ])