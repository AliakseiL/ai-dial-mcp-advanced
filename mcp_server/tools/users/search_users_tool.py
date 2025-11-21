from typing import Any

from mcp_server.tools.users.base import BaseUserServiceTool


class SearchUsersTool(BaseUserServiceTool):

    @property
    def name(self) -> str:
        # Provide tool name as `search_users`
        return "search_users"

    @property
    def description(self) -> str:
        # Short description of the tool
        return "Search users by optional filters: name, surname, email, gender"

    @property
    def input_schema(self) -> dict[str, Any]:
        # Provide tool params Schema: optional filters
        return {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "surname": {"type": "string"},
                "email": {"type": "string"},
                "gender": {"type": "string"},
            },
            "required": []
        }

    async def execute(self, arguments: dict[str, Any]) -> str:
        # Call user_client search_users (with `**arguments`) and return its results
        # Pass only keys that exist to avoid unexpected None handling
        params = {k: v for k, v in arguments.items() if v is not None}
        result = await self._user_client.search_users(
            name=params.get("name"),
            surname=params.get("surname"),
            email=params.get("email"),
            gender=params.get("gender"),
        )
        return result
