import string
from fastapi import FastAPI
import secrets

app = FastAPI()


@app.get("/")
async def generate_password(max_length: int = 12, number_of_digits: int = 2) -> str:
    """
    This function will generate random password according to params
    :param max_length: maximum length of the password
    :param number_of_digits: number of digits required in the password
    :return: (str) the generated password.
    """

    if number_of_digits > max_length:
        raise Exception(
            "Error while generating password: Number of digits must be less than maximum length of the password"
        )

    excluded_chars = {"+", "-", "?", "`", "#", "/", "|", "@", '"', ";", ",", "*", "!", "<"}
    letters = string.ascii_letters
    digits = string.digits
    special_chars = ''.join([val for val in set(string.punctuation) - excluded_chars])
    alphabet = letters + digits + special_chars

    while True:
        passwd = ""
        for i in range(max_length):
            passwd += "".join(secrets.choice(alphabet))
        if any(char in special_chars for char in passwd) and sum(char in digits for char in passwd) == number_of_digits:
            break
    return passwd