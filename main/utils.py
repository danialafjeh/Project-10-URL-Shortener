import random
import string
from .models import ShortURL

def generate_short_code():
    characters = string.ascii_letters + string.digits
    while True:
        short_code = "".join(
            random.choice(characters)
            for _ in range(8)
        )

        if not ShortURL.objects.filter(short_code=short_code).exists():
            return short_code
        