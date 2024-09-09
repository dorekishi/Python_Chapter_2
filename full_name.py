#
first_name='ada'
last_name='lovelace'
full_name=f'{first_name} {last_name}'
print(full_name)
#
print(f'Hello, {full_name.title()}!')
#
message=f'Hello, {full_name.title()}!'
print(message)
#
print('python')
print('\tpython')
#
print('languages:\npython\nc\njavascript')
#
print('languages:\n\tpython\n\tc\n\tjavascript')
#
favorite_language='python '
print(favorite_language)
print(favorite_language.rstrip())
print(favorite_language)
#
favorite_language='python'
favorite_language=favorite_language.rstrip()
print(favorite_language)
 #
favorite_language=' python '
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())
#
nostarch_url='https://nostarch.com'
print(nostarch_url.removeprefix('https://'))
#
simple_url=nostarch_url.removeprefix('https://')
print(simple_url)
