class PluginResponse:
    def __init__(self, result: str, source: str, is_error: bool = False):
        self.result = result
        self.is_error = is_error
        self.source = source

    def __str__(self):
        err_str = "ERROR" if self.is_error else "NORMAL"
        return f"[{self.source}] [{err_str}] {self.result}"
