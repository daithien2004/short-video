# Video ngắn truyền thuyết Việt Nam

Chạy giao diện:

```
python D:\idea\studio.py      ->  http://localhost:8765
```

| Thư mục | Nội dung |
|---|---|
| `studio.py` | máy chủ giao diện (React, không cần build) |
| `src/` | bộ dựng (`engine.py`), giọng đọc (`shorts.py`), các cảnh đã vẽ (`scenes_hk*.py`), nhân vật và hoạt ảnh |
| `static/` | giao diện `studio.html` và thư viện React nằm sẵn trong `vendor/` |
| `assets/` | mascot, âm thanh, ảnh cũ |
| `projects/<tên>/script.json` | kịch bản của từng video |
| `previews/<tên>/` | bản nháp (mỗi lần dựng ghi đè) |
| `exports/<tên>/` | bản chính, mỗi lần xuất một file có ngày giờ |
| `cache/` | giọng và clip đã lưu, xoá được, tự tạo lại |
| `archive/` | thí nghiệm và file cũ, đã chuyển khỏi thư mục chính |

Cách làm việc, định dạng kịch bản và các quyết định đã chốt: xem skill `vn-legend-shorts` trong `.claude/skills/`.
