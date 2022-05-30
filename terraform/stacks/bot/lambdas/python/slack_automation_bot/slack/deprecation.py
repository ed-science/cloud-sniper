import os
import warnings


def show_message(old: str, new: str) -> None:
    if skip_deprecation := os.environ.get("SLACKCLIENT_SKIP_DEPRECATION"):
        return

    message = (
        f"{old} package is deprecated. Please use {new} package instead. "
        "For more info, go to https://slack.dev/python-slack-sdk/v3-migration/"
    )
    warnings.warn(message)
