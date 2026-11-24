---
name: vn-scam-story-shorts
description: Làm video ngắn kể chuyện thực tế / cảnh báo lừa đảo (không lộ mặt, không bìa, phong cách mực nét đen, nhìn là hiểu) cho TikTok/Facebook Reels trong D:\idea. Dùng khi người dùng muốn làm video lừa đảo/cảnh báo/kể chuyện thời sự mới, vẽ cảnh phong cách mực, hoặc giao việc cho opencode. Kỹ thuật dùng chung (Studio, engine, script.json, giọng, cache) xem skill vn-legend-shorts.
---

# Video kể chuyện thực tế / cảnh báo lừa đảo (D:\idea)

Kỹ thuật chung (chạy Studio, `script.json`, giọng VieNeu, bộ nhớ đệm, đăng ký cảnh ở 4 chỗ, bẫy Windows, quy tắc "người dùng chốt hook", "xem ảnh trước khi dựng", "không đăng bài thay người dùng", "không Co-Authored-By"): **đọc `vn-legend-shorts` trước**. File này chỉ chứa phần riêng của thể loại này. Hướng dẫn giao việc cho opencode: `AGENTS.md`.

## Video đã làm
8. **Lừa đảo vòng quay may mắn + "lừa lần hai"** (`projects/scam_wheel`, thể loại kể chuyện thực tế, phong cách mực, `src/scenes_ink.py`, `scenes_sc.py`, `scenes_sc2.py`, `scenes_sc3.py` tiền tố `sc_`; sc3 ghi đè cùng tên trong sc/sc2), đã xuất bản đẹp, chưa commit. KHÔNG có hook/bìa, 10 đoạn, ~73 s. Nguồn: Tuổi Trẻ, CafeF, CAND, Công an Quảng Ngãi/Cần Thơ, Người Quan Sát (xem caption.txt).

9. **Việc nhẹ lương cao: hai nữ sinh Đà Nẵng bị dụ đi Bắc Kạn** (`projects/scam_job`, cùng thể loại kể chuyện thực tế; cảnh `src/scenes_s9.py` tiền tố `s9_`, nhân vật `girl`/`girl2` trong `ink_figure`), đã xuất. Nguồn: Báo Công an TP Đà Nẵng (21/11/2026), VOV (xem `projects/scam_job/sources.txt`). Làm chủ yếu bằng opencode (xem `AGENTS.md`), Claude kiểm nguồn + xem ảnh. 29 khung/73 s. Bài học: không thêm chi tiết ngoài nguồn; không nêu tên nạn nhân hay tài khoản người dụ.


## Thể loại "kể chuyện thực tế / cảnh báo lừa đảo" (video 8 trở đi)
- **Vào thẳng nội dung:** không `hook`, không `cover` trong script (engine hỗ trợ: thiếu `hook` thì video bắt đầu ngay ở cảnh 1). Mascot chỉ hiện giữa lời kể nếu cần. Độ dài mục tiêu khoảng 1:10 (≈350 chữ, speed 1.12).
- **Nguyên tắc cao nhất: người xem nhìn là HIỂU.** Mỗi khung một vật/hành động to, rõ, đúng câu đang đọc; không chi tiết thừa, không hình trừu tượng/ký hiệu khó đoán, không nhân vật đứng trơ, không đường rời thay tay chân. Nhịp 2 đến 3 giây/khung (≈30 đến 36 khung cho 75 giây).
- **Hình khớp từng câu:** viết `shots` thủ công theo từng cụm (`tulinh2.phrases` liệt kê cụm), không dùng autoshots. Mỗi khung một ý đúng lời đang đọc, 1 đến 4 giây, chi tiết vừa đủ, không rối mắt. Màn hình điện thoại: phóng to thành khung bên cạnh nhân vật.
- **Nhân vật (phong cách mực, `ink_figure` trong `scenes_ink.py`):** nửa người, viền đen dày `#14121a`, tô phẳng, đầu ngũ giác, mắt là hai nét đứng ngắn, lông mày nét ngang, miệng một nét. Cảm xúc chỉ bằng lông mày/miệng (calm, worried có giọt mồ hôi, stern, shock, happy). Mỗi vai một nét đặc trưng + một màu: nạn nhân (búi tóc, áo hồng, cầm điện thoại hai tay), kẻ lừa (mũ trùm tối, mặt đen, mắt miệng trắng), nhân viên ngân hàng (áo trắng, cà vạt xanh, tóc nâu), công an (mũ xanh huy hiệu vàng, ria). Nhân vật hoàn toàn hư cấu, không dùng mặt/tên người thật, không nêu danh nạn nhân.
- **Vật thể:** đơn giản, đủ nét đặc trưng (cá chỉ thân + đuôi + vây lưng + mắt). Mọi hình tô phẳng có cùng viền đen: bọc hàm vẽ bằng `InkD(d)` (viền 3 đến 8 px theo cỡ hình; hình rất nhỏ/trong suốt không viền). Không chữ trong hình, không vầng sáng/lấp lánh, ít đồ trang trí.
- **Màu nền: KHÔNG chốt một màu cho mọi video; chọn theo loại nội dung.** Riêng video này nền được pha trắng 86% (`lighten_scene`, biến môi trường `INK_K` đổi mức pha, mặc định 0.86) để viền đen nổi; nội dung khác (đêm, kịch tính, tin tức) có thể dùng nền đậm hơn, nhưng viền đen phải còn đọc được. Hỏi/cho xem ảnh so sánh mức nền trước khi dựng.
- **Quy trình:** xem ảnh tĩnh các cảnh (`tools/sheet.py out/x.png <tên cảnh>`) và được duyệt, rồi mới dựng nháp. Người dùng từng chê: hình quá chung chung/không khớp lời, quá rối, nhân vật xấu/phức tạp, cá xấu, tóc hồng bắt chước mẫu.
- **Lỗi hình hay gặp (đã sửa ở video 9, đừng lặp lại):** (1) miệng sát viền cằm: mặt nhân vật `girl` vẽ ở y=114, đừng hạ thấp; (2) đoạn thẳng rời làm "tay"/đường nối tay tới màn hình (trông như que xám): hàm `zoom` trong `scenes_s9` là no-op, đừng vẽ tay bằng `d.line`; (3) nhân vật thừa/bị cắt mép khung (kiểm cx và scale: nửa người rộng ≈ 200*scale*0.78 px); (4) hình trừu tượng (cột, bàn, ghim lạ), bong bóng trống, cửa sổ/ba lô/dây trang trí; (5) hai nhân vật cùng mẫu (hai em có `girl` đuôi ngựa cam, `girl2` bob băng đô hồng). Biểu tượng dễ hiểu: gạch chéo đỏ (không được), dấu tích xanh (nên), biển cấm, tam giác cảnh báo, bia ngắm, mũ tốt nghiệp, chồng tiền, ghim vị trí, xe.
- **Nhịp:** khoảng 2,5 giây/khung (29 khung/73 s) vẫn bị chê "nhanh" lúc 36 khung; nếu còn nhanh giảm xuống 22–24 khung.
- **Kiểm tra trước khi dựng:** làm bảng ảnh có ghi lời đọc dưới từng cảnh (đối chiếu từng khung với câu), xem từng ô. Nhiều khung trong ảnh nhỏ vẫn có lỗi (nhân vật cắt mép) nên xem ảnh lớn.
- **Chữ trong caption:** ghi nguồn, ngày cập nhật; nhắc nhân vật là minh họa; số liệu thống kê ghi "theo báo chí".
- Các video 6 và 7 (Nvidia, GTA 6) vẫn nền tối kiểu cũ, chưa chuyển sang phong cách mực; chưa có luật cho cảnh toàn thân/đám đông.

