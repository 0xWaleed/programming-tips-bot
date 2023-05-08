
template = """
{
  "content": null,
  "embeds": [
    {
      "title": "Tip",
      "description": "{content}",
      "color": null
    }
  ],
  "attachments": [],
  "flags": 4100
}
"""

def webhook_builder(content):
    return template.format(content=content)

