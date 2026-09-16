import json
import os
import sys

# Add project root directory to sys.path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from utils.encryption import get_or_create_key, encrypt_password

TEST_DATA_DIR = os.path.join(PROJECT_ROOT, "test_data")
os.makedirs(TEST_DATA_DIR, exist_ok=True)

CREDENTIALS_FILE = os.path.join(TEST_DATA_DIR, "credentials.json")
TEMPLATE_FILE = os.path.join(TEST_DATA_DIR, "credentials.template.json")



def create_credentials_json(
    test_email: str = "testuser@gmail.com",
    test_password: str = "Password1!",
    existing_email: str = "existinguser@gmail.com",
):
    """Encrypt password and save credentials JSON file along with a template file."""
    key = get_or_create_key()
    encrypted_pw = encrypt_password(test_password, key)

    credentials_data = {
        "test_email": test_email,
        "encrypted_password": encrypted_pw,
        "existing_email": existing_email,
    }

    with open(CREDENTIALS_FILE, "w", encoding="utf-8") as f:
        json.dump(credentials_data, f, indent=2)

    template_data = {
        "test_email": "user@example.com",
        "encrypted_password": "<ENCRYPTED_FERNET_PASSWORD_TOKEN>",
        "existing_email": "existing_user@example.com",
    }
    with open(TEMPLATE_FILE, "w", encoding="utf-8") as f:
        json.dump(template_data, f, indent=2)

    print("Secret key generated/validated.")
    print(f"Successfully generated encrypted credentials file: {CREDENTIALS_FILE}")
    print(f"Created template credentials file: {TEMPLATE_FILE}")


if __name__ == "__main__":
    create_credentials_json()
