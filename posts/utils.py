def post_files_upload_path(section, filename):
    return f'posts/post_{section.post.id}/{section.order}_{filename}'
