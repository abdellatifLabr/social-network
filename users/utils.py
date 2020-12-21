def build_user_image_path(user, filename):
    return f'users/user_{user.id}/image/{filename}'


def build_user_cover_path(user, filename):
    return f'users/user_{user.id}/cover/{filename}'
