
import streamlit as st

# Cấu hình trang
st.set_page_config(
    page_title="Ứng dụng tính lãi tiết kiệm",
    page_icon="💰",
    layout="centered"
)

# Tiêu đề ứng dụng
st.title("💰 TÍNH LÃI GỬI TIẾT KIỆM")
st.write("Nhập thông tin khoản tiền gửi để tính toán tiền lãi.")

st.divider()

# Nhập thông tin
st.subheader("📋 Thông tin tiền gửi")

so_tien = st.number_input(
    "Số tiền gửi (VNĐ)",
    min_value=0,
    value=10000000,
    step=1000000,
    format="%d"
)

ky_han = st.number_input(
    "Kỳ hạn gửi (tháng)",
    min_value=1,
    max_value=120,
    value=12,
    step=1
)

lai_suat = st.number_input(
    "Lãi suất (%/năm)",
    min_value=0.0,
    max_value=100.0,
    value=5.0,
    step=0.1,
    format="%.2f"
)

hinh_thuc = st.selectbox(
    "Hình thức nhận lãi",
    [
        "Cuối kỳ",
        "Hàng tháng",
        "Hàng quý"
    ]
)

# Tính toán
if st.button("TÍNH TIỀN LÃI", type="primary", use_container_width=True):

    # Quy đổi lãi suất và thời gian
    lai_suat_nam = lai_suat / 100
    thoi_gian_nam = ky_han / 12

    # Tổng tiền lãi theo lãi đơn
    tong_lai = so_tien * lai_suat_nam * thoi_gian_nam

    # Xác định số kỳ nhận lãi
    if hinh_thuc == "Cuối kỳ":
        so_ky = 1
    elif hinh_thuc == "Hàng tháng":
        so_ky = ky_han
    else:
        so_ky = ky_han / 3

    # Tính lãi định kỳ
    if so_ky > 0:
        lai_dinh_ky = tong_lai / so_ky
    else:
        lai_dinh_ky = 0

    # Tổng tiền gốc và lãi
    tong_nhan = so_tien + tong_lai

    st.divider()
    st.subheader("📊 KẾT QUẢ TÍNH TOÁN")

    # Hiển thị kết quả
    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            label="💵 Tiền lãi định kỳ",
            value=f"{lai_dinh_ky:,.0f} VNĐ"
        )

    with col2:
        st.metric(
            label="📈 Tổng tiền lãi",
            value=f"{tong_lai:,.0f} VNĐ"
        )

    st.success(
        f"💰 Tổng gốc và lãi: {tong_nhan:,.0f} VNĐ"
    )

    # Thông tin chi tiết
    st.write("### Chi tiết khoản gửi")
    st.write(f"- Số tiền gốc: **{so_tien:,.0f} VNĐ**")
    st.write(f"- Kỳ hạn: **{ky_han} tháng**")
    st.write(f"- Lãi suất: **{lai_suat:.2f}%/năm**")
    st.write(f"- Hình thức nhận lãi: **{hinh_thuc}**")

    # Ghi chú
    st.caption(
        "Lưu ý: Kết quả được tính theo lãi đơn, "
        "giả định lãi suất cố định và không tái đầu tư "
        "tiền lãi. Số tiền thực tế có thể khác tùy "
        "theo quy định của ngân hàng."
    )
