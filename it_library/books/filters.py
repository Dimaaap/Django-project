class ValuesFilter:

    def __call__(self, field: str, value):
        return {field: value}

