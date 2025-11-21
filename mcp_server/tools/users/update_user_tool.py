from typing import Any

from mcp_server.models.user_info import UserUpdate
from mcp_server.tools.users.base import BaseUserServiceTool


class UpdateUserTool(BaseUserServiceTool):

    @property
    def name(self) -> str:
        # Provide tool name as `update_user`
        return "update_user"

    @property
    def description(self) -> str:
        # Short description of the tool
        return "Update an existing user's information by ID"

    @property
    def input_schema(self) -> dict[str, Any]:
        # Provide tool params Schema: id required and new_info schema
        return {
            "type": "object",
            "properties": {
                "id": {"type": "number"},
                "new_info": UserUpdate.model_json_schema(),
            },
            "required": ["id", "new_info"],
        }

    async def execute(self, arguments: dict[str, Any]) -> str:
        # 1. Get user `id` from `arguments`
        user_id = int(arguments.get("id"))

        # 2. Get `new_info` from `arguments` and create `UserUpdate` via pydantic `UserUpdate.model_validate`
        new_info_raw = arguments.get("new_info", {})
        user_update = UserUpdate.model_validate(new_info_raw)

        # 3. Call user_client update_user and return its results
        result = await self._user_client.update_user(user_id, user_update)
        return result
