
# Pet

## Structure

`Pet`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `long\|int` | Optional | - |
| `category` | [`Category`](../../doc/models/category.md) | Optional | - |
| `name` | `str` | Required | - |
| `photo_urls` | `List[str]` | Required | - |
| `tags` | [`List[Tag]`](../../doc/models/tag.md) | Optional | - |
| `status` | [`StatusEnum`](../../doc/models/status-enum.md) | Optional | pet status in the store |

## Example (as JSON)

```json
{
  "id": 112,
  "category": {
    "id": 232,
    "name": "name2"
  },
  "name": "name0",
  "photoUrls": [
    "photoUrls5",
    "photoUrls6",
    "photoUrls7"
  ],
  "tags": [
    {
      "id": 239,
      "name": "name5"
    },
    {
      "id": 240,
      "name": "name6"
    }
  ],
  "status": "sold"
}
```

