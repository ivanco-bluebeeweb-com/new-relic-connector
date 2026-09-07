"""Resource handlers for New Relic Connector."""
from __future__ import annotations
from typing import Any
from imperal_sdk import ActionResult
from app import chat
from schemas import (
    ListMetricParams, GetMetricParams,
    MetricRecord, MetricList, AuditHealthReport, ConnectionIdParams
)
from handlers_connection import resolve_client

@chat.function("list_metrics", "List metrics in New Relic.", action_type="read", chain_callable=True, event="new-relic-connector.list_metrics", effects=["read:metrics"], data_model=MetricList)
async def list_metrics(ctx, params: ListMetricParams) -> ActionResult:
    client = await resolve_client(ctx, params.connection_id)
    try:
        raw_items = await client.list_metrics(limit=params.limit)
        items = []
        for r in raw_items:
            rid = str(r.get("id") or r.get("key") or r.get("uuid") or "unknown")
            rname = r.get("name") or r.get("title") or r.get("label") or rid
            items.append({"id": rid, "name": rname, "status": r.get("status"), "created_at": r.get("createdAt") or r.get("created_at"), "raw": r})
        return ActionResult.success({"metrics": items, "total": len(items)}, summary=f"Found {len(items)} metrics.")
    except Exception as e:
        return ActionResult.error(f"Error listing metrics: {e}")

@chat.function("get_metric", "Get details of one Metric in New Relic.", action_type="read", chain_callable=True, event="new-relic-connector.get_metric", effects=["read:metric"], data_model=MetricRecord)
async def get_metric(ctx, params: GetMetricParams) -> ActionResult:
    client = await resolve_client(ctx, params.connection_id)
    try:
        r = await client.get_metric(params.metric_id)
        rid = str(r.get("id") or params.metric_id)
        rname = r.get("name") or r.get("title") or rid
        return ActionResult.success({"id": rid, "name": rname, "status": r.get("status"), "created_at": r.get("createdAt") or r.get("created_at"), "raw": r}, summary=f"Retrieved Metric {rid}.")
    except Exception as e:
        return ActionResult.error(f"Error retrieving Metric: {e}")

@chat.function("audit_metric_health", "Audit health of New Relic metrics and connectivity.", action_type="read", chain_callable=True, event="new-relic-connector.audit_metric_health", effects=["read:audit"], data_model=AuditHealthReport)
async def audit_metric_health(ctx, params: ConnectionIdParams) -> ActionResult:
    client = await resolve_client(ctx, params.connection_id)
    try:
        items = await client.list_metrics(limit=50)
        return ActionResult.success({
            "healthy": True,
            "total_metrics": len(items),
            "details": {"sample_count": len(items)},
            "summary": f"New Relic healthy. Sampled {len(items)} metrics."
        }, summary=f"New Relic health check passed with {len(items)} metrics.")
    except Exception as e:
        return ActionResult.error(f"Error auditing New Relic health: {e}")
