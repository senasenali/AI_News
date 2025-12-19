import feedparser
from datetime import datetime

RSS_FEEDS = {
    "OpenAI": "https://openai.com/blog/rss.xml",
    "Hugging Face": "https://huggingface.co/blog/feed.xml",
    "arXiv AI": "https://export.arxiv.org/rss/cs.AI",
    "arXiv CL": "https://export.arxiv.org/rss/cs.CL",
}

def fetch_feed(name, url, limit=5):
    feed = feedparser.parse(url)
    items = []
    for entry in feed.entries[:limit]:
        items.append({
            "title": entry.title,
            "link": entry.link,
            "published": entry.get("published", "")
        })
    return items

def generate_markdown(data):
    today = datetime.now().strftime("%Y-%m-%d")
    md = [f"# 🤖 AI Digest — {today}\n"]

    for source, items in data.items():
        md.append(f"## {source}\n")
        for item in items:
            md.append(f"- **{item['title']}**")
            md.append(f"  - {item['link']}")
        md.append("")

    return "\n".join(md)

def main():
    all_data = {}
    for name, url in RSS_FEEDS.items():
        all_data[name] = fetch_feed(name, url)

    markdown = generate_markdown(all_data)

    with open("AI_Digest.md", "w", encoding="utf-8") as f:
        f.write(markdown)

    print("✅ AI_Digest.md 已生成")

if __name__ == "__main__":
    main()
