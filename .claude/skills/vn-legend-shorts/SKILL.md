---
name: vn-legend-shorts
description: Làm video ngắn kể truyền thuyết/lịch sử Việt Nam (không lộ mặt, TikTok/Facebook Reels) bằng Studio trong D:\idea. Dùng khi người dùng muốn làm kịch bản/video mới, sửa cảnh, dựng nháp, xuất bản đẹp, viết caption, hoặc khi cần nhớ các quyết định đã chốt và lỗi không được lặp lại.
---

# Video truyền thuyết Việt Nam (D:\idea)

## Mục tiêu và nguyên tắc làm việc
- Làm video ngắn kể truyền thuyết/lịch sử, không lộ mặt, tiếng Việt, có thể lên xu hướng. Giai đoạn đầu là dự án của một người, làm bằng Studio chạy trên máy.
- **Tiết kiệm token là ưu tiên số 1.** Claude chỉ viết kịch bản JSON ngắn và vẽ các cảnh còn thiếu. Giọng, dựng hình, phụ đề, trộn âm là code Python/FFmpeg có sẵn. Không gọi MCP nặng khi không cần.
- **Không hỏi nhiều.** Tự chọn phương án hợp lý, làm, rồi cho người dùng xem. Chỉ hỏi khi quyết định thật sự là của họ.
- **Cho xem khung hình/ý tưởng trước, đừng render video vội.** Xem ảnh tĩnh (bảng nhiều khung) rồi mới dựng nháp.
- **Không bao giờ đăng bài thay người dùng.** Chỉ viết nội dung đăng, họ tự đăng. Việc "xuất bản" trong Studio chỉ là xuất file.
- Người dùng nói tiếng Việt. Trả lời tiếng Việt, ngắn, nói rõ cái gì đã kiểm tra và cái gì chưa (chưa nghe giọng, chưa xem video chạy, chỉ xem ảnh tĩnh...).

## Bản đồ thư mục
```
D:\idea
  studio.py            chạy giao diện:  python D:\idea\studio.py  ->  http://localhost:8765
  src\                 engine.py (bộ nhớ đệm + dựng), shorts.py (giọng VieNeu, mix), build.py (helper cũ: tint, MOOD, title2),
                       story2/story3/tulinh*/animate/opening_frames (nhân vật, khung hình nền), scenes_hk.py + scenes_hk2.py (các cảnh đã vẽ)
  static\              studio.html (React + Babel nằm sẵn trong static\vendor, không cần build, không cần mạng)
  assets\mascot        0.png (ngạc nhiên), 1.png (suy nghĩ)
  projects\<tên>\script.json    mỗi video một thư mục
  previews\<tên>\      bản nháp (ghi đè)
  exports\<tên>\       bản chính, mỗi lần xuất một file có ngày giờ, không ghi đè
  cache\               giọng và clip lưu theo nội dung, xoá được, tự tạo lại
  archive\             thí nghiệm và file cũ (chuyển vào đây, không xoá)
```
Chạy lại Studio: tắt tiến trình cũ trước (tắt `studio.py` mà để sót tiến trình con thì ăn hết RAM). Chỉ tắt đúng tiến trình `studio.py` và `multiprocessing.spawn`, đừng tắt mọi python.

## Quy trình làm một truyền thuyết mới
1. **Chọn chuyện và kiểm tra sự kiện bằng nguồn** (tìm web). Chỉ dùng sự kiện chính xác, **không dùng điều gây tranh cãi**. Chi tiết chỉ có trong truyền thuyết thì mở bằng "Truyền thuyết kể rằng", điều chưa chắc thì viết "nhiều người tin". Không kể năm cụ thể nếu chưa chắc.
2. **Viết kịch bản** vào `projects/<tên>/script.json` (tạo bằng nút "+ Dự án mới" hoặc tạo thư mục thủ công).
   - Giọng người dẫn truyện nghiêm trang, câu ngắn, kể như người kể chuyện.
   - Mở đầu bằng một câu hook ngắn trùng tiêu đề bìa. Hook chỉ khoảng 3 đến 5 giây (bìa + câu đầu).
   - **Số và năm viết bằng chữ** ("hai nghìn không trăm mười sáu") vì giọng đọc số sai.
   - Dài khoảng **1:05 đến 1:20**, 10 đến 12 cảnh (độ dài thực tế lúc giọng 1.12x: khoảng 330 chữ ≈ 1:10). TikTok chỉ trả tiền video dài hơn 1 phút (nguồn thứ cấp, nhắc người dùng tự kiểm tra); Reels của Facebook không có mức tối thiểu cố định.
   - **Không đặt câu hỏi kết ở cuối video.** Đưa câu hỏi vào bình luận ghim.
   - Không lời kêu gọi "follow".
3. **Chia khung hình theo từng ý** (xem mục luật hình). Dùng `shots` với chỉ số câu.
4. **Kiểm tra cảnh còn thiếu.** Dùng lại cảnh có sẵn nếu hợp, nhưng không lặp lại nguyên một cảnh. Thiếu thì vẽ mới (xem mục vẽ cảnh), đăng ký, xem bảng ảnh tĩnh.
5. **Dựng nháp trong Studio, người dùng xem, sửa theo phản hồi**, rồi mới xuất bản đẹp.
6. **Viết caption TikTok/Facebook** (ngắn, ít hashtag, có bình luận ghim). Không đăng giùm.

## Định dạng script.json
```json
{"title": ["TRUYỀN THUYẾT", "HỒ HOÀN KIẾM"], "hook": "Truyền thuyết về Hồ Hoàn Kiếm?", "cover": "tower", "speed": 1.12,
 "scenes": [
  {"scene": "hanoi", "text": "Câu một, câu hai. Câu ba?", "mood": "kich", "mascot": true, "fx": ["fireflies"],
   "shots": [{"at": 1, "scene": "swordlake"}, {"at": 3, "scene": "scroll", "mood": "tram"}]}]}
```
- `scene` là cảnh đầu của cảnh nội dung; `shots[].at` là chỉ số câu (0, 1, 2...) bắt đầu đổi sang cảnh khác, chuyển mờ 0,3 giây. Câu = đoạn cắt tại `. , ? ! :`.
- `mood`: `kich` (đỏ), `huyen` (tím), `tram` (xám xanh). Bốn bảng màu đã chốt: đêm / bình minh / huyền bí / kịch tính.
- `cover`: cảnh làm nền bìa (đang dùng `tower`, hồ đêm có trăng và tháp).
- `speed`: tốc độ giọng, mặc định 1.12 (thanh trượt trong Studio).
- Các khóa `cam` và `at` (zoom/lia máy) vẫn có trong code nhưng **người dùng không thích, đừng dùng**.

## Luật về hình (người dùng đã chốt qua nhiều vòng sửa)
- **Hình đổi theo nội dung đang đọc.** Mỗi khung hình giữ tối đa khoảng 3,5 giây, thường 1 đến 3 giây. Cảnh dài mà một hình là chán.
- **Mỗi khung hình là một cảnh vẽ mới.** Được dùng lại nhân vật, đồ vật, mảnh nền; **không** dùng lại nguyên một cảnh đã xuất hiện trong video.
- **Mỗi nhân vật trong truyện có hình riêng, phân biệt được.** Không dùng chung một hình người (ví dụ cùng một mẫu "Lê Lợi" áo đỏ mũ quan) cho nhiều nhân vật khác nhau như vua, người đánh cá, lính, nông dân, quân địch. Khác nhau về trang phục, màu, mũ, dáng, đồ cầm. Một nhân vật xuất hiện lại ở nhiều cảnh thì giữ nguyên hình của nhân vật đó. (Video Hoàn Kiếm đã mắc lỗi này và đã xong, đừng lặp lại ở truyện sau.) Khi lên danh sách cảnh, ghi rõ từng nhân vật và cách nhận ra họ trước khi vẽ.
- **Hoạt ảnh tối giản**, chủ yếu thể hiện nội dung. Chỉ đẩy máy chậm 5% (mặc định) và chuyển động nhẹ (sóng, mây, đom đóm). Không zoom/lia kiểu "phóng lên".
- **Phong cách cắt giấy (paper-cut)**, nhân vật đơn giản dễ đọc, nền phẳng. Giữ nguyên hình đã chốt, không "cải thiện" khi chưa được yêu cầu.
- **Phụ đề:** chữ trắng, hiện 1 đến 2 từ một lần, nảy nhẹ, cao khoảng 70% màn hình. **Không** dùng dòng sự kiện màu vàng, không highlight vàng, không thẻ câu hỏi, không chép từ video tham khảo của người dùng (chỉ để lấy cảm hứng).
- **Chuyển cảnh:** xé giấy giữa bìa và cảnh một; chuyển mờ giữa các cảnh.
- **Bìa:** nền hồ đêm trăng + tháp + ánh vàng, tiêu đề hai dòng dạng sticker (dòng 1 vàng, dòng 2 trắng), **mascot rất lớn ở giữa**, **không có thanh gươm trên bìa** (người dùng đã loại 7 cách đặt gươm). Mascot trồi từ đáy lên (0,45 giây, làm chậm dần, không nảy), đứng lại, đổi sang tư thế suy nghĩ khoảng 0,7 giây, rồi chìm xuống, xé giấy vào cảnh một. Nền trôi nhẹ để không bị đơ.
- **Mascot** chỉ hiện đúng hai lần: bìa, và một lần phản ứng ở điểm ngoặt (mượt, trồi lên rồi chìm xuống). **Không bao giờ lộ viền cắt phẳng ở đáy**: luôn giấu đáy dưới mép màn hình (cộng thêm độ lệch khi có nảy). Mascot nằm giữa nhờ khung cắt chung cho hai tư thế (xem `tulinh3.mascot`).
- Vùng an toàn của TikTok/Facebook (khoảng 20% đáy, cột phải, 200 px trên) là ước lượng từ blog, **chưa đo thực tế**.

## Giọng và âm thanh
- Giọng VieNeu-TTS mặc định "Hải Đăng" (nam), **không dùng edge-tts**. Đọc từng câu, tăng tốc `atempo` (script `speed`, mặc định 1.12). Đoạn nghỉ 0,12 giây sau câu, 0,04 giây sau dấu phẩy.
- Chuỗi âm cuối: acompressor + loudnorm I=-16.5. Tiếng pad và tiếng whoosh khi chuyển cảnh tạo bằng code (không cần bản quyền).
- VieNeu không có mốc thời gian từng từ nên phụ đề chia theo số ký tự (ước lượng). Căn khớp chính xác cần forced alignment (chưa làm).

## Bộ nhớ đệm và tốc độ (đừng phá)
- Giọng gốc lưu một lần cho mỗi câu; tốc độ chỉ là bước ffmpeg rẻ, nên chỉnh tốc độ không phải đọc lại.
- Clip lưu theo nội dung cảnh + phiên bản mã (giờ sửa đổi các file trong `CODE` của `src/engine.py`). **Thêm file hình mới thì phải thêm vào `CODE`**, nếu không clip cũ không biết là cũ. Sửa mã dựng/hình là làm lại hết clip một lần; chỉ sửa kịch bản thì chỉ làm lại cảnh đổi và cảnh kế tiếp (vì chuyển mờ).
- Thời lượng cảnh làm tròn lên bội của 1/15 giây để mọi cảnh độc lập nhau.
- Đo thực tế: dựng nháp lạnh khoảng 2 phút, không đổi gì khoảng 3 giây, sửa một cảnh khoảng 26 giây. Bản đẹp (1080x1920, 30fps) nặng hơn, vẽ riêng.

