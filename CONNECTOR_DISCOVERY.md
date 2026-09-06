# New Relic Connector — Connector Discovery

**Vendor API Baseline:** https://newrelic.com

## Архитектура API
- **Базовый адрес:** `https://api.newrelic.com/v2`
- **Протокол:** REST / HTTPS (JSON)
- **Аутентификация:** User API Key (NRAK) / GraphQL NerdGraph API
- **Ключевые эндпоинты:**
  - приложения APM (/applications.json)
  - алерты (/alerts_policies.json)
  - NerdGraph запросы (/graphql)
  - метрики серверов
- **Тестовая точка проверки подключения:** `GET /v2/applications.json`.
