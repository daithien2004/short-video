---
name: vn-legend-shorts
description: Làm video ngắn kể truyền thuyết/lịch sử Việt Nam (không lộ mặt, TikTok/Facebook Reels) bằng Studio trong D:\idea. Dùng khi người dùng muốn làm kịch bản/video mới, sửa cảnh, đổi hook, dựng nháp, xuất bản đẹp, viết caption, hoặc khi cần nhớ các quyết định đã chốt và lỗi không được lặp lại.
---

# Video truyền thuyết Việt Nam (D:\idea)

## Nguyên tắc làm việc
- Làm video ngắn kể truyền thuyết/lịch sử, không lộ mặt, tiếng Việt. Một người dùng, chạy bằng Studio trên máy.
- **Tiết kiệm token là ưu tiên số 1.** Claude chỉ viết kịch bản JSON ngắn và vẽ các cảnh còn thiếu. Giọng, dựng hình, phụ đề, trộn âm là code Python/FFmpeg có sẵn.
- **Người dùng quyết định hook.** Đưa vài bản (kèm từ khóa vàng gợi ý, nói bản nào nghiêng về), chờ họ chốt, KHÔNG tự ghi vào kịch bản trước. (Một lần ghi hook khi họ chưa chốt, họ đã phản đối.) Các việc khác thì tự chọn hợp lý, làm, rồi cho xem; đừng hỏi nhiều.
- **Cho xem trước khi dựng/xuất:** bảng ảnh tĩnh cảnh, ảnh chữ bìa từng dòng (`tools/hooksheet.py`). Khi họ bảo "xuất" hoặc "xuất bản đẹp" thì xuất ngay.
- **Không bao giờ đăng bài thay người dùng.** Chỉ viết caption. "Xuất bản" trong Studio chỉ là xuất file.
- Trả lời tiếng Việt, ngắn. Nói rõ cái gì đã kiểm tra và chưa (chưa nghe giọng, chưa xem video chạy, chỉ xem ảnh tĩnh).
- Không xóa file của người dùng; chuyển vào `archive/`. Ngoại lệ: họ nói "ghi đè" bản xuất cũ thì thay bằng bản mới (xóa bản cũ chỉ sau khi bản mới xuất thành công).

## Bản đồ thư mục
```
studio.py                    giao diện: python studio.py -> http://localhost:8765
src/engine.py                bộ dựng có bộ nhớ đệm; src/shorts.py giọng VieNeu + trộn âm
src/chars*.py, scenes*.py    nhân vật và cảnh theo từng truyện (xem "Truyện đã làm")
src/scenes_hk.py             registry() gộp mọi REG của các tệp cảnh
static/studio.html           giao diện React (không cần build)
tools/autoshots.py           tự chia khung theo thời lượng giọng
tools/sheet.py               bảng ảnh tĩnh nhiều cảnh
tools/hooksheet.py           ảnh chữ bìa từng dòng
projects/<tên>/script.json   kịch bản
previews/<tên>/              bản nháp (xóa sau khi xuất)
exports/<tên>/               bản chính + caption.txt (mỗi video đúng một file .mp4)
cache/                       giọng, clip, ảnh tĩnh (xóa được); archive/ file cũ
```
Chạy lại Studio: tắt đúng tiến trình `studio.py` và `multiprocessing.spawn` (đừng tắt mọi python), rồi chạy lại bằng công cụ PowerShell. **Phải khởi động lại Studio sau khi sửa kịch bản hoặc `engine.py`**: máy chủ giữ kịch bản và mã trong bộ nhớ, ảnh tĩnh sẽ cũ.

