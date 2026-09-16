# Test & Verification Ledger — New Relic Connector

**App ID:** `new-relic-connector`  
**Last Updated:** 2026-09-16  
**Registration Target:** https://one.newrelic.com  
**Auth Mechanism:** User API Key (NRAK-)  
**Core Domain Scope:** Observability: metrics, entities, alerts  

---

## 1. Test History & Stage Breakdown

| Date | Verification Stage | Method | Result | Evidence / Details |
|---|---|---|---|---|
| 2026-08-31 | Platform Contract Audit | Static Parser | ✅ Passed | Fixed ActionResult/Entity signatures, secrets declared |
| 2026-09-15 | PST D-Layer Verification | D1-D4 Standard | ✅ Passed | Zero secret leak, strict typing, schema alignment |
| Pending | Live Screen/GUI Registration | OS Mouse/Keyboard (cliclick/Chrome) | ⏳ Ready | Awaiting account signup & API token issuance |
| Pending | Live Provider CRUD E2E | Vendor API + ctx.store | ⏳ Ready | Awaiting Live Token |

---

## 2. Capability Matrix & Tools Audited (6 tools)

- `connect_new_relic_connector`: contract validated (PST ready)
- `list_connections`: contract validated (PST ready)
- `disconnect_new_relic_connector`: contract validated (PST ready)
- `list_metrics`: contract validated (PST ready)
- `get_metric`: contract validated (PST ready)
- `audit_metric_health`: contract validated (PST ready)

---

## 3. Screen / Browser Test Execution Protocol (For Next Session)
1. Launch Chrome directly to `https://one.newrelic.com`.
2. Complete signup / OAuth via `vlad@bluebeeweb.com`.
3. Extract `User API Key (NRAK-)` via GUI navigation.
4. Call `connect_new_relic_connector` in Imperal OS panel.
5. Run live create/read/delete verification cycle with Zero Residue.
