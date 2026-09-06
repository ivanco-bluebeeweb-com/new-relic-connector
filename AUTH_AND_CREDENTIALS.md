# New Relic Connector — Auth & Credentials Standard

**Compliance:** AUTH_AND_CREDENTIALS_STANDARD.md (B1–B10)

## Схема аутентификации
- **Метод:** User API Key (NRAK) / GraphQL NerdGraph API
- **Хранение:** Секреты сохраняются изолированно в хранилище секретов платформы Imperal.
- **Валидация:** При сохранении ключа выполняется тестовый запрос `GET /v2/applications.json`.
- **Отключение:** Удаление локальных ключей без воздействия на аккаунт вендора.
