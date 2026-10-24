# architek.earth MCP servers

Every live [architek.earth](https://github.com/architek-earth) actor as a ready-to-paste MCP server entry, so an AI agent
(Claude, Cursor, VS Code, any MCP client) can call it as a tool. All entries use the official
[Apify MCP server](https://docs.apify.com/mcp) at `mcp.apify.com`, scoped to one actor with
`https://mcp.apify.com?tools=architekture/<slug>`. Nothing runs from this repo; it is configuration only.

All actors are pay per result: you pay for delivered rows, and rows with `"recordType": "status"` are free (they explain
blocked, empty or invalid inputs). Runs are billed to your own Apify account.

## How to use

1. Get an Apify API token at [console.apify.com/settings/integrations](https://console.apify.com/settings/integrations).
2. Put it in an environment variable, never in a config file you commit:
   `export APIFY_TOKEN=...` (macOS/Linux) or `setx APIFY_TOKEN ...` (Windows), then restart your client.
3. Copy the entries you need from [mcp.json](mcp.json) (or one actor's snippet below) into your client's MCP config.

[mcp.json](mcp.json) uses the common `mcpServers` format with `"type": "http"`; each entry sends
`Authorization: Bearer ${APIFY_TOKEN}`, which Claude Code (`.mcp.json`) expands from the environment.

- **Claude Code:** save the entries as `.mcp.json` in your project, or `claude mcp add --transport http architekture-<slug> "https://mcp.apify.com?tools=architekture/<slug>" --header "Authorization: Bearer $APIFY_TOKEN"`.
- **Cursor:** `~/.cursor/mcp.json`; write the header value as `Bearer ${env:APIFY_TOKEN}`.
- **VS Code:** `.vscode/mcp.json` uses `"servers"` instead of `"mcpServers"`; write the header value as `Bearer ${env:APIFY_TOKEN}` or use an `inputs` prompt.
- **Claude Desktop / claude.ai:** add `https://mcp.apify.com?tools=architekture/<slug>` as a custom connector; it signs you in to Apify with OAuth, so no token is needed.
- **No header support:** drop `headers` and keep only `url`; the Apify server then signs you in with OAuth.

Want several actors in one server? Join slugs with commas: `https://mcp.apify.com?tools=architekture/google-trends-scraper,architekture/google-hotels-scraper`.
Each actor tool comes with `get-actor-run`, `get-dataset-items`, `get-key-value-store-record` and `abort-actor-run`, so the
agent can read results and stop a run. Pass a spending cap (`maxTotalChargeUsd`) in the run options when your client offers it.

To tell the maintainers what you needed, add `"feedback": "<what you needed>"` to any run's input; output is unchanged
and a human reads every note. Code samples for Python, Node, curl, n8n and Make are in
[architek-earth/examples](https://github.com/architek-earth/examples).

## Actors

<!-- actors:start -->
**27 live actors.** Each one is its own server entry; copy only the ones you need.

### Ad Intelligence Watchlist

Meta Ad Library, any country (facebook.com/ads/library): new and changed Facebook and Instagram ads per advertiser since the last run: ad text, headline, link, CTA, format, start and end dates, platforms and changed fields.

Price: $1.50 per 1,000 · new or changed ad; status rows are free. Listing: [apify.com/architekture/ad-intelligence-watchlist](https://apify.com/architekture/ad-intelligence-watchlist).

Server URL: `https://mcp.apify.com?tools=architekture/ad-intelligence-watchlist`

```json
{
  "mcpServers": {
    "architekture-ad-intelligence-watchlist": {
      "type": "http",
      "url": "https://mcp.apify.com?tools=architekture/ad-intelligence-watchlist",
      "headers": {
        "Authorization": "Bearer ${APIFY_TOKEN}"
      }
    }
  }
}
```

### ALDI AU Scraper

ALDI Australia (aldi.com.au) scraper: product name, brand, pack size, price, was price, savings, specials, unit price, Special Buys date, category, image, URL; detail rows add ingredients, allergens, origin, storage, claims.

Price: $1.50 per 1,000 · product; status rows are free. Listing: [apify.com/architekture/aldi-au-product-scraper](https://apify.com/architekture/aldi-au-product-scraper).

Server URL: `https://mcp.apify.com?tools=architekture/aldi-au-product-scraper`

```json
{
  "mcpServers": {
    "architekture-aldi-au-product-scraper": {
      "type": "http",
      "url": "https://mcp.apify.com?tools=architekture/aldi-au-product-scraper",
      "headers": {
        "Authorization": "Bearer ${APIFY_TOKEN}"
      }
    }
  }
}
```

### ALDI Ireland Scraper

ALDI Ireland (aldi.ie) scraper: product name, brand, size, price in EUR, was price, saving, unit price, availability, Specialbuys on-sale date, category, image, URL; detail rows add ingredients, storage, nutritional claims, origin.

Price: $1.00 per 1,000 · product; status rows are free. Listing: [apify.com/architekture/aldi-ie-scraper](https://apify.com/architekture/aldi-ie-scraper).

Server URL: `https://mcp.apify.com?tools=architekture/aldi-ie-scraper`

```json
{
  "mcpServers": {
    "architekture-aldi-ie-scraper": {
      "type": "http",
      "url": "https://mcp.apify.com?tools=architekture/aldi-ie-scraper",
      "headers": {
        "Authorization": "Bearer ${APIFY_TOKEN}"
      }
    }
  }
}
```

### AliExpress Scraper

AliExpress global product search from aliexpress.com by keyword: sale price, original price, discount, currency, order count, rating, image, item URL, search position, sponsored flag, free shipping, delivery estimate.

Price: $2.50 per 1,000 · product; status rows are free. Listing: [apify.com/architekture/aliexpress-search-scraper](https://apify.com/architekture/aliexpress-search-scraper).

Server URL: `https://mcp.apify.com?tools=architekture/aliexpress-search-scraper`

```json
{
  "mcpServers": {
    "architekture-aliexpress-search-scraper": {
      "type": "http",
      "url": "https://mcp.apify.com?tools=architekture/aliexpress-search-scraper",
      "headers": {
        "Authorization": "Bearer ${APIFY_TOKEN}"
      }
    }
  }
}
```

### Coles Scraper

Coles Australia (coles.com.au) scraper: product name, brand, size, price, was price, savings, specials, multi-buy, unit price, category, image, URL; detail rows add GTIN barcode, ingredients, allergens, nutrition, origin.

Price: $1.50 per 1,000 · product; status rows are free. Listing: [apify.com/architekture/coles-au-product-scraper](https://apify.com/architekture/coles-au-product-scraper).

Server URL: `https://mcp.apify.com?tools=architekture/coles-au-product-scraper`

```json
{
  "mcpServers": {
    "architekture-coles-au-product-scraper": {
      "type": "http",
      "url": "https://mcp.apify.com?tools=architekture/coles-au-product-scraper",
      "headers": {
        "Authorization": "Bearer ${APIFY_TOKEN}"
      }
    }
  }
}
```

### EU E-Invoice Parser

EU e-invoices (XRechnung, ZUGFeRD, Factur-X, PEPPOL UBL) to JSON: invoice number, dates, seller and buyer VAT IDs, IBAN, net, tax and gross totals, line items, reconciliation checks and XML evidence.

Price: $2.00 per 1,000 · e-invoice; status rows are free. Listing: [apify.com/architekture/docparser-invoice-json](https://apify.com/architekture/docparser-invoice-json).

Server URL: `https://mcp.apify.com?tools=architekture/docparser-invoice-json`

```json
{
  "mcpServers": {
    "architekture-docparser-invoice-json": {
      "type": "http",
      "url": "https://mcp.apify.com?tools=architekture/docparser-invoice-json",
      "headers": {
        "Authorization": "Bearer ${APIFY_TOKEN}"
      }
    }
  }
}
```

### Dunnes Stores Scraper

Dunnes Stores Ireland (dunnesstores.com) fashion and home scraper: name, brand, EUR price, sale price, sizes, colours, SKU, EAN barcode, availability per size, category path, image, URL; detail rows add description, care, size-fit, origin.

Price: $1.00 per 1,000 · product; status rows are free. Listing: [apify.com/architekture/dunnes-ie-scraper](https://apify.com/architekture/dunnes-ie-scraper).

Server URL: `https://mcp.apify.com?tools=architekture/dunnes-ie-scraper`

```json
{
  "mcpServers": {
    "architekture-dunnes-ie-scraper": {
      "type": "http",
      "url": "https://mcp.apify.com?tools=architekture/dunnes-ie-scraper",
      "headers": {
        "Authorization": "Bearer ${APIFY_TOKEN}"
      }
    }
  }
}
```

### Google Hotels Scraper

Google Hotels (google.com/travel/hotels) scraper: nightly prices, stay totals, currency, guest ratings, review counts, star class, amenities, property type and stay dates, by destination or hotel name with optional check-in/check-out dates.

Price: $4.00 per 1,000 · hotel property; status rows are free. Listing: [apify.com/architekture/google-hotels-scraper](https://apify.com/architekture/google-hotels-scraper).

Server URL: `https://mcp.apify.com?tools=architekture/google-hotels-scraper`

```json
{
  "mcpServers": {
    "architekture-google-hotels-scraper": {
      "type": "http",
      "url": "https://mcp.apify.com?tools=architekture/google-hotels-scraper",
      "headers": {
        "Authorization": "Bearer ${APIFY_TOKEN}"
      }
    }
  }
}
```

### Google Shopping Scraper

Google Shopping scraper by keyword and country: title, price, sale price, merchant, rating, shipping and image per product; offers mode returns up to 5 merchant offers per product with price, delivery, total and link.

Price: $3.00 per 1,000 · delivered product; status rows are free. Listing: [apify.com/architekture/google-shopping-scraper](https://apify.com/architekture/google-shopping-scraper).

Server URL: `https://mcp.apify.com?tools=architekture/google-shopping-scraper`

```json
{
  "mcpServers": {
    "architekture-google-shopping-scraper": {
      "type": "http",
      "url": "https://mcp.apify.com?tools=architekture/google-shopping-scraper",
      "headers": {
        "Authorization": "Bearer ${APIFY_TOKEN}"
      }
    }
  }
}
```

### Google Trends Scraper

Google Trends Trending Now searches by country (title, approximate traffic, start time, related queries) and Explore keyword reports: interest over time, interest by region and related queries for up to 20 keywords, as rows.

Price: $1.00 per 1,000 · delivered trending now row; status rows are free. Listing: [apify.com/architekture/google-trends-scraper](https://apify.com/architekture/google-trends-scraper).

Server URL: `https://mcp.apify.com?tools=architekture/google-trends-scraper`

```json
{
  "mcpServers": {
    "architekture-google-trends-scraper": {
      "type": "http",
      "url": "https://mcp.apify.com?tools=architekture/google-trends-scraper",
      "headers": {
        "Authorization": "Bearer ${APIFY_TOKEN}"
      }
    }
  }
}
```

### Indeed Scraper

Indeed US jobs from indeed.com: job title, company, location, full description, salary range and period, job type, remote or hybrid label, posting date and job URL.

Price: $3.50 per 1,000 · job; status rows are free. Listing: [apify.com/architekture/indeed-scraper](https://apify.com/architekture/indeed-scraper).

Server URL: `https://mcp.apify.com?tools=architekture/indeed-scraper`

```json
{
  "mcpServers": {
    "architekture-indeed-scraper": {
      "type": "http",
      "url": "https://mcp.apify.com?tools=architekture/indeed-scraper",
      "headers": {
        "Authorization": "Bearer ${APIFY_TOKEN}"
      }
    }
  }
}
```

### LinkedIn Jobs Scraper

LinkedIn jobs (linkedin.com) public job search: title, company, location, posted date, description, salary with evidence, seniority, employment type, industries, workplace.

Price: $4.00 per 1,000 · delivered job; status rows are free. Listing: [apify.com/architekture/linkedin-jobs-monitor](https://apify.com/architekture/linkedin-jobs-monitor).

Server URL: `https://mcp.apify.com?tools=architekture/linkedin-jobs-monitor`

```json
{
  "mcpServers": {
    "architekture-linkedin-jobs-monitor": {
      "type": "http",
      "url": "https://mcp.apify.com?tools=architekture/linkedin-jobs-monitor",
      "headers": {
        "Authorization": "Bearer ${APIFY_TOKEN}"
      }
    }
  }
}
```

### Mercadona Scraper

Mercadona Spain (tienda.mercadona.es) scraper: name, brand, packaging, size, EUR price, unit price, previous price, VAT rate, category path, image, URL; detail rows add EAN barcode, ingredients, allergens, origin, suppliers.

Price: $1.00 per 1,000 · product; status rows are free. Listing: [apify.com/architekture/mercadona-es-scraper](https://apify.com/architekture/mercadona-es-scraper).

Server URL: `https://mcp.apify.com?tools=architekture/mercadona-es-scraper`

```json
{
  "mcpServers": {
    "architekture-mercadona-es-scraper": {
      "type": "http",
      "url": "https://mcp.apify.com?tools=architekture/mercadona-es-scraper",
      "headers": {
        "Authorization": "Bearer ${APIFY_TOKEN}"
      }
    }
  }
}
```

### New World NZ Scraper

New World NZ (newworld.co.nz) scraper: store, product ID, name, brand, size, shelf price, Clubcard price, unit price, promotions, category, channels, URL; details add EAN barcode, ingredients, allergens, nutrition, image.

Price: $4.00 per 1,000 · product; status rows are free. Listing: [apify.com/architekture/new-world-nz-scraper](https://apify.com/architekture/new-world-nz-scraper).

Server URL: `https://mcp.apify.com?tools=architekture/new-world-nz-scraper`

```json
{
  "mcpServers": {
    "architekture-new-world-nz-scraper": {
      "type": "http",
      "url": "https://mcp.apify.com?tools=architekture/new-world-nz-scraper",
      "headers": {
        "Authorization": "Bearer ${APIFY_TOKEN}"
      }
    }
  }
}
```

### Pak'nSave Scraper

Pak'nSave New Zealand (paknsave.co.nz) scraper: product ID, name, brand, package size, price in NZD, unit price, unit label, promotions, category, sales channels, URL, store ID.

Price: $4.00 per 1,000 · product; status rows are free. Listing: [apify.com/architekture/paknsave-nz-scraper](https://apify.com/architekture/paknsave-nz-scraper).

Server URL: `https://mcp.apify.com?tools=architekture/paknsave-nz-scraper`

```json
{
  "mcpServers": {
    "architekture-paknsave-nz-scraper": {
      "type": "http",
      "url": "https://mcp.apify.com?tools=architekture/paknsave-nz-scraper",
      "headers": {
        "Authorization": "Bearer ${APIFY_TOKEN}"
      }
    }
  }
}
```

### Sainsbury's Scraper

Sainsbury's UK (sainsburys.co.uk) scraper: product name, price, unit price, offers, promotions, EAN barcodes, labels, reviews, rating, category, availability, image, URL; detail rows add description, attributes, important information, images.

Price: $2.00 per 1,000 · product; status rows are free. Listing: [apify.com/architekture/sainsburys-uk-scraper](https://apify.com/architekture/sainsburys-uk-scraper).

Server URL: `https://mcp.apify.com?tools=architekture/sainsburys-uk-scraper`

```json
{
  "mcpServers": {
    "architekture-sainsburys-uk-scraper": {
      "type": "http",
      "url": "https://mcp.apify.com?tools=architekture/sainsburys-uk-scraper",
      "headers": {
        "Authorization": "Bearer ${APIFY_TOKEN}"
      }
    }
  }
}
```

### Shopify Scraper

Shopify store scraper for any public Shopify storefront, worldwide: products, variant prices, compare-at (sale) prices, SKUs, availability, options, images, tags and vendor, plus optional barcodes and inventory counts.

Price: $0.50 per 1,000 · product; status rows are free. Listing: [apify.com/architekture/shopify-products-scraper](https://apify.com/architekture/shopify-products-scraper).

Server URL: `https://mcp.apify.com?tools=architekture/shopify-products-scraper`

```json
{
  "mcpServers": {
    "architekture-shopify-products-scraper": {
      "type": "http",
      "url": "https://mcp.apify.com?tools=architekture/shopify-products-scraper",
      "headers": {
        "Authorization": "Bearer ${APIFY_TOKEN}"
      }
    }
  }
}
```

### Substack Scraper

Substack newsletter scraper (substack.com and custom domains): posts, authors, likes, comment counts, restacks, word counts, tags, dates, free-post full text, comment threads, subscriber bands.

Price: $1.00 per 1,000 · post; status rows are free. Listing: [apify.com/architekture/substack-scraper](https://apify.com/architekture/substack-scraper).

Server URL: `https://mcp.apify.com?tools=architekture/substack-scraper`

```json
{
  "mcpServers": {
    "architekture-substack-scraper": {
      "type": "http",
      "url": "https://mcp.apify.com?tools=architekture/substack-scraper",
      "headers": {
        "Authorization": "Bearer ${APIFY_TOKEN}"
      }
    }
  }
}
```

### Tennis Scraper

Flashscore tennis (global, flashscore.com): matches, live and final scores, set and tiebreak scores, point-by-point, match statistics, odds, head-to-head and ATP/WTA singles rankings.

Price: $2.50 per 1,000 · delivered match or ranking; status rows are free. Listing: [apify.com/architekture/tennis-data-scraper](https://apify.com/architekture/tennis-data-scraper).

Server URL: `https://mcp.apify.com?tools=architekture/tennis-data-scraper`

```json
{
  "mcpServers": {
    "architekture-tennis-data-scraper": {
      "type": "http",
      "url": "https://mcp.apify.com?tools=architekture/tennis-data-scraper",
      "headers": {
        "Authorization": "Bearer ${APIFY_TOKEN}"
      }
    }
  }
}
```

### Tesco UK Scraper

Tesco UK (tesco.com) scraper: product ID, TPNB, TPNC, GTIN barcode, title, brand, price, unit price, Clubcard price, promotions, offer end date, availability, department, aisle, shelf, ratings, image, URL.

Price: $2.00 per 1,000 · product; status rows are free. Listing: [apify.com/architekture/tesco-uk-scraper](https://apify.com/architekture/tesco-uk-scraper).

Server URL: `https://mcp.apify.com?tools=architekture/tesco-uk-scraper`

```json
{
  "mcpServers": {
    "architekture-tesco-uk-scraper": {
      "type": "http",
      "url": "https://mcp.apify.com?tools=architekture/tesco-uk-scraper",
      "headers": {
        "Authorization": "Bearer ${APIFY_TOKEN}"
      }
    }
  }
}
```

### Threads Replies Scraper

Threads replies scraper, global, threads.com: reply and comment rows with author handle, name and verified badge, text, like, reply, repost and quote counts, timestamp, media URLs, nesting depth, parent post and author flag, plus the root post.

Price: $2.50 per 1,000 · reply; status rows are free. Listing: [apify.com/architekture/threads-replies-scraper](https://apify.com/architekture/threads-replies-scraper).

Server URL: `https://mcp.apify.com?tools=architekture/threads-replies-scraper`

```json
{
  "mcpServers": {
    "architekture-threads-replies-scraper": {
      "type": "http",
      "url": "https://mcp.apify.com?tools=architekture/threads-replies-scraper",
      "headers": {
        "Authorization": "Bearer ${APIFY_TOKEN}"
      }
    }
  }
}
```

### TikTok Shop Scraper

TikTok Shop US (shop.tiktok.com) products by keyword search: price, currency, seller ID and name, rating, review count, sold count and product URL.

Price: $3.00 per 1,000 · product; status rows are free. Listing: [apify.com/architekture/tiktok-shop-products-scraper](https://apify.com/architekture/tiktok-shop-products-scraper).

Server URL: `https://mcp.apify.com?tools=architekture/tiktok-shop-products-scraper`

```json
{
  "mcpServers": {
    "architekture-tiktok-shop-products-scraper": {
      "type": "http",
      "url": "https://mcp.apify.com?tools=architekture/tiktok-shop-products-scraper",
      "headers": {
        "Authorization": "Bearer ${APIFY_TOKEN}"
      }
    }
  }
}
```

### Unified Video Transcript API

YouTube and TikTok video transcripts from youtube.com and tiktok.com in one JSON schema: transcript text, language, title, author, duration, caption tracks and optional timestamped segments.

Price: $1.00 per 1,000 · transcript; status rows are free. Listing: [apify.com/architekture/unified-transcript-api](https://apify.com/architekture/unified-transcript-api).

Server URL: `https://mcp.apify.com?tools=architekture/unified-transcript-api`

```json
{
  "mcpServers": {
    "architekture-unified-transcript-api": {
      "type": "http",
      "url": "https://mcp.apify.com?tools=architekture/unified-transcript-api",
      "headers": {
        "Authorization": "Bearer ${APIFY_TOKEN}"
      }
    }
  }
}
```

### Woolworths AU Scraper

Woolworths Australia (woolworths.com.au) scraper: product name, brand, size, price, was price, savings, specials, unit price, barcode, stock flags, image, URL; detail rows add ingredients, allergens, nutrition, health star rating, origin.

Price: $1.50 per 1,000 · product; status rows are free. Listing: [apify.com/architekture/woolworths-au-product-scraper](https://apify.com/architekture/woolworths-au-product-scraper).

Server URL: `https://mcp.apify.com?tools=architekture/woolworths-au-product-scraper`

```json
{
  "mcpServers": {
    "architekture-woolworths-au-product-scraper": {
      "type": "http",
      "url": "https://mcp.apify.com?tools=architekture/woolworths-au-product-scraper",
      "headers": {
        "Authorization": "Bearer ${APIFY_TOKEN}"
      }
    }
  }
}
```

### Woolworths NZ Scraper

Woolworths New Zealand (woolworths.co.nz, ex-Countdown) product data: prices, was prices, specials, club prices, multi-buys, promotion dates, unit prices, stock, barcodes, departments, images; ingredients and allergens on detail rows.

Price: $1.00 per 1,000 · product; status rows are free. Listing: [apify.com/architekture/woolworths-nz-scraper](https://apify.com/architekture/woolworths-nz-scraper).

Server URL: `https://mcp.apify.com?tools=architekture/woolworths-nz-scraper`

```json
{
  "mcpServers": {
    "architekture-woolworths-nz-scraper": {
      "type": "http",
      "url": "https://mcp.apify.com?tools=architekture/woolworths-nz-scraper",
      "headers": {
        "Authorization": "Bearer ${APIFY_TOKEN}"
      }
    }
  }
}
```

### Y Combinator Scraper

Y Combinator startup directory data from ycombinator.com: company name, batch, status, stage, industry, region, tags, team size, website, location, hiring flag, founders, LinkedIn links and open jobs.

Price: $2.00 per 1,000 · company; status rows are free. Listing: [apify.com/architekture/yc-companies-scraper](https://apify.com/architekture/yc-companies-scraper).

Server URL: `https://mcp.apify.com?tools=architekture/yc-companies-scraper`

```json
{
  "mcpServers": {
    "architekture-yc-companies-scraper": {
      "type": "http",
      "url": "https://mcp.apify.com?tools=architekture/yc-companies-scraper",
      "headers": {
        "Authorization": "Bearer ${APIFY_TOKEN}"
      }
    }
  }
}
```

### YouTube Transcript Scraper

YouTube transcripts, worldwide, from youtube.com: transcript text, timestamped segments, caption language, auto-generated flag, available languages, translations, title, channel, duration and view count, by video URL or ID.

Price: $4.00 per 1,000 · transcript; status rows are free. Listing: [apify.com/architekture/youtube-transcript-scraper](https://apify.com/architekture/youtube-transcript-scraper).

Server URL: `https://mcp.apify.com?tools=architekture/youtube-transcript-scraper`

```json
{
  "mcpServers": {
    "architekture-youtube-transcript-scraper": {
      "type": "http",
      "url": "https://mcp.apify.com?tools=architekture/youtube-transcript-scraper",
      "headers": {
        "Authorization": "Bearer ${APIFY_TOKEN}"
      }
    }
  }
}
```
<!-- actors:end -->

<sub>Generated weekly from the public Apify Store listings by [scripts/generate.py](scripts/generate.py).</sub>

## Contact

- Email: [north@architek.earth](mailto:north@architek.earth)
- Something broken or missing? [Open an issue](https://github.com/architek-earth/.github/issues/new).
