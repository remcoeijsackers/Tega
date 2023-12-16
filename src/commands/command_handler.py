from src.commands.request_handler import flaskAccountHandler


CliAccountHandler = flaskAccountHandler.update_defined_arg(
    key="mail",
    value={
        "default": "clean",
        "supported": ["c", "f", "d", "clean", "fake", "disposable"]
        }
    )
