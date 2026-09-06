"""Extension declaration, capabilities, health check for New Relic Connector."""
from __future__ import annotations
import json
from imperal_sdk import ChatExtension, Extension

ext = Extension(
    "new-relic-connector",
    version="0.1.0",
    display_name="New Relic",
    icon="icon.svg",
    capabilities=["new_relic:manage"],
    description="Official Imperal connector for New Relic (C30. Email Marketing & Newsletter). Manage operations securely."
)

chat = ChatExtension(ext)

@ext.health_check
async def health_check(ctx) -> dict:
    raw = await ctx.secrets.get("new_relic_connections")
    try:
        count = len(json.loads(raw)) if raw else 0
    except Exception:
        count = 0
    return {
        "healthy": True,
        "detail": f"{count} New Relic connection(s) configured." if count else "Not connected yet."
    }
