Đọc AGENTS.md rồi .claude/skills/vn-legend-shorts/SKILL.md (đặc biệt mục "Thể loại kể chuyện thực tế / cảnh báo lừa đảo"). Xem projects/scam_wheel/script.json và texts.json làm mẫu.
Việc: chuẩn bị video thứ 9, cùng thể loại kể chuyện lừa đảo thực tế, MỘT vụ/chiêu khác vòng quay may mắn (ví dụ giả danh công an gọi điện, việc nhẹ lương cao, đầu tư tiền ảo, tình cảm online). Tra web, chỉ dùng nguồn báo chính thống/công an, một vụ có thật được đưa tin, không nêu tên nạn nhân.
Làm đúng các bước sau, KHÔNG làm gì khác:
1. Tạo projects/scam_<ten_ngan>/script.json theo mẫu scam_wheel: KHÔNG có hook/cover, speed 1.12, pause 0.2, 10 đoạn, khoảng 350 chữ (~73 giây), số viết bằng chữ khi có thể, câu ngắn, có đoạn cuối lời khuyên. Chỉ điền "text" từng đoạn (chưa cần scene/shots).
2. Tạo projects/scam_<ten_ngan>/sources.txt: tên vụ, danh sách URL nguồn + ngày, và các số liệu/chi tiết nào chưa chắc (ghi rõ hedged).
3. Tạo projects/scam_<ten_ngan>/scene_plan.md: với mỗi đoạn, liệt kê từng cụm câu (tách tại . , ? ! :) và gợi ý một hình minh họa đơn giản khớp đúng lời cụm đó, theo luật mực (nhân vật: nạn nhân, kẻ lừa, nhân viên, công an; vật thể đơn giản; không chữ trong hình).
Không chạy Studio, không render, không git, không sửa file ngoài thư mục dự án mới, không đăng gì. Trả lời cuối: tên dự án, vụ đã chọn, đường dẫn các file.