## Quy trình một truyện mới
1. **Chọn truyện, tra nguồn web.** Chỉ dùng sự kiện chính xác, tránh điều tranh cãi; chi tiết truyền thuyết mở bằng "Truyền thuyết kể rằng", điều chưa chắc viết "nhiều người tin" hoặc "tương truyền". Không nêu số đời vua, năm hay địa danh hành chính nếu các nguồn không thống nhất.
2. **Viết kịch bản** `projects/<tên>/script.json`: 10 đến 12 đoạn, khoảng 320 chữ (giọng 1.12 ≈ 1:10 đến 1:15; mục tiêu 1:05 đến 1:20). Giọng người kể chuyện nghiêm trang, câu ngắn. Số và năm viết bằng chữ. Không câu hỏi kết, không "follow" (đưa câu hỏi vào bình luận ghim).
3. **Lên danh sách nhân vật trước khi vẽ**, mỗi người một diện mạo riêng (xem luật hình), rồi danh sách cảnh (khoảng 3 đến 4 cảnh cho mỗi đoạn).
4. **Vẽ nhân vật + cảnh mới** (tệp `chars_xx.py`, `scenes_xx.py`, tiền tố `xx_`), đăng ký, xem bảng ảnh tĩnh (`tools/sheet.py`), sửa.
5. **Chia khung:** mỗi đoạn trong script ghi `"seq": [tên các cảnh theo thứ tự]`, chạy `python tools/autoshots.py <dự án>` (sinh giọng rồi chọn điểm cắt để mỗi khung 1 đến 3,5 giây).
6. **Hook:** đưa vài bản, chờ người dùng chốt, ghi `hook` và `hl`.
7. **Dựng nháp, gửi; sửa theo phản hồi; xuất bản đẹp** (Studio `/api/render` mode `final`), viết `exports/<tên>/caption.txt`, dọn `previews/<tên>`.
8. Cập nhật mục "Truyện đã làm" trong skill này.

## Định dạng script.json
```json
{"hook": "Mai an tiêm đã nói gì, mà bị vua đày ra đảo hoang?", "hl": ["MAI AN TIÊM", "ĐẢO HOANG"], "cover": "ma_island_empty", "speed": 1.12, "pause": 0.2,
 "scenes": [{"scene": "ma_court", "text": "Câu một, câu hai. Câu ba?", "mascot": true,
             "seq": ["ma_court", "ma_home", "ma_family"],
             "shots": [{"at": 1, "scene": "ma_home"}, {"at": 2, "scene": "ma_family"}]}]}
```
- `seq` do `autoshots.py` đọc để sinh `scene` + `shots`. `shots[].at` là chỉ số đoạn đọc (đoạn = cắt tại `. , ? ! :`), chuyển mờ 0,3 giây.
- `hl`: cụm từ khóa tô vàng trên bìa, viết HOA đúng như trong hook; không có thì tô tên nhân vật trong `NAMES_HL` của engine; không có gì thì toàn vàng. Không còn trường `title`.
- `speed` 1.12 và `pause` 0.20 **cho mọi video** (Hoàn Kiếm từng lệch 0.12 nên nhanh hơn; đã sửa).
- `mood`: `kich` (đỏ), `huyen` (tím), `tram` (xám xanh). `mascot: true` cho đúng một đoạn ngoặt. Khóa `cam`/`at` (zoom/lia máy) người dùng không thích, đừng dùng.
- `cover`: cảnh làm nền bìa, chọn cảnh ngầm hợp truyện, không quá sáng (nền sương bị ánh vàng đè trông bẩn).

## Luật về hình
- **Hình đổi theo lời đang đọc.** Mỗi khung tối đa khoảng 3,5 giây, thường 1 đến 3 giây; khung đầu đoạn không dưới 1 giây.
- **Mỗi khung là một cảnh vẽ mới.** Được dùng lại nhân vật, đồ vật, mảnh nền; không dùng lại nguyên một cảnh đã xuất hiện trong cùng video.
- **Mỗi nhân vật có hình riêng, phân biệt được** (trang phục, màu, mũ, dáng, đồ cầm). Không dùng chung một mẫu người cho nhiều nhân vật. Một nhân vật xuất hiện lại thì giữ nguyên hình.
- **Hoạt ảnh tối giản**, chỉ chuyển động nhẹ (sóng, mây, mưa, đom đóm). Không zoom/lia kiểu "phóng lên". Phong cách cắt giấy (paper-cut), nền phẳng. Không "cải thiện" hình đã chốt khi chưa được yêu cầu.
- **Phụ đề:** chữ trắng, 1 đến 2 từ một lần, nảy nhẹ, cao khoảng 70% màn hình. Không dòng sự kiện vàng, không thẻ câu hỏi, không chép video tham khảo.
- **Chuyển cảnh:** xé giấy từ bìa sang cảnh một; chuyển mờ giữa các cảnh.
- **Mascot** hiện đúng hai lần: bìa và một đoạn ngoặt. Không bao giờ lộ viền cắt phẳng ở đáy (luôn giấu dưới mép màn hình).
- Vùng an toàn TikTok/Facebook chỉ là ước lượng từ blog, **chưa đo thực tế**.

## Bìa và hook
- **Chữ bìa = câu hook đọc ở đầu video, đúng từng chữ**, tự sinh từ hook (hàm `hook_lines`, `_hook_layer` trong engine). Dấu phẩy không hiện.
- **Cỡ chữ cố định 108** (người dùng chốt theo video Nỏ thần), mỗi dòng tối đa 12 ký tự, lề ≥120 px mỗi bên. Chỉ MỘT dòng hiện một lúc, dòng mới thay dòng cũ, nằm gần giữa màn hình (y≈680/1920), nảy nhẹ 0,18 giây đúng lúc giọng đọc tới chữ đầu dòng; chỉ mờ đi sau khi dòng cuối đã hiện.
- **Màu: mỗi dòng một màu. Từ khóa (`hl`) màu vàng, phần còn lại trắng.** Ngắt dòng không gộp qua chỗ giọng nghỉ (dấu phẩy, dấu hỏi) và không gộp khác màu; tên hai chữ (Thủy Tinh, Sơn Tinh...) không bị tách. Có thể còn vài dòng ngắn đứng riêng; người dùng chấp nhận.
- **Mascot ở bìa:** trồi từ đáy lên chậm và mượt (khoảng 1 giây, làm chậm dần, không nảy), đứng yên (không chìm xuống), đổi tư thế suy nghĩ ở giây 1,3, rồi xé giấy. Không có thanh gươm trên bìa.
- **Hook hay:** có tên nhân vật + một câu hỏi cụ thể người xem chưa biết ("Tại sao Thủy Tinh…", "Với chiếc nỏ thần…, Trọng Thủy đã làm gì?", "Mai An Tiêm đã nói gì, mà…?"). Không dùng hook chung chung ("Truyền thuyết về…"). Dấu phẩy đặt như viết bình thường (phẩy trước "mà", sau vế trạng ngữ), không ngắt vô cớ sau tên nhân vật. Tránh đề tài tranh cãi.
- Nếu tên ở đầu hook đọc không liền mạch, viết thường tên trong `hook` để thử ("Mai an tiêm"); bìa vẫn hiện HOA. Phần kể thì giữ nguyên chữ hoa (phụ đề hiện đúng chữ trong lời kể). Muốn sửa cách đọc trong phần kể cần thêm bảng "chữ hiện / chữ đọc" (chưa làm).

## Giọng và âm thanh
- VieNeu-TTS "Hải Đăng" (nam), không dùng edge-tts. Đọc từng đoạn, tăng tốc bằng `atempo` 1.12, mỗi đoạn có 8 ms làm mượt hai đầu. Nghỉ sau câu 0,20 giây, sau dấu phẩy một phần ba (người dùng chọn 0,20 khi so với video tham khảo).
- Chuỗi âm cuối nhẹ: `highpass=f=70,loudnorm=I=-16:TP=-1.5:LRA=11,alimiter=limit=0.89`. Không dùng `acompressor` mạnh (làm giọng vỡ).
- **Chưa nghe được âm thanh.** Khi nghi giọng có vấn đề, làm 3 đến 4 mẫu A/B (`engine.unit(text, True, lead=0.2, rate=..., pause=...)` rồi `soundfile.write`) gửi người dùng nghe, đừng đoán.
- VieNeu không có mốc thời gian từng từ nên phụ đề và nhịp hiện dòng bìa chia theo số ký tự (ước lượng). Căn chính xác cần forced alignment (chưa làm).

## Bộ nhớ đệm (đừng phá)
- Giọng gốc lưu một lần cho mỗi đoạn; tốc độ chỉ là bước ffmpeg. Clip lưu theo nội dung cảnh + phiên bản mã (giờ sửa đổi các file trong `CODE` của `engine.py`). **File hình mới phải thêm vào `CODE`.** Sửa mã dựng/hình làm lại hết clip một lần (nháp lạnh khoảng 2 phút, xuất khoảng 2 đến 3 phút); sửa kịch bản chỉ làm lại cảnh đổi và cảnh kế tiếp.
- Thời lượng cảnh làm tròn lên bội của 1/15 giây. Nháp 540x960@15fps, bản đẹp 1080x1920@30fps.

## Vẽ cảnh mới
- Hàm trả về `(nền RGB 1080x1920, [lớp...])`; lớp `(tốc_độ_parallax, layer, hàm_chuyển_động(t)→(dx,dy))` hoặc lớp giả `(0,"glow",ảnh)`, `(0,"rays",ảnh)`, `(0,"sparkle",None)`. Dựng bằng helper có sẵn: `L`, `sky`, `grad`, `fill_wave`, `S.mountain`, `S.sword_glow`, `X.rays_simple`, `sway`, `bob`, `_peasant`.
- Trình vẽ `D` chỉ có `polygon, ellipse, rectangle, line, arc, pieslice, regular_polygon` (không có `rounded_rectangle`). Toạ độ/kích thước ép `int` khi tạo ảnh. Nhân vật: `(d, cx, base, s)`, chân ở `(cx, base)`, cao khoảng `232*s`.
- **Đăng ký cảnh mới ở 4 chỗ:** `REG` trong tệp cảnh + `registry()` ở `scenes_hk.py`; thêm tệp vào `CODE` ở `engine.py`; thêm tên vào `SCENES` ở `studio.py`; thêm nhãn tiếng Việt vào `LABEL` ở `static/studio.html`.
- Xem bảng ảnh tĩnh (`tools/sheet.py`) trước khi dựng. Kiểm tra vật không che mặt nhân vật, nhân vật không bị cắt mép.

## Caption
`exports/<tên>/caption.txt` gồm TikTok (ngắn, vài hashtag), Facebook Reels, bình luận ghim (có câu hỏi). Đổi hook thì cập nhật dòng đầu caption. Số liệu chỉ ghi từ trí nhớ (như năm UNESCO) thì nhắc người dùng tự kiểm tra.

## Sai lầm đã gặp, đừng lặp lại
- Ghi hook vào kịch bản khi người dùng chưa chốt; dùng hook chung chung; viết lại chữ hook mà không giữ đúng với giọng đọc.
- Render/xuất video trước khi người dùng xem khung hình hoặc ảnh chữ bìa.
- Dùng lại nguyên cảnh, một cảnh dài giữ một hình, zoom/lia máy, bìa tĩnh, thanh gươm trên bìa, mascot chìm xuống hoặc nảy.
- Dùng chung một hình người cho nhiều nhân vật; để vật (quả dưa) che mặt nhân vật.
- Lệch nhịp giữa các video (pause khác nhau).
- Ngắt dòng bìa gộp hai màu trong một dòng, hoặc gộp qua chỗ giọng nghỉ.
- Lấy mẫu ảnh chữ bìa quá muộn (các dòng đổi nhanh hơn 0,3 giây; lấy ở `t0+0,1`); ảnh tĩnh cũ vì chưa khởi động lại Studio.
- Hỏi nhiều câu, đề xuất xong lại chờ; nói "xong" khi chưa kiểm tra; đưa sự kiện từ trí nhớ mà không tra nguồn.
- Xóa file của người dùng không được phép; đăng bài thay họ.

## Bẫy kỹ thuật trên máy này (Windows)
- Chạy Python với `PYTHONUTF8=1`. Đường dẫn `D:/idea/...` hoặc `/d/idea/...` trong bash.
- Khởi động lại Studio bằng công cụ PowerShell (chạy `powershell` từ trong bash từng tự kill chính nó). `engine.py` gọi `os.chdir` vào thư mục gốc khi import: dùng đường dẫn tuyệt đối hoặc tính từ gốc.
- Viết nhiều file bằng Write/Edit, không heredoc nhiều file. Sửa chuỗi có xuống dòng trong HTML/JSX bằng Edit, đừng `\n` qua heredoc.
- `from opening_frames import *` ghi đè biến `H`; mỗi tiến trình vẽ giữ LRU 6 cảnh, tối đa 6 tiến trình (16 GB RAM, đừng tăng; thiếu RAM báo `MemoryError`/`BrokenProcessPool`).
- claude-mem có thể báo mất đăng nhập: người dùng cần `/login`; không tự khởi động lại worker.

## Truyện đã làm (đều đã xuất, có caption.txt)
| # | Truyện | Dự án | Nhân vật / cảnh | Hook |
|---|---|---|---|---|
| 1 | Hồ Hoàn Kiếm | `hoan_kiem` | `scenes_hk.py`, `scenes_hk2.py` | Thanh gươm thần của Lê Lợi, rốt cuộc đã đi đâu? |
| 2 | Nỏ thần – Cổ Loa | `no_than` | `chars.py`, `scenes_nt.py` (`nt_`) | Với chiếc nỏ thần của An Dương Vương, Trọng Thủy đã làm gì? |
| 3 | Thánh Gióng | `thanh_giong` | `chars_tg.py`, `scenes_tg.py` (`tg_`) | Tại sao Thánh Gióng đến ba tuổi, mà vẫn chưa biết nói? |
| 4 | Sơn Tinh – Thủy Tinh | `son_tinh` | `chars_st.py`, `scenes_st.py` (`st_`) | Tại sao mỗi năm, Thủy Tinh lại dâng nước đánh Sơn Tinh? |
| 5 | Mai An Tiêm | `mai_an_tiem` | `chars_ma.py`, `scenes_ma.py` (`ma_`) | Mai an tiêm đã nói gì, mà bị vua đày ra đảo hoang? |
6. **Nvidia: CEO từ chức rồi quay lại** (`projects/nvidia_ceo`, dạng tin tức giải thích, nhân vật `src/chars_nv.py`, cảnh `src/scenes_nv.py` tiền tố `nv_`), đã xuất (commit 539bbd0). Hook: "Vì sao CEO Nvidia từ chức rồi quay lại chỉ sau mười một ngày?". Quy tắc cho video tin tức người thật: tra nguồn gốc (thông cáo, CNBC), ghi rõ ai nói (chính thức / có tên / nguồn ẩn danh / cáo buộc chưa xác minh), không khẳng định điều chưa có bằng chứng, không vẽ ai làm điều bị cáo buộc, không đưa người khác bị nhắc trong tin, ghi ngày cập nhật vào caption; nhân vật thật vẽ cắt giấy đơn giản theo trang phục và kiểu tóc người dùng đưa (ảnh tham khảo), không chép khuôn mặt. Ông Huang: tóc bạc chải ngược, kính gọng nửa, áo da đen cổ đứng, tay khoanh, quần dài.
7. **GTA 6: tiền bỏ ra và doanh số ngày đầu** (`projects/gta6`, tin tức giải thích, `src/scenes_g6.py` tiền tố `g6_`, 13 cảnh cắt giấy), đã xuất, commit 1c39bb2. Hook: "GTA 6 tốn hơn một tỷ đô. Ngày đầu bán được bao nhiêu?".
8. **Lừa đảo vòng quay may mắn + "lừa lần hai"** (`projects/scam_wheel`, thể loại kể chuyện thực tế, phong cách mực, `src/scenes_ink.py`, `scenes_sc.py`, `scenes_sc2.py`, `scenes_sc3.py` tiền tố `sc_`; sc3 ghi đè cùng tên trong sc/sc2), đã xuất bản đẹp, chưa commit. KHÔNG có hook/bìa, 10 đoạn, ~73 s. Nguồn: Tuổi Trẻ, CafeF, CAND, Công an Quảng Ngãi/Cần Thơ, Người Quan Sát (xem caption.txt).

## Thể loại "kể chuyện thực tế / cảnh báo lừa đảo" (video 8 trở đi)
- **Vào thẳng nội dung:** không `hook`, không `cover` trong script (engine hỗ trợ: thiếu `hook` thì video bắt đầu ngay ở cảnh 1). Mascot chỉ hiện giữa lời kể nếu cần. Độ dài mục tiêu khoảng 1:10 (≈350 chữ, speed 1.12).
- **Hình khớp từng câu:** viết `shots` thủ công theo từng cụm (`tulinh2.phrases` liệt kê cụm), không dùng autoshots. Mỗi khung một ý đúng lời đang đọc, 1 đến 4 giây, chi tiết vừa đủ, không rối mắt. Màn hình điện thoại: phóng to thành khung bên cạnh nhân vật.
- **Nhân vật (phong cách mực, `ink_figure` trong `scenes_ink.py`):** nửa người, viền đen dày `#14121a`, tô phẳng, đầu ngũ giác, mắt là hai nét đứng ngắn, lông mày nét ngang, miệng một nét. Cảm xúc chỉ bằng lông mày/miệng (calm, worried có giọt mồ hôi, stern, shock, happy). Mỗi vai một nét đặc trưng + một màu: nạn nhân (búi tóc, áo hồng, cầm điện thoại hai tay), kẻ lừa (mũ trùm tối, mặt đen, mắt miệng trắng), nhân viên ngân hàng (áo trắng, cà vạt xanh, tóc nâu), công an (mũ xanh huy hiệu vàng, ria). Nhân vật hoàn toàn hư cấu, không dùng mặt/tên người thật, không nêu danh nạn nhân.
- **Vật thể:** đơn giản, đủ nét đặc trưng (cá chỉ thân + đuôi + vây lưng + mắt). Mọi hình tô phẳng có cùng viền đen: bọc hàm vẽ bằng `InkD(d)` (viền 3 đến 8 px theo cỡ hình; hình rất nhỏ/trong suốt không viền). Không chữ trong hình, không vầng sáng/lấp lánh, ít đồ trang trí.
- **Màu nền: KHÔNG chốt một màu cho mọi video; chọn theo loại nội dung.** Riêng video này nền được pha trắng 86% (`lighten_scene`, biến môi trường `INK_K` đổi mức pha, mặc định 0.86) để viền đen nổi; nội dung khác (đêm, kịch tính, tin tức) có thể dùng nền đậm hơn, nhưng viền đen phải còn đọc được. Hỏi/cho xem ảnh so sánh mức nền trước khi dựng.
- **Quy trình:** xem ảnh tĩnh các cảnh (`tools/sheet.py out/x.png <tên cảnh>`) và được duyệt, rồi mới dựng nháp. Người dùng từng chê: hình quá chung chung/không khớp lời, quá rối, nhân vật xấu/phức tạp, cá xấu, tóc hồng bắt chước mẫu.
- **Chữ trong caption:** ghi nguồn, ngày cập nhật; nhắc nhân vật là minh họa; số liệu thống kê ghi "theo báo chí".
- Các video 6 và 7 (Nvidia, GTA 6) vẫn nền tối kiểu cũ, chưa chuyển sang phong cách mực; chưa có luật cho cảnh toàn thân/đám đông.

Truyện đề xuất tiếp: Chử Đồng Tử – Tiên Dung, bánh chưng bánh giầy (Lang Liêu), Con Rồng cháu Tiên, Ngô Quyền và trận Bạch Đằng (lịch sử, cần tra nguồn kỹ).

## Việc còn mở (làm khi người dùng yêu cầu)
- Thư viện mảnh ghép dùng chung (nền, nhân vật, đồ vật) để truyện sau ít token hơn; hiện mỗi truyện có tệp nhân vật và cảnh riêng.
- Bảng "chữ hiện / chữ đọc" để sửa cách đọc tên trong phần kể; forced alignment để phụ đề khớp từng từ; đo vùng an toàn thật trên điện thoại.
