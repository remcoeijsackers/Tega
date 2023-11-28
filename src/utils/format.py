
def remove_null(value: dict):
    return {k: v for k, v in value.items() if v}