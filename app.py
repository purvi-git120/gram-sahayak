import streamlit as st

# Page Configuration
st.set_page_config(page_title="Gram Sahayak", page_icon="🌾", layout="centered")

# App Header
st.title("🌾 Gram Sahayak")
st.subheader("Hyper-Local AI Voice & Advisory Assistant for Rural Micro-Entrepreneurs")

# Sidebar for Language and Profile Selection
st.sidebar.header("⚙️ Settings")
language = st.sidebar.selectbox("Select Language", ["English", "Hindi (हिन्दी)", "Kannada (ಕನ್ನಡ)"])
user_location = st.sidebar.selectbox("Select Market Location", ["Hubballi", "Dharwad", "Belagavi", "Bengaluru"])


# Main Navigation Tabs
tab1, tab2, tab3 = st.tabs(["🌾 Market Prices", "🏛️ Government Schemes", "💰 Financial Assistant"])

# ----------------- TAB 1: MARKET PRICES -----------------
with tab1:
    st.header("Local Market Price Lookup")
    st.write("Check real-time or recent wholesale prices for crops in your selected market.")
    
    crop = st.selectbox("Select Crop", ["Tomato", "Onion", "Potato", "Green Chilli"])
    
    if st.button("Check Price"):
        # Mock dataset logic
        prices = {
            "Tomato": {"price": "₹28 / kg", "trend": "📈 Increasing", "market": user_location},
            "Onion": {"price": "₹22 / kg", "trend": "📉 Decreasing", "market": user_location},
            "Potato": {"price": "₹18 / kg", "stable": "Stable", "market": user_location},
            "Green Chilli": {"price": "₹45 / kg", "trend": "📈 Increasing", "market": user_location}
        }
        
        data = prices.get(crop)
        st.success(f"Current price for **{crop}** in **{data['market']}**: **{data['price']}** ({data['trend']})")
        st.caption("Data source: Simulated agricultural market API feed.")

# ----------------- TAB 2: GOVERNMENT SCHEMES -----------------
with tab2:
    st.header("Government Scheme Recommendations")
    st.write("Find out which business or agricultural schemes you qualify for.")
    
    business_type = st.selectbox("Your Business Type", ["Small Vegetable Vendor", "Dairy Farmer", "Handicraft Artisan", "General Retail"])
    
    if st.button("Find Schemes"):
        st.markdown("### Recommended Schemes:")
        if business_type == "Small Vegetable Vendor":
            st.info("🏛️ **PM SVANidhi Scheme**\n\n* **Benefit:** Working capital loan up to ₹10,000 - ₹50,000.\n* **Eligibility:** Street vendors and micro-entrepreneurs.\n* **Next Step:** Visit the nearest common service center (CSC) with your ID card.")
        else:
            st.info("🏛️ **Mudra Loan Scheme (Shishu/Kishor)**\n\n* **Benefit:** Collateral-free loans up to ₹50,000 for micro-business expansion.\n* **Eligibility:** Small business owners.\n* **Next Step:** Apply through any public or private sector bank.")

# ----------------- TAB 3: FINANCIAL ASSISTANT -----------------
with tab3:
    st.header("Business Profit & Calculator")
    st.write("Calculate your expected profit or loan EMI instantly and reliably.")
    
    calc_type = st.radio("Choose Calculator", ["Profit Calculator", "Loan EMI Calculator"])
    
    if calc_type == "Profit Calculator":
        qty = st.number_input("Quantity (in kg/units)", min_value=1.0, value=100.0)
        buy_price = st.number_input("Purchase Cost per unit (₹)", min_value=0.0, value=20.0)
        sell_price = st.number_input("Selling Price per unit (₹)", min_value=0.0, value=30.0)
        
        if st.button("Calculate Profit"):
            total_purchase = qty * buy_price
            total_sales = qty * sell_price
            profit = total_sales - total_purchase
            
            st.write(f"* Total Purchase Cost: ₹{total_purchase}")
            st.write(f"* Total Sales Revenue: ₹{total_sales}")
            if profit >= 0:
                st.success(f"Estimated Profit: **₹{profit}** 🎉")
            else:
                st.error(f"Estimated Loss: **₹{abs(profit)}** ⚠️")
                
    else:
        loan_amt = st.number_input("Loan Amount (₹)", min_value=1000, value=50000)
        interest_rate = st.number_input("Annual Interest Rate (%)", min_value=1.0, value=10.0)
        years = st.number_input("Duration (Years)", min_value=1, value=2)
        
        if st.button("Calculate EMI"):
            r = (interest_rate / 12) / 100
            n = years * 12
            emi = (loan_amt * r * ((1 + r)**n)) / (((1 + r)**n) - 1)
            st.success(f"Approximate Monthly EMI: **₹{round(emi, 2)} per month**")