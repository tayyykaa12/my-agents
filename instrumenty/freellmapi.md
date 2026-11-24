# FreeLLMAPI в агентстве (установлено 24.11.2026)

Роутер бесплатных AI-API (github.com/tashfeenahmed/freellmapi, MIT). Используем для: картинок к креативам, озвучки Reels, черновиков текстов. Агенты агентства остаются на Claude.

## Запуск (контейнер сессии временный — повторять в новой сессии)
```bash
D=/tmp/freellmapi && git clone --depth 1 https://github.com/tashfeenahmed/freellmapi.git $D && cd $D && npm install
printf "ENCRYPTION_KEY=%s\nPORT=3001\n" "$(node -e 'console.log(require("crypto").randomBytes(32).toString("hex"))')" > .env
set -a; . ./.env; set +a; export NODE_USE_ENV_PROXY=1   # без этого каталог не скачивается через прокси
cd server && nohup npx tsx src/index.ts > ../server.log 2>&1 &
```
Первый вход: `POST /api/auth/setup` (локальный аккаунт), единый ключ — на странице Keys.

## Сеть
В окружении разрешён `api.freellmapi.co` (каталог моделей).

## Ключи провайдеров (бесплатные, вносит директор в настройках окружения → Network secrets)
| Сервис | Для чего | Host | Как |
|---|---|---|---|
| Google AI Studio | тексты, озвучка Gemini TTS (укр.) | generativelanguage.googleapis.com | заголовок `x-goog-api-key` |
| Cloudflare Workers AI | картинки FLUX / Leonardo | api.cloudflare.com | `Authorization: Bearer`; в роутер ключ как `account_id:token` |
В роутер вносится фиктивный ключ, настоящий подставляет прокси.

## Правила
- Тексты клиентов в бесплатные модели — только без персональных данных покупателей (бесплатные тарифы могут использовать данные для обучения).
- Картинки: проверять лицензию модели (FLUX schnell — Apache 2.0). Реальных людей (Богдан, клиенты) не генерировать; логотип и Щебіньчик — только оригинальные файлы.
- Цвета и шрифты креативов по-прежнему из брендбука.
