def string_smaller(title,length=50):
    if len(title) >= length:
        return title[:length] + "..."
    return title