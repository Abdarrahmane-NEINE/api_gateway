from app.config import settings

def resolve_service(request_path: str) -> str:
    # Simple mapping of URL prefixes to service URLs.
    service_mapping = {
        "/service1": {settings.SERVICE1_URL},
        "/service2": {settings.SERVICE2_URL},
    }
    
    for prefix, service_url in service_mapping.items():
        if request_path.startswith(prefix):
            return service_url
    
    # Return None if no service matches the given path.
    return None