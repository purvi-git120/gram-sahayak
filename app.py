import streamlit as st

# Page Configuration
st.set_page_config(page_title="Gram Sahayak", page_icon="🌾", layout="centered")

# Translation Dictionary for Multi-language Support
translations = {
    "English": {
        "title": "🌾 Gram Sahayak",
        "subtitle": "Hyper-Local AI Voice & Advisory Assistant for Rural Micro-Entrepreneurs",
        "settings": "⚙️ Settings",
        "lang_label": "Select Language",
        "market_loc": "Select Market Location",
        "tab1": "🌾 Market Prices",
        "tab2": "🏛️ Government Schemes",
        "tab3": "💰 Financial Assistant",
        "crop_prompt": "Enter the vegetable or crop name:",
        "crop_placeholder": "e.g., Tomato, Onion...",
        "check_btn": "Check Price",
        "business_prompt": "Select your business type:",
        "find_scheme_btn": "Find Schemes",
        "calc_type": "Choose Calculator",
        "profit_calc": "Profit Calculator",
        "emi_calc": "Loan EMI Calculator",
        "qty_label": "Enter the quantity (in kg/units):",
        "buy_label": "Enter the purchase cost per unit (₹):",
        "sell_label": "Enter the selling price per unit (₹):",
        "calc_profit_btn": "Calculate Profit",
        "loan_label": "Enter the loan amount (₹):",
        "rate_label": "Enter the annual interest rate (%):",
        "years_label": "Enter the duration (Years):",
        "calc_emi_btn": "Calculate EMI"
    },
    "Hindi (हिन्दी)": {
        "title": "🌾 ग्राम सहायक",
        "subtitle": "ग्रामीण सूक्ष्म-उद्यमियों के लिए हाइपर-लोकल एआई वॉयस और सलाहकार सहायक",
        "settings": "⚙️ सेटिंग्स",
        "lang_label": "भाषा चुनें",
        "market_loc": "बाज़ार स्थान चुनें",
        "tab1": "🌾 बाज़ार भाव",
        "tab2": "🏛️ सरकारी योजनाएं",
        "tab3": "💰 वित्तीय सहायक",
        "crop_prompt": "सब्जी या फसल का नाम दर्ज करें:",
        "crop_placeholder": "जैसे: टमाटर, प्याज...",
        "check_btn": "मूल्य जांचें",
        "business_prompt": "अपना व्यवसाय प्रकार चुनें:",
        "find_scheme_btn": "योजनाएं खोजें",
        "calc_type": "कैलकुलेटर चुनें",
        "profit_calc": "लाभ कैलकुलेटर",
        "emi_calc": "ऋण ईएमआई कैलकुलेटर",
        "qty_label": "मात्रा दर्ज करें (किग्रा/इकाई में):",
        "buy_label": "प्रति इकाई खरीद लागत दर्ज करें (₹):",
        "sell_label": "प्रति इकाई बिक्री मूल्य दर्ज करें (₹):",
        "calc_profit_btn": "लाभ की गणना करें",
        "loan_label": "ऋण राशि दर्ज करें (₹):",
        "rate_label": "वार्षिक ब्याज दर दर्ज करें (%):",
        "years_label": "अवधि दर्ज करें (वर्ष):",
        "calc_emi_btn": "ईएमआई की गणना करें"
    },
    "Kannada (ಕನ್ನಡ)": {
        "title": "🌾 ಗ್ರಾಮ್ ಸಹಾಯಕ",
        "subtitle": "ग्रामीण ಸೂಕ್ಷ್ಮ ಉದ್ಯಮಿಗಳಿಗಾಗಿ ಹೈಪರ್-ಲೋಕಲ್ AI ಧ್ವನಿ ಮತ್ತು ಸಲಹಾ ಸಹಾಯಕ",
        "settings": "⚙️ ಸೆಟ್ಟಿಂಗ್‌ಗಳು",
        "lang_label": "ಭಾಷೆಯನ್ನು ಆಯ್ಕೆಮಾಡಿ",
        "market_loc": "ಮಾರುಕಟ್ಟೆ ಸ್ಥಳವನ್ನು ಆಯ್ಕೆಮಾಡಿ",
        "tab1": "🌾 ಮಾರುಕಟ್ಟೆ ಬೆಲೆಗಳು",
        "tab2": "🏛️ ಸರ್ಕಾರಿ ಯೋಜನೆಗಳು",
        "tab3": "💰 ಹಣಕಾಸು ಸಹಾಯಕ",
        "crop_prompt": "ತರಕಾರಿ ಅಥವಾ ಬೆಳೆಯ ಹೆಸರನ್ನು ನಮೂದಿಸಿ:",
        "crop_placeholder": "ಉದಾ: ಟೊಮೆಟೊ, ಈರುಳ್ಳಿ...",
        "check_btn": "ಬೆಲೆ ಪರಿಶೀಲಿಸಿ",
        "business_prompt": "ನಿಮ್ಮ ವ್ಯಾಪಾರದ ಪ್ರಕಾರವನ್ನು ಆಯ್ಕೆಮಾಡಿ:",
        "find_scheme_btn": "ಯೋಜನೆಗಳನ್ನು ಹುಡುಕಿ",
        "calc_type": "ಕ್ಯಾಲ್ಕುಲೇಟರ್ ಅನ್ನು ಆಯ್ಕೆಮಾಡಿ",
        "profit_calc": "ಲಾಭ ಕ್ಯಾಲ್ಕುಲೇಟರ್",
        "emi_calc": "ಸಾಲದ EMI ಕ್ಯಾಲ್ಕುಲೇಟರ್",
        "qty_label": "ಪ್ರಮಾಣವನ್ನು ನಮೂದಿಸಿ (ಕೆಜಿ/ಘಟಕಗಳಲ್ಲಿ):",
        "buy_label": "ಪ್ರತಿ ಘಟಕಕ್ಕೆ ಖರೀದಿ ವೆಚ್ಚವನ್ನು ನಮೂದಿಸಿ (₹):",
        "sell_label": "ಪ್ರತಿ ಘಟಕಕ್ಕೆ ಮಾರಾಟ ಬೆಲೆಯನ್ನು ನಮೂದಿಸಿ (₹):",
        "calc_profit_btn": "ಲಾಭವನ್ನು ಲೆಕ್ಕಹಾಕಿ",
        "loan_label": "ಸಾಲದ ಮೊತ್ತವನ್ನು ನಮೂದಿಸಿ (₹):",
        "rate_label": "ವಾರ್ಷಿಕ ಬಡ್ಡಿ ದರವನ್ನು ನಮೂದಿಸಿ (%):",
        "years_label": "ಅವಧಿಯನ್ನು ನಮೂದಿಸಿ (ವರ್ಷಗಳು):",
        "calc_emi_btn": "EMI ಲೆಕ್ಕಹಾಕಿ"
    }
}

# Sidebar for Language and Profile Selection
st.sidebar.header(translations["English"]["settings"])
language = st.sidebar.selectbox("Select Language", ["English", "Hindi (हिन्दी)", "Kannada (ಕನ್ನಡ)"])
t = translations[language]  # Load text dictionary based on language choice

user_location = st.sidebar.selectbox(t["market_loc"], ["Hubballi", "Dharwad", "Belagavi", "Bengaluru"])


# App Header using translated strings
st.title(t["title"])
st.subheader(t["subtitle"])

# Main Navigation Tabs
tab1, tab2, tab3 = st.tabs([t["tab1"], t["tab2"], t["tab3"]])

# ----------------- TAB 1: MARKET PRICES -----------------
with tab1:
    st.header(t["tab1"])
    st.write("Check wholesale prices for crops in your selected market.")
    
    crop_input = st.text_input(t["crop_prompt"], placeholder=t["crop_placeholder"])
    
    if st.button(t["check_btn"]):
        if not crop_input.strip():
            st.warning("Please enter a valid vegetable or crop name.")
        else:
            st.success(f"Current estimated price for **{crop_input.capitalize()}** in **{user_location}**: **₹30 / kg** (📈 Increasing)")
            st.caption("Data source: Simulated agricultural market API feed.")

# ----------------- TAB 2: GOVERNMENT SCHEMES -----------------
with tab2:
    st.header(t["tab2"])
    st.write("Find out which business or agricultural schemes you qualify for.")
    
    business_type = st.selectbox(t["business_prompt"], ["-- Select --", "Small Vegetable Vendor", "Dairy Farmer", "Handicraft Artisan", "General Retail"])
    
    if st.button(t["find_scheme_btn"]):
        if business_type == "-- Select --":
            st.warning("Please select your business type.")
        elif business_type == "Small Vegetable Vendor":
            st.info("🏛️ **PM SVANidhi Scheme**\n\n* **Benefit:** Working capital loan up to ₹10,000 - ₹50,000.\n* **Eligibility:** Street vendors and micro-entrepreneurs.\n* **Next Step:** Visit the nearest common service center (CSC) with your ID card.")
        else:
            st.info("🏛️ **Mudra Loan Scheme (Shishu/Kishor)**\n\n* **Benefit:** Collateral-free loans up to ₹50,000 for micro-business expansion.\n* **Eligibility:** Small business owners.\n* **Next Step:** Apply through any public or private sector bank.")

# ----------------- TAB 3: FINANCIAL ASSISTANT -----------------
with tab3:
    st.header(t["tab3"])
    st.write("Calculate your expected profit or loan EMI instantly.")
    
    calc_type = st.radio(t["calc_type"], [t["profit_calc"], t["emi_calc"]])
    
    if calc_type == t["profit_calc"]:
        qty = st.number_input(t["qty_label"], min_value=0.0, value=0.0, step=1.0)
        buy_price = st.number_input(t["buy_label"], min_value=0.0, value=0.0, step=1.0)
        sell_price = st.number_input(t["sell_label"], min_value=0.0, value=0.0, step=1.0)
        
        if st.button(t["calc_profit_btn"]):
            if qty <= 0 or buy_price <= 0 or sell_price <= 0:
                st.warning("Please enter valid positive numbers for calculation.")
            else:
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
        loan_amt = st.number_input(t["loan_label"], min_value=0.0, value=0.0, step=1000.0)
        interest_rate = st.number_input(t["rate_label"], min_value=0.0, value=0.0, step=0.5)
        years = st.number_input(t["years_label"], min_value=0.0, value=0.0, step=1.0)
        
        if st.button(t["calc_emi_btn"]):
            if loan_amt <= 0 or interest_rate <= 0 or years <= 0:
                st.warning("Please enter valid loan details.")
            else:
                r = (interest_rate / 12) / 100
                n = years * 12
                emi = (loan_amt * r * ((1 + r)**n)) / (((1 + r)**n) - 1)
                st.success(f"Approximate Monthly EMI: **₹{round(emi, 2)} per month**")
