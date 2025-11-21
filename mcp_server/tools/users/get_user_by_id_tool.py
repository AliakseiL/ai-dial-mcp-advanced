from typing import Any

from mcp_server.tools.users.base import BaseUserServiceTool


class GetUserByIdTool(BaseUserServiceTool):

    @property
    def name(self) -> str:
        # Provide tool name as `get_user_by_id`
        return "get_user_by_id"

    @property
    def description(self) -> str:
        # Short description of the tool
        return "Retrieve a user by their ID from the users management service"

    @property
    def input_schema(self) -> dict[str, Any]:
        # Provide tool params Schema. This tool applies user `id` (number) as a parameter and it is required
        return {
            "type": "object",
            "properties": {"id": {"type": "number"}},
            "required": ["id"],
        }

    async def execute(self, arguments: dict[str, Any]) -> str:
        # 1. Get int `id` from arguments
        user_id = int(arguments.get("id"))

        # 2. Call user_client get_user and return its results
        result = await self._user_client.get_user(user_id)
        return result
