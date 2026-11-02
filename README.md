# freegpt.party

A minimal browser-based AI chat, based on [tinygrad's chat interface](https://github.com/tinygrad/tinygrad/blob/master/tinygrad/llm/chat.html).

## Use it

1. Open [freegpt.party](https://freegpt.party).
2. Choose a model from the dropdown.
3. Type a message and press **Enter** to send. Use **Shift+Enter** for a new line.
4. Wait for the response to finish before sending another message.

Refresh the page to start a new conversation. Chat history lives only in the page's memory and is lost on refresh.

By default, the app connects to `https://api.llm7.io` without an API key and selects `nemotron-3-nano:30b` if available. Available models, rate limits, and service availability depend on the API provider.

## Use another model or API server

Configure the app with URL fragment parameters (after `#`, not `?`):

| Parameter | Purpose |
| --- | --- |
| `server` | API base URL, without a trailing slash or `/v1`. |
| `model` | Model ID to select from the server's model list. |
| `api_key` | Optional API key, sent to the server as a Bearer token. |

For example, select a model:

```text
https://freegpt.party/#model=nemotron-3-nano%3A30b
```

Or connect to your own API (replace the example values):

```text
https://freegpt.party/#server=https%3A%2F%2Fapi.example.com&model=your-model&api_key=your-key
```

URL-encode parameter values, especially keys containing `&`, `+`, or `#`. Reload the page after changing parameters.

The server must support OpenAI-compatible `GET /v1/models` and streaming `POST /v1/chat/completions`. Requests go directly from your browser, so the server must allow cross-origin requests (CORS) from the site's origin, including any required headers. Use HTTPS when connecting from the hosted site.

## Privacy

- Your messages and conversation context are sent to the selected API provider. Its data retention and privacy policies apply.
- The site is a static frontend, not an API proxy. Markdown JavaScript is hosted alongside the page rather than fetched from a third-party CDN.
- URL fragments are not sent to the static hosting server, but keys in URLs can remain in browser history or be exposed when sharing links. Don't share URLs containing API keys; use restricted, disposable keys where possible.

## Run locally

Serve the `public/` directory with any static HTTP server, for example:

```sh
python3 -m http.server 8000 --directory public
```

Open `http://localhost:8000`. No build step is needed. Your API server must allow this origin too.

## Deploy

The repo is configured for Cloudflare Workers static assets in `wrangler.jsonc`.

```sh
npm ci
npx wrangler login
npx wrangler deploy
```

For Cloudflare Git-connected builds, leave the build command empty and use `npx wrangler deploy` as the deploy command. Everything under `public/` is published.
