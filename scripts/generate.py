"""Regenerate mcp.json and the per-actor sections of README.md from the public Apify Store.

Same catalog source as architek-earth/examples: the public store API for user `architekture`, deprecated actors skipped
(the store lists public actors only). One MCP server entry per live actor, each scoped to that actor with
`https://mcp.apify.com?tools=architekture/<slug>`. The token is never written: every entry reads it from the
APIFY_TOKEN environment variable. The script validates its own output (parses, no token, every live actor listed).
Usage: python scripts/generate.py
"""

import json
import pathlib
import re
import urllib.request

API = "https://api.apify.com/v2"
USER = "architekture"
MCP = "https://mcp.apify.com"
ROOT = pathlib.Path(__file__).resolve().parent.parent
CONFIG = ROOT / "mcp.json"
README = ROOT / "README.md"
START, END = "<!-- actors:start -->", "<!-- actors:end -->"
AUTH = "Bearer ${APIFY_TOKEN}"
TOKEN_RE = re.compile(r"apify_api_[A-Za-z0-9]{10,}|Bearer\s+(?!\$\{)[A-Za-z0-9_\-]{20,}")


def get(path: str) -> dict:
    req = urllib.request.Request(f"{API}/{path}", headers={"Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)["data"]


def live_actors() -> list[dict]:
    # Deprecated actors stay on Apify for existing users but get no server entry.
    items = get(f"store?username={USER}&limit=200")["items"]
    return sorted((a for a in items if not a.get("isDeprecated") and not get(f"acts/{USER}~{a['name']}").get("isDeprecated")),
                  key=lambda a: a["name"])


def title(a: dict) -> str:
    return re.split(r"\s+[—–-]\s+", a["title"], maxsplit=1)[0].strip()


def first_sentence(a: dict) -> str:
    text = " ".join((a.get("description") or "").split())
    return re.split(r"(?<=[.!?])\s", text, maxsplit=1)[0]


def price(a: dict) -> str:
    events = ((a.get("currentPricingInfo") or {}).get("pricingPerEvent") or {}).get("actorChargeEvents") or {}
    if not events:
        return "see the listing"
    primary = next((e for e in events.values() if e.get("isPrimaryEvent")), next(iter(events.values())))
    return f"${primary['eventPriceUsd'] * 1000:,.2f} per 1,000 · {(primary.get('eventTitle') or 'result').lower()}"


def server_url(slug: str) -> str:
    return f"{MCP}?tools={USER}/{slug}"


def entry(slug: str) -> dict:
    return {"type": "http", "url": server_url(slug), "headers": {"Authorization": AUTH}}


def config(slugs: list[str]) -> dict:
    return {"mcpServers": {f"{USER}-{s}": entry(s) for s in slugs}}


def section(a: dict) -> str:
    slug = a["name"]
    snippet = json.dumps({"mcpServers": {f"{USER}-{slug}": entry(slug)}}, indent=2)
    return f"""### {title(a)}

{first_sentence(a)}

Price: {price(a)}; status rows are free. Listing: [apify.com/{USER}/{slug}](https://apify.com/{USER}/{slug}).

Server URL: `{server_url(slug)}`

```json
{snippet}
```
"""


def validate(cfg_text: str, readme_text: str, slugs: list[str]) -> None:
    cfg = json.loads(cfg_text)
    servers = cfg["mcpServers"]
    missing = [s for s in slugs if f"{USER}-{s}" not in servers]
    if missing or len(servers) != len(slugs):
        raise SystemExit(f"mcp.json does not list exactly the live actors (missing: {missing})")
    for name, srv in servers.items():
        if srv["headers"]["Authorization"] != AUTH or not srv["url"].startswith(f"{MCP}?tools={USER}/"):
            raise SystemExit(f"unexpected entry {name}")
    for label, text in (("mcp.json", cfg_text), ("README.md", readme_text)):
        if TOKEN_RE.search(text):
            raise SystemExit(f"token-like string in {label}")
    for block in re.findall(r"```json\n(.*?)```", readme_text, flags=re.DOTALL):
        json.loads(block)


def main() -> None:
    actors = live_actors()
    slugs = [a["name"] for a in actors]
    cfg_text = json.dumps(config(slugs), indent=2) + "\n"
    text = README.read_text(encoding="utf-8")
    head, rest = text.split(START, 1)
    _, tail = rest.split(END, 1)
    count = f"**{len(slugs)} live actors.** Each one is its own server entry; copy only the ones you need.\n\n"
    body = count + "\n".join(section(a) for a in actors)
    readme_text = f"{head}{START}\n{body}{END}{tail}"
    validate(cfg_text, readme_text, slugs)
    CONFIG.write_text(cfg_text, encoding="utf-8", newline="\n")
    README.write_text(readme_text, encoding="utf-8", newline="\n")
    print(f"{len(slugs)} actors in mcp.json")


if __name__ == "__main__":
    main()
