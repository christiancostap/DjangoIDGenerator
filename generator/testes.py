import string
import secrets

length = 10

lettercase = 'mixed'

case = {
    'mixed': string.ascii_letters,
    'upper': string.ascii_uppercase,
    'lower': string.ascii_lowercase
}

characters = case.get(lettercase)

numbers = 'on'
if numbers == 'on':
    numbers = string.digits
print(''.join(secrets.choice(characters + numbers) for _ in range(length)))