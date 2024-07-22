import re

from unidecode import unidecode


def latin_slugify(text=None):
    if not text:
        return text
    # Convert Russian characters to Latin
    text = unidecode(text)
    # Convert to lowercase
    text = text.lower()
    # Remove non-alphanumeric characters
    text = re.sub(r'[^a-z0-9]+', '-', text)
    # Remove leading and trailing hyphens
    text = text.strip('-')
    return text

# Example usage
# text = "Пример текста на русском"
# slug = slugify(text)
# print(slug)
