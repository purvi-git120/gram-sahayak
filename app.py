import streamlit as st

# Page Configuration
st.set_page_config(page_title="Gram Sahayak", page_icon="🌾", layout="centered")

# Translation Dictionary (Covers both UI and Outputs for all 3 languages)
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
        "enter_crop_warning": "Please enter a valid vegetable or crop name.",
        "market_source": "Data source: Simulated agricultural market API feed.",
        "price_result": "Current estimated price for **{crop}** in **{location}**: **₹30 / kg** (📈 Increasing)",
        "business_prompt": "Select your business type:",
        "select_business_default": "-- Select --",
        "find_scheme_btn": "Find Schemes",
        "select_business_warning": "Please select your business type.",
        "scheme_pv_title": "🏛️ **PM SVANidhi Scheme**",
        "scheme_pv_benefit": "Benefit: Working capital loan up to ₹10,000 - ₹50,000.",
        "scheme_pv_eligibility": "Eligibility: Street vendors and micro-entrepreneurs.",
        "scheme_pv_step": "Next Step: Visit the nearest common service center (CSC) with your ID card.",
        "scheme_mudra_title": "🏛️ **Mudra Loan Scheme (Shishu/Kishor)**",
        "scheme_mudra_benefit": "Benefit: Collateral-free loans up to ₹50,000 for micro-business expansion.",
        "scheme_mudra_eligibility": "Eligibility: Small business owners.",
        "scheme_mudra_step": "Next Step: Apply through any public or private sector bank.",
        "calc_type": "Choose Calculator",
        "profit_calc": "Profit Calculator",
        "emi_calc": "Loan EMI Calculator",
        "qty_label": "Enter the quantity (in kg/units):",
        "buy_label": "Enter the purchase cost per unit (₹):",
        "sell_label": "Enter the selling price per unit (₹):",
        "calc_profit_btn": "Calculate Profit",
        "calc_warning": "Please enter valid positive numbers for calculation.",
        "total_purchase": "Total Purchase Cost: ₹",
        "total_sales": "Total Sales Revenue: ₹",
        "est_profit": "Estimated Profit: **₹{profit}** 🎉",
        "est_loss": "Estimated Loss: **₹{loss}** ⚠️",
        "loan_label": "Enter the loan amount (₹):",
        "rate_label": "Enter the annual interest rate (%):",
        "years_label": "Enter the duration (Years):",
        "calc_emi_btn": "Calculate EMI",
        "loan_warning": "Please enter valid loan details.",
        "emi_result": "Approximate Monthly EMI: **₹{emi} per month**"
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
        "enter_crop_warning": "कृपया एक वैध सब्जी या फसल का नाम दर्ज करें।",
        "market_source": "डेटा स्रोत: सिम्युलेटेड कृषि बाज़ार एपीआई फ़ीड।",
        "price_result": "**{location}** में **{crop}** का वर्तमान अनुमानित मूल्य: **₹30 / किग्रा** (📈 बढ़ रहा है)",
        "business_prompt": "अपना व्यवसाय प्रकार चुनें:",
        "select_business_default": "-- चुनें --",
        "find_scheme_btn": "योजनाएं खोजें",
        "select_business_warning": "कृपया अपना व्यवसाय प्रकार चुनें।",
        "scheme_pv_title": "🏛️ **पीएम स्वनिधि योजना**",
        "scheme_pv_benefit": "लाभ: ₹10,000 से ₹50,000 तक कार्यशील पूंजी ऋण।",
        "scheme_pv_eligibility": "पात्रता: सड़क विक्रेता और सूक्ष्म उद्यमी।",
        "scheme_pv_step": "अगला कदम: अपने आईडी कार्ड के साथ निकटतम सामान्य सेवा केंद्र (CSC) पर जाएं।",
        "scheme_mudra_title": "🏛️ **मुद्रा लोन योजना (शिशु/किशोर)**",
        "scheme_mudra_benefit": "लाभ: सूक्ष्म-व्यापार विस्तार के लिए ₹50,000 तक संपार्श्विक-मुक्त (collateral-free) ऋण।",
        "scheme_mudra_eligibility": "पात्रता: छोटे व्यवसाय के मालिक।",
        "scheme_mudra_step": "अगला कदम: किसी भी सार्वजनिक या निजी क्षेत्र के बैंक के माध्यम से आवेदन करें।",
        "calc_type": "कैलकुलेटर चुनें",
        "profit_calc": "लाभ कैलकुलेटर",
        "emi_calc": "ऋण ईएमआई कैलकुलेटर",
        "qty_label": "मात्रा दर्ज करें (किग्रा/इकाई में):",
        "buy_label": "प्रति इकाई खरीद लागत दर्ज करें (₹):",
        "sell_label": "प्रति इकाई बिक्री मूल्य दर्ज करें (₹):",
        "calc_profit_btn": "लाभ की गणना करें",
        "calc_warning": "कृपया गणना के लिए वैध सकारात्मक संख्याएं दर्ज करें।",
        "total_purchase": "कुल खरीद लागत: ₹",
        "total_sales": "कुल बिक्री राजस्व: ₹",
        "est_profit": "अनुमानित लाभ: **₹{profit}** 🎉",
        "est_loss": "अनुमानित हानि: **₹{loss}** ⚠️",
        "loan_label": "ऋण राशि दर्ज करें (₹):",
        "rate_label": "वार्षिक ब्याज दर दर्ज करें (%):",
        "years_label": "अवधि दर्ज करें (वर्ष):",
        "calc_emi_btn": "ईएमआई की गणना करें",
        "loan_warning": "कृपया वैध ऋण विवरण दर्ज करें।",
        "emi_result": "अनुमानित मासिक ईएमआई: **₹{emi} प्रति माह**"
    },
    "Kannada (ಕನ್ನಡ)": {
        "title": "🌾 ಗ್ರಾಮ್ ಸಹಾಯಕ",
        "subtitle": "ಗ್ರಾಮೀಣ ಸೂಕ್ಷ್ಮ ಉದ್ಯಮಿಗಳಿಗಾಗಿ ಹೈಪರ್-ಲೋಕಲ್ AI ಧ್ವನಿ ಮತ್ತು ಸಲಹಾ ಸಹಾಯಕ",
        "settings": "⚙️ ಸೆಟ್ಟಿಂಗ್‌ಗಳು",
        "lang_label": "ಭಾಷೆಯನ್ನು ಆಯ್ಕೆಮಾಡಿ",
        "market_loc": "ಮಾರುಕಟ್ಟೆ ಸ್ಥಳವನ್ನು ಆಯ್ಕೆಮಾಡಿ",
        "tab1": "🌾 ಮಾರುಕಟ್ಟೆ ಬೆಲೆಗಳು",
        "tab2": "🏛️ ಸರ್ಕಾರಿ ಯೋಜನೆಗಳು",
        "tab3": "💰 ಹಣಕಾಸು ಸಹಾಯಕ",
        "crop_prompt": "ತರಕಾರಿ ಅಥವಾ ಬೆಳೆಯ ಹೆಸರನ್ನು ನಮೂದಿಸಿ:",
        "crop_placeholder": "ಉದಾ: ಟೊಮೆಟೊ, ಈರುಳ್ಳಿ...",
        "check_btn": "ಬೆಲೆ ಪರಿಶೀಲಿಸಿ",
        "enter_crop_warning": "ದಯವಿಟ್ಟು ಸರಿಯಾದ ತರಕಾರಿ ಅಥವಾ ಬೆಳೆಯ ಹೆಸರನ್ನು ನಮೂದಿಸಿ.",
        "market_source": "ಡೇಟಾ ಮೂಲ: ಸಿಮ್ಯುಕೇಟೆಡ್ ಕೃಷಿ ಮಾರುಕಟ್ಟೆ API ಫೀಡ್.",
        "price_result": "**{location}** ನಲ್ಲಿ **{crop}** ನ ಪ್ರಸ್ತುತ ಅಂದಾಜು ಬೆಲೆ: **₹30 / ಕೆಜಿ** (📈 ಹೆಚ್ಚುತ್ತಿದೆ)",
        "business_prompt": "ನಿಮ್ಮ ವ್ಯಾಪಾರದ ಪ್ರಕಾರವನ್ನು ಆಯ್ಕೆಮಾಡಿ:",
        "select_business_default": "-- ಆಯ್ಕೆಮಾಡಿ --",
        "find_scheme_btn": "ಯೋಜನೆಗಳನ್ನು ಹುಡುಕಿ",
        "select_business_warning": "ದಯವಿಟ್ಟು ನಿಮ್ಮ ವ್ಯಾಪಾರದ ಪ್ರಕಾರವನ್ನು ಆಯ್ಕೆಮಾಡಿ.",
        "scheme_pv_title": "🏛️ **ಪಿಎಂ ಸ್ವನಿಧಿ ಯೋಜನೆ**",
        "scheme_pv_benefit": "ಪ್ರಯೋಜನ: ₹10,000 ರಿಂದ ₹50,000 ರವರೆಗೆ ಕಾರ್ಯಂಡದ ಸಾಲ.",
        "scheme_pv_eligibility": "ಅರ್ಹತೆ: ಬೀದಿ ವ್ಯಾಪಾರಿಗಳು ಮತ್ತು ಸೂಕ್ಷ್ಮ ಉದ್ಯಮಿಗಳು.",
        "scheme_pv_step": "ಮುಂದಿನ ಹಂತ: ನಿಮ್ಮ ಐಡಿ ಕಾರ್ಡ್‌ನೊಂದಿಗೆ ಹತ್ತಿರದ ಸಾಮಾನ್ಯ ಸೇವಾ ಕೇಂದ್ರಕ್ಕೆ (CSC) ಭೇಟಿ ನೀಡಿ.",
        "scheme_mudra_title": "🏛️ **ಮುದ್ರಾ ಸಾಲ ಯೋಜನೆ (ಶಿಶು/ಕಿಶೋರ್)**",
        "scheme_mudra_benefit": "ಪ್ರಯೋಜನ: ಸಣ್ಣ ವ್ಯಾಪಾರ ವಿಸ್ತರಣೆಗಾಗಿ ₹50,000 ರವರೆಗೆ ಮೇಲಾಧಾರರಹಿತ ಸಾಲ.",
        "scheme_mudra_eligibility": "ಅರ್ಹತೆ: ಸಣ್ಣ ವ್ಯಾಪಾರ ಮಾಲೀಕರು.",
        "scheme_mudra_step": "ಮುಂದಿನ ಹಂತ: ಯಾವುದೇ ಸಾರ್ವಜನಿಕ ಅಥವಾ ಖಾಸಗಿ ವಲಯದ ಬ್ಯಾಂಕ್ ಮೂಲಕ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ.",
        "calc_type": "ಕ್ಯಾಲ್ಕುಲೇಟರ್ ಅನ್ನು ಆಯ್ಕೆಮಾಡಿ",
        "profit_calc": "ಲಾಭ ಕ್ಯಾಲ್ಕುಲೇಟರ್",
        "emi_calc": "ಸಾಲದ EMI ಕ್ಯಾಲ್ಕುಲೇಟರ್",
        "qty_label": "ಪ್ರಮಾಣವನ್ನು ನಮೂದಿಸಿ (ಕೆಜಿ/ಘಟಕಗಳಲ್ಲಿ):",
        "buy_label": "ಪ್ರತಿ ಘಟಕಕ್ಕೆ ಖರೀದಿ ವೆಚ್ಚವನ್ನು ನಮೂದಿಸಿ (₹):",
        "sell_label": "ಪ್ರತಿ ಘಟಕಕ್ಕೆ ಮಾರಾಟ ಬೆಲೆಯನ್ನು ನಮೂದಿಸಿ (₹):",
        "calc_profit_btn": "ಲಾಭವನ್ನು ಲೆಕ್ಕಹಾಕಿ",
        "calc_warning": "ದಯವಿಟ್ಟು ಲೆಕ್ಕಾಚಾರಕ್ಕಾಗಿ ಮಾನ್ಯವಾದ ಧನಾತ್ಮಕ ಸಂಖ್ಯೆಗಳನ್ನು ನಮೂದಿಸಿ.",
        "total_purchase": "ಒಟ್ಟು ಖರೀದಿ ವೆಚ್ಚ: ₹",
        "total_sales": "ಒಟ್ಟು ಮಾರಾಟ ಆದಾಯ: ₹",
        "est_profit": "ಅಂದಾಜು ಲಾಭ: **₹{profit}** 🎉",
        "est_loss": "ಅಂದಾಜು ನಷ್ಟ: **₹{loss}** ⚠️",
        "loan_label": "ಸಾಲದ ಮೊತ್ತವನ್ನು ನಮೂದಿಸಿ (₹):",
        "rate_label": "ವಾರ್ಷಿಕ ಬಡ್ಡಿ ದರವನ್ನು ನಮೂದಿಸಿ (%):",
        "years_label": "ಅವಧಿಯನ್ನು ನಮೂದಿಸಿ (ವರ್ಷಗಳು):",
        "calc_emi_btn": "EMI ಲೆಕ್ಕಹಾಕಿ",
        "loan_warning": "ದಯವಿಟ್ಟು ಮಾನ್ಯವಾದ ಸಾಲದ ವಿವರಗಳನ್ನು ನಮೂದಿಸಿ.",
        "emi_result": "ಅಂದಾಜು ಮಾಸಿಕ EMI: **₹{emi} ಪ್ರತಿ ತಿಂಗಳು**"
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
            st.warning(t["enter_crop_warning"])
        else:
            formatted_price = t["price_result"].format(crop=crop_input.capitalize(), location=user_location)
            st.success(formatted_price)
            st.caption(t["market_source"])

# ----------------- TAB 2: GOVERNMENT SCHEMES -----------------
with tab2:
    st.header(t["tab2"])
    st.write("Find out which business or agricultural schemes you qualify for.")
    
    business_type = st.selectbox(t["business_prompt"], [t["select_business_default"], "Small Vegetable Vendor", "Dairy Farmer", "Handicraft Artisan", "General Retail"])
    
    if st.button(t["find_scheme_btn"]):
        if business_type == t["select_business_default"]:
            st.warning(t["select_business_warning"])
        elif business_type == "Small Vegetable Vendor":
            st.info(f"{t['scheme_pv_title']}\n\n* **{t['scheme_pv_benefit']}**\n* **{t['scheme_pv_eligibility']}**\n* **{t['scheme_pv_step']}**")
        else:
            st.info(f"{t['scheme_mudra_title']}\n\n* **{t['scheme_mudra_benefit']}**\n* **{t['scheme_mudra_eligibility']}**\n* **{t['scheme_mudra_step']}**")

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
                st.warning(t["calc_warning"])
            else:
                total_purchase = qty * buy_price
                total_sales = qty * sell_price
                profit = total_sales - total_purchase
                
                st.write(f"* {t['total_purchase']}{total_purchase}")
                st.write(f"* {t['total_sales']}{total_sales}")
                if profit >= 0:
                    st.success(t["est_profit"].format(profit=profit))
                else:
                    st.error(t["est_loss"].format(loss=abs(profit)))
                
    else:
        loan_amt = st.number_input(t["loan_label"], min_value=0.0, value=0.0, step=1000.0)
        interest_rate = st.number_input(t["rate_label"], min_value=0.0, value=0.0, step=0.5)
        years = st.number_input(t["years_label"], min_value=0.0, value=0.0, step=1.0)
        
        if st.button(t["calc_emi_btn"]):
            if loan_amt <= 0 or interest_rate <= 0 or years <= 0:
                st.warning(t["loan_warning"])
            else:
                r = (interest_rate / 12) / 100
                n = years * 12
                emi = (loan_amt * r * ((1 + r)**n)) / (((1 + r)**n) - 1)
                st.success(t["emi_result"].format(emi=round(emi, 2)))
