import hashlib

def hash_email(email: str) -> str:
    cleaned = email.strip().lower()
    encoded = cleaned.encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()