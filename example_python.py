import os

API_KEY = os.environ.get("API_KEY")
SECRET_TOKEN = os.environ.get("SECRET_TOKEN")


def print_secrets():
    print(f"API_KEY: {API_KEY}")
    print(f"SECRET_TOKEN: {SECRET_TOKEN}")


if __name__ == "__main__":
    print_secrets()
    print("This line has a syntax error")