## Vẽ cảnh mới (khi thiếu)
- Hàm trả về `(nền RGB 1080x1920, [lớp...])`. Lớp: `(tốc_độ_parallax, layer(vẽ, bóng, lệch), hàm_chuyển_động(t)→(dx,dy))` hoặc lớp giả `(0,"glow",ảnh)`, `(0,"rays",ảnh)`, `(0,"sparkle",None)`. Đăng ký tên trong `registry()` (`scenes_hk.py`) hoặc `REG` trong `scenes_hk2.py`, thêm tên vào `SCENES` trong `studio.py` và nhãn tiếng Việt trong `LABEL` ở `static/studio.html`.
- Trình vẽ `D` chỉ có `polygon, ellipse, rectangle, line, arc, pieslice, regular_polygon`. **Không có `rounded_rectangle`.** Toạ độ và kích thước phải là số nguyên (ép `int`) khi tạo ảnh/mảng. Lớp vẽ trên bề rộng `W+2*PAD` (PAD=70).
- Dùng lại được: đồ vật và nền (`X.boat`, gươm, tháp, sóng, núi) và **cùng một nhân vật ở các cảnh khác**. `X.person` hiện chỉ là một mẫu người áo đỏ mũ quan: chỉ dùng cho đúng một nhân vật, nhân vật khác phải vẽ hàm riêng (đã có `_peasant`, `_foe` làm mẫu). Đồ vật khác: `X.boat`, `X.turtle`, `S.sword_rgba`, `S.sword_glow`, `X.tower_layer`, sóng `fill_wave`, núi `S.mountain`.
- **Xem bảng ảnh tĩnh nhiều cảnh trước** (render vài khung rồi ghép thành một ảnh), sửa, rồi mới dựng video.

## Những sai lầm đã gặp, đừng lặp lại
- Render video ngay khi người dùng chưa xem khung hình. (Họ đã nói "đừng render vội".)
- Dùng lại nguyên cảnh cho nhiều khung hình, một cảnh dài giữ một hình, zoom/lia máy, bìa tĩnh, thanh gươm trên bìa.
- **Dùng chung một hình nhân vật (`X.person`, áo đỏ mũ quan) cho nhiều nhân vật khác nhau** (vua, ngư dân, lính, nông dân...). Mỗi nhân vật phải có hình riêng.
- Để mascot lộ viền dưới, hoặc lệch tâm (nhiều pixel mờ làm hộp bao sai: dùng khung cắt chung).
- Ép người dùng chọn quá nhiều câu hỏi hoặc đề xuất xong lại chờ. Hãy chọn, làm, cho xem.
- Nói "xong" khi chưa kiểm tra: luôn nói rõ chỉ xem ảnh tĩnh hay đã xem video, đã nghe giọng chưa.
- Đưa ra sự kiện lịch sử từ trí nhớ mà không tra nguồn, hoặc dùng điều đang tranh cãi.
- Ghi chú rác: câu hỏi cuối video, kêu gọi theo dõi.
- Xoá file của người dùng. **Chuyển vào `archive`, đừng xoá**, trừ khi họ yêu cầu.

## Bẫy kỹ thuật trên máy này (Windows)
- Chạy Python với `PYTHONUTF8=1` để in tiếng Việt. Đường dẫn dùng `D:/idea/...` hoặc `/d/idea/...` trong bash.
- Khi viết nhiều file, dùng công cụ Write hoặc Edit, không dùng heredoc nhiều file (shell báo lỗi). Khi sửa chuỗi có xuống dòng trong file HTML/JSX, dùng Edit, đừng viết `\n` qua heredoc (nó thành xuống dòng thật và làm hỏng Babel).
- `from opening_frames import *` ghi đè biến `H` (=1920); đặt tên khác.
- Mỗi tiến trình vẽ giữ vài cảnh trong RAM (LRU 6) và dùng tối đa 6 tiến trình; máy có 16 GB, đừng tăng. Thiếu RAM sẽ báo `MemoryError`/`BrokenProcessPool`.
- Import `opening_frames` tự ghi ảnh vào `out/` và dựng 7 cảnh khi import (chậm, mỗi tiến trình vẽ mất vài giây).
- claude-mem có thể báo mất đăng nhập: người dùng cần `/login` hoặc `claude setup-token`; không tự khởi động lại worker.

## Việc còn mở (làm sau, khi người dùng yêu cầu)
- Tách 26 cảnh Hoàn Kiếm thành **thư viện mảnh ghép** (nền, nhân vật, đồ vật, hiệu ứng) và cảnh dạng "công thức" dữ liệu, để truyện sau tốn ít token. Cần thêm nhiều nhân vật có hình riêng (nữ, trẻ em, nhà sư, lính, vua, ngư dân, tướng...), mỗi loại một diện mạo, và thư viện phải có sẵn trước khi làm truyện sau.
- Forced alignment để phụ đề khớp từng từ. Đo vùng an toàn thật trên điện thoại. Huy hiệu "cần làm lại" riêng cho bản đẹp.
