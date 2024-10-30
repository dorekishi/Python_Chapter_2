def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_1 = build_profile(
    'miguel',
    'moreno',
    hobby = 'fashion',
    favorite_color = '6000FF',
    rap_name = 'dorekishi',
)

print(user_1)