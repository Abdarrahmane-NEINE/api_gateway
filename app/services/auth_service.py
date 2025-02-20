class AuthService:
    """
    Simulated AuthService for external authentication via an Identity Provider (IDP).
    This stub simulates token verification and introspection without using JWT decoding.
    """

    def __init__(self, public_key: str = None, algorithm: str = "RS256"):
        # For simulation purposes, these values are not used.
        self.public_key = public_key
        self.algorithm = algorithm

    def verify_token(self, token: str) -> dict:
        """
        Simulates token verification.
        Returns a dummy payload if the token is "valid-token", otherwise returns None.
        """
        if token == "valid-token":
            # Simulated payload from a valid token
            return {"sub": "test@example.com", "role": "user"}
        return None

    def introspect_token(self, token: str, introspection_url: str, client_id: str, client_secret: str) -> dict:
        """
        Simulates token introspection by returning a dummy response.
        """
        if token == "valid-token":
            return {"active": True, "sub": "test@example.com", "scope": "read write"}
        return {"active": False}
