def registr():
    """Возвращает заглавные буквы..."""
    word = input().upper()
    return word

def registr_title():
    """Возвращает заглавные первые буквы каждого слова в строке"""
    word = input().title()
    return word


print(registr())
print(registr_title())