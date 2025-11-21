from typing import Any

from mcp_server.models.user_info import UserCreate
from mcp_server.tools.users.base import BaseUserServiceTool


class CreateUserTool(BaseUserServiceTool):

    @property
    def name(self) -> str:
        # Provide tool name as `add_user`
        return "add_user"

    @property
    def description(self) -> str:
        # Short description of the tool
        return "Add a new user to the users management service"

    @property
    def input_schema(self) -> dict[str, Any]:
        # Provide tool params Schema using UserCreate pydantic model
        # Use the model JSON schema so the MCP can understand expected fields
        return UserCreate.model_json_schema()

    async def execute(self, arguments: dict[str, Any]) -> str:
        # 1. Validate arguments with `UserCreate.model_validate`
        user_create = UserCreate.model_validate(arguments)

        # 2. Call user_client add user and return its results (it is async, don't forget to await)
        result = await self._user_client.add_user(user_create)
        return result
