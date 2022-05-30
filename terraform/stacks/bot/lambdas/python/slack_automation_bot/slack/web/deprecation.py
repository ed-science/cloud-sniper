import os
import warnings

# https://api.slack.com/changelog/2020-01-deprecating-antecedents-to-the-conversations-api
deprecated_method_prefixes_2020_01 = [
    "channels.",
    "groups.",
    "im.",
    "mpim.",
    "admin.conversations.whitelist.",
]


def show_2020_01_deprecation(method_name: str):
    """Prints a warning if the given method is deprecated"""

    if skip_deprecation := os.environ.get("SLACKCLIENT_SKIP_DEPRECATION"):
        return
    if not method_name:
        return

    if matched_prefixes := [
        prefix
        for prefix in deprecated_method_prefixes_2020_01
        if method_name.startswith(prefix)
    ]:
        message = (
            f"{method_name} is deprecated. Please use the Conversations API instead. "
            "For more info, go to "
            "https://api.slack.com/changelog/2020-01-deprecating-antecedents-to-the-conversations-api"
        )
        warnings.warn(message)
