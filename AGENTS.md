# Hướng dẫn cho mọi AI/công cụ (không riêng Claude Code)

Dự án làm video ngắn tiếng Việt không lộ mặt bằng Studio (Python/FFmpeg/React). Chạy: `python studio.py` -> http://localhost:8765.

**Đọc trước khi làm bất cứ gì:** `.claude/skills/vn-legend-shorts/SKILL.md` (markdown thường, AI nào cũng đọc được). Trong đó có: quy trình, định dạng script.json, luật hình, hook, giọng, bộ nhớ đệm, đăng ký cảnh ở 4 chỗ, danh sách video đã làm, thể loại kể chuyện lừa đảo (phong cách mực), lỗi đã gặp.

Quy tắc cốt lõi: tiết kiệm token; người dùng chốt hook; cho xem ảnh/nháp trước khi xuất; không đăng bài thay người dùng; không tự thêm Co-Authored-By; màu nền chọn theo loại nội dung.

## Giao việc cho opencode (kinh nghiệm thực tế, cập nhật khi gặp thêm)
- Chạy nền không tương tác: `opencode run --auto --title "<tên>" "Read D:\idea	ools\opencode_tasks\oc_task.md and do exactly what it says"`; việc dài để trong file `tools/opencode_tasks/oc_task*.md` (mẫu giai đoạn 1 viết script, giai đoạn 2 vẽ cảnh + dựng nháp) (đường dẫn máy này có dấu `'`, đừng dán vào dòng lệnh). Terminal panel chỉ cho gõ một dòng ASCII, nên dùng `--prompt` trỏ tới file.
- Model mặc định miễn phí (big-pickle). Tách việc thành giai đoạn nhỏ, mỗi giai đoạn một file nhiệm vụ, có điều kiện dừng ("KHÔNG làm gì khác"). Giai đoạn 1 (viết script + nguồn) mất ~4 phút; giai đoạn 2 (vẽ cảnh + dựng nháp) lâu hơn.
- Chỗ nó mất thời gian: (1) tra web bằng cách tự gọi WebFetch vào Bing/Google/DuckDuckGo (bị chặn, thử đi thử lại hàng chục lần): nên chỉ rõ trang báo cụ thể hoặc cho sẵn từ khóa/URL; (2) lệnh shell sai cú pháp Windows (dùng `taskkill /PID` kiểu cmd trong Git Bash, phải `//PID`; `/dev/null`, `$VAR`): dặn "shell là Git Bash trên Windows, dùng `//` cho cờ taskkill, hoặc dùng PowerShell"; (3) tắt tiến trình Studio: nó tự kill cây tiến trình, nên dặn rõ chỉ kill đúng PID của studio.py.
- Luôn dặn: không git, không render final, không sửa file ngoài phạm vi. Người kiểm lại nguồn/số liệu và xem ảnh trước khi dựng.
- Để theo dõi kết quả mà không phải nhắn lại: chạy nền bằng công cụ có thông báo khi kết thúc (Claude Code: Bash run_in_background).
- Nhịp hình: khoảng 2 đến 3 giây một khung (75 giây ≈ 30 đến 36 khung). Lần đầu opencode cắt mọi cụm câu thành 1 khung (61 khung, ~1,3 giây) khiến cảnh chuyển liên tục. Chỉ giữ hình mạnh nhất của mỗi ý, gộp các cụm ngắn (ví dụ liệt kê Facebook, TikTok, Zalo dùng một khung).
- Không để nó thêm chi tiết không có trong nguồn (đã gặp: "cả nhà không ai hay", "để tạo lòng tin", lời công an chưa kiểm chứng). Luôn dặn "chỉ dùng chi tiết có trong sources.txt".
- Nó không xem được ảnh: phần xem ảnh xem trước do người/Claude làm.

## Nguyên tắc vẽ cao nhất (người dùng chốt)
Người xem nhìn vào phải HIỂU NGAY, không cần nhiều chi tiết: mỗi khung chỉ một vật/hành động to, rõ, đúng câu đang đọc. Không dùng hình trừu tượng, ký hiệu khó đoán, nhân vật đứng trơ trọi không làm gì, nét que/đường rời thay cho tay chân. Thà đơn giản mà dễ hiểu còn hơn nhiều chi tiết mà khó hiểu. Màu nền chọn theo nội dung từng cảnh/video.
