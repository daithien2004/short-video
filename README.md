# Video ngắn truyền thuyết Việt Nam

Chạy giao diện:

```
python D:\idea\studio.py      ->  http://localhost:8765
```

| Thư mục | Nội dung |
|---|---|
| `studio.py` | máy chủ giao diện (React, không cần build) |
| `src/` | bộ dựng (`engine.py`), giọng đọc (`shorts.py`), nhân vật và cảnh theo từng truyện (`chars_*.py`, `scenes_*.py`) |
| `tools/` | `autoshots.py` (chia khung theo giọng), `sheet.py` (bảng ảnh tĩnh), `hooksheet.py` (ảnh chữ bìa) |
| `static/` | giao diện `studio.html` và thư viện React nằm sẵn trong `vendor/` |
| `assets/` | mascot, âm thanh, ảnh cũ |
| `projects/<tên>/script.json` | kịch bản của từng video |
| `previews/<tên>/` | bản nháp (mỗi lần dựng ghi đè) |
| `exports/<tên>/` | bản chính (một file `.mp4` có ngày giờ) và `caption.txt` |
| `cache/` | giọng và clip đã lưu, xoá được, tự tạo lại |
| `archive/` | thí nghiệm và file cũ, đã chuyển khỏi thư mục chính |

Cách làm việc, định dạng kịch bản và các quyết định đã chốt: xem skill `vn-legend-shorts` trong `.claude/skills/`.
