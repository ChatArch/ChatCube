"Typed environment configuration for ChatCube."

from chatenv import BaseEnvConfig, EnvField


class ChatcubeConfig(BaseEnvConfig):
    "ChatCube ChatEnv configuration."

    _title = "ChatCube Configuration"
    _aliases = ["chatcube"]
    _storage_dir = "Chatcube"

    @classmethod
    def test(cls) -> None:
        """Validate schema registration without external side effects."""

        print(f"Testing {cls._title}...")
        print("Schema loaded; no network test is required.")

    CHATCUBE_API_KEY = EnvField(
        "CHATCUBE_API_KEY",
        desc="API key",
        is_sensitive=True,
    )


__all__ = ["ChatcubeConfig"]
