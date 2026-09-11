import streamlit as st

# Page Configuration
st.set_page_config(page_title="Gram Sahayak", page_icon="🌾", layout="centered")

# Custom styling for clean cards and dark theme compatibility
st.markdown("""
    <style>
    .market-card {
        background-color: #ffffff;
        color: #0f172a;
        border-radius: 1rem;
        padding: 1.25rem;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        height: 100%;
    }
    .card-title {
        color: #0f172a !important;
        font-weight: 700;
        font-size: 1.25rem;
    }
    .card-category {
        color: #4b5563 !important;
        font-size: 0.875rem;
        font-weight: 500;
    }
    .card-price {
        color: #1f2937 !important;
        font-weight: 800;
        font-size: 1.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# ============================================================
# UNIFIED MASTER TRANSLATION DICTIONARY
# ============================================================
translations = {
    "English": {
        # General & Sidebar
        "title": "🌾 Gram Sahayak",
        "subtitle": "Hyper-Local AI Voice & Advisory Assistant for Rural Micro-Entrepreneurs",
        "settings": "⚙️ Settings",
        "lang_label": "Select Language",
        "market_loc": "Select Market Location",
        "tab1": "🌾 Market Prices",
        "tab2": "🏛️ Government Schemes",
        "tab3": "💰 Financial Assistant",
        
        # Tab 1: Market Prices
        "market_desc": "Check wholesale prices for crops in your selected market.",
        "crop_prompt": "Enter the vegetable or crop name:",
        "crop_placeholder": "e.g., Tomato, Onion...",
        "check_btn": "Check Price",
        "enter_crop_warning": "Please enter a valid vegetable or crop name.",
        "market_source": "Data source: Simulated agricultural market API feed.",
        "price_result": "Current estimated price for **{crop}** in **{location}**: **₹30 / kg** (📈 Increasing)",
        "board_header": "🧺 Crop Market Board",
        "board_sub": "Showing crops for the selected demonstration market: {location}",
        "veg": "Vegetable",
        "increasing": "📈 Increasing",
        "stable": "➡️ Stable",
        
        # Tab 2: Government Schemes
        "schemes_desc": "Find out which business or agricultural schemes you qualify for.",
        "search_schemes": "🔎 Search Schemes",
        "search_placeholder": "e.g., loan, subsidy, vendor, food...",
        "no_schemes": "No matching schemes found. Try searching with a different keyword.",
        "scheme_note": "Note: Scheme rules, eligibility criteria, and financial caps are subject to government guidelines. Verify details with local branch offices or common service centers (CSCs) before applying.",
        
        # Tab 3: Financial Assistant
        "finance_title": "Financial Assistant",
        "profit_tab": "📊 Profit Estimator",
        "emi_tab": "🏦 Loan EMI Calculator",
        "profit_est": "Profit Estimation Calculator",
        "quantity": "Quantity Sold",
        "purchase": "Purchase Price per Unit",
        "selling": "Selling Price per Unit",
        "other": "Other/Operational Costs",
        "total_cost": "Total Cost",
        "revenue": "Total Revenue",
        "profit": "Net Profit",
        "positive": "Great! Your business model shows a net profit.",
        "break_even": "You are at a break-even point (No profit, no loss).",
        "loss": "Warning: Your current pricing results in a loss.",
        "loan": "Loan Amount (₹)",
        "rate": "Annual Interest Rate (%)",
        "period": "Loan Period (Years)",
        "monthly": "Monthly EMI",
        "total_payment": "Total Payment",
        "interest": "Total Interest Payable",
        "loan_note": "Note: Actual loan terms, processing fees, and interest calculations may vary depending on bank policies and individual credit assessments."
    },
    "Hindi (हिन्दी)": {
        # General & Sidebar
        "title": "🌾 ग्राम सहायक",
        "subtitle": "ग्रामीण सूक्ष्म-उद्यमियों के लिए हाइपर-लोकल एआई वॉयस और सलाहकार सहायक",
        "settings": "⚙️ सेटिंग्स",
        "lang_label": "भाषा चुनें",
        "market_loc": "बाज़ार स्थान चुनें",
        "tab1": "🌾 बाज़ार भाव",
        "tab2": "🏛️ सरकारी योजनाएं",
        "tab3": "💰 वित्तीय सहायक",
        
        # Tab 1: Market Prices
        "market_desc": "अपने चयनित बाज़ार में फसलों के थोक मूल्य की जाँच करें।",
        "crop_prompt": "सब्जी या फसल का नाम दर्ज करें:",
        "crop_placeholder": "जैसे: टमाटर, प्याज...",
        "check_btn": "मूल्य जांचें",
        "enter_crop_warning": "कृपया एक वैध सब्जी या फसल का नाम दर्ज करें।",
        "market_source": "डेटा स्रोत: सिम्युलेटेड कृषि बाज़ार एपीआई फ़ीड।",
        "price_result": "**{location}** में **{crop}** का वर्तमान अनुमानित मूल्य: **₹30 / किग्रा** (📈 बढ़ रहा है)",
        "board_header": "🧺 फसल बाज़ार बोर्ड",
        "board_sub": "चयनित प्रदर्शन बाज़ार के लिए फसलें दिखाई जा रही हैं: {location}",
        "veg": "सब्जी",
        "increasing": "📈 बढ़ रहा है",
        "stable": "➡️ स्थिर",
        
        # Tab 2: Government Schemes
        "schemes_desc": "पता करें कि आप किस व्यवसाय या कृषि योजना के पात्र हैं।",
        "search_schemes": "🔎 योजनाएं खोजें",
        "search_placeholder": "जैसे: ऋण, सब्सिडी, वेंडर, खाद्य...",
        "no_schemes": "कोई मेल खाने वाली योजना नहीं मिली। किसी अन्य कीवर्ड के साथ खोजें।",
        "scheme_note": "नोट: योजना के नियम, पात्रता मानदंड और वित्तीय सीमाएं सरकारी दिशानिर्देशों के अधीन हैं। आवेदन करने से पहले स्थानीय शाखा कार्यालयों या सामान्य सेवा केंद्रों (CSC) से विवरण सत्यापित करें।",
        
        # Tab 3: Financial Assistant
        "finance_title": "वित्तीय सहायक",
        "profit_tab": "📊 लाभ अनुमानक",
        "emi_tab": "🏦 ऋण ईएमआई कैलकुलेटर",
        "profit_est": "लाभ अनुमान कैलकुलेटर",
        "quantity": "बेची गई मात्रा",
        "purchase": "प्रति यूनिट खरीद मूल्य",
        "selling": "प्रति यूनिट बिक्री मूल्य",
        "other": "अन्य/परिचालन लागत",
        "total_cost": "कुल लागत",
        "revenue": "कुल राजस्व",
        "profit": "शुद्ध लाभ",
        "positive": "बढ़िया! आपका व्यवसाय मॉडल शुद्ध लाभ दिखा रहा है।",
        "break_even": "आप सम-विच्छेद बिंदु पर हैं (न लाभ, न हानि)।",
        "loss": "चेतावनी: आपकी वर्तमान कीमत से नुकसान हो रहा है।",
        "loan": "ऋण राशि (₹)",
        "rate": "वार्षिक ब्याज दर (%)",
        "period": "ऋण अवधि (वर्ष)",
        "monthly": "मासिक ईएमआई",
        "total_payment": "कुल भुगतान",
        "interest": "देय कुल ब्याज",
        "loan_note": "नोट: बैंक नीतियों के आधार पर वास्तविक ऋण शर्तें बदल सकती हैं।"
    },
    "Kannada (ಕನ್ನಡ)": {
        # General & Sidebar
        "title": "🌾 ಗ್ರಾಮ್ ಸಹಾಯಕ",
        "subtitle": "ಗ್ರಾಮೀಣ ಸೂಕ್ಷ್ಮ ಉದ್ಯಮಿಗಳಿಗಾಗಿ ಹೈಪರ್-ಲೋಕಲ್ AI ಧ್ವನಿ ಮತ್ತು ಸಲಹಾ ಸಹಾಯಕ",
        "settings": "⚙️ ಸೆಟ್ಟಿಂಗ್‌ಗಳು",
        "lang_label": "ಭಾಷೆಯನ್ನು ಆಯ್ಕೆಮಾಡಿ",
        "market_loc": "ಮಾರುಕಟ್ಟೆ ಸ್ಥಳವನ್ನು ಆಯ್ಕೆಮಾಡಿ",
        "tab1": "🌾 ಮಾರುಕಟ್ಟೆ ಬೆಲೆಗಳು",
        "tab2": "🏛️ ಸರ್ಕಾರಿ ಯೋಜನೆಗಳು",
        "tab3": "💰 ಹಣಕಾಸು ಸಹಾಯಕ",
        
        # Tab 1: Market Prices
        "market_desc": "ನಿಮ್ಮ ಆಯ್ಕೆಯ ಮಾರುಕಟ್ಟೆಯಲ್ಲಿ ಬೆಳೆಗಳ ಸಗಟು ಬೆಲೆಗಳನ್ನು ಪರಿಶೀಲಿಸಿ.",
        "crop_prompt": "ತರಕಾರಿ ಅಥವಾ ಬೆಳೆಯ ಹೆಸರನ್ನು ನಮೂದಿಸಿ:",
        "crop_placeholder": "ಉದಾ: ಟೊಮೆಟೊ, ಈರುಳ್ಳಿ...",
        "check_btn": "ಬೆಲೆ ಪರಿಶೀಲಿಸಿ",
        "enter_crop_warning": "ದಯವಿಟ್ಟು ಸರಿಯಾದ ತರಕಾರಿ ಅಥವಾ ಬೆಳೆಯ ಹೆಸರನ್ನು ನಮೂದಿಸಿ.",
        "market_source": "ಡೇಟಾ ಮೂಲ: ಸಿಮ್ಯುಕೇಟೆಡ್ ಕೃಷಿ ಮಾರುಕಟ್ಟೆ API ಫೀಡ್.",
        "price_result": "**{location}** ನಲ್ಲಿ **{crop}** ನ ಪ್ರಸ್ತುತ ಅಂದಾಜು ಬೆಲೆ: **₹30 / ಕೆಜಿ** (📈 ಹೆಚ್ಚುತ್ತಿದೆ)",
        "board_header": "🧺 ಬೆಳೆ ಮಾರುಕಟ್ಟೆ ಮಂಡಳಿ",
        "board_sub": "ಆಯ್ಕೆಮಾಡಿದ ಪ್ರದರ್ಶನ ಮಾರುಕಟ್ಟೆಗಾಗಿ ಬೆಳೆಗಳನ್ನು ತೋರಿಸಲಾಗುತ್ತಿದೆ: {location}",
        "veg": "ತರಕಾರಿ",
        "increasing": "📈 ಹೆಚ್ಚುತ್ತಿದೆ",
        "stable": "➡️ ಸ್ಥಿರ",
        
        # Tab 2: Government Schemes
        "schemes_desc": "ನೀವು ಯಾವ ವ್ಯವಹಾರ ಅಥವಾ ಕೃಷಿ ಯೋಜನೆಗೆ ಅರ್ಹರಾಗಿದ್ದೀರಿ ಎಂಬುದನ್ನು ತಿಳಿದುಕೊಳ್ಳಿ.",
        "search_schemes": "🔎 ಯೋಜನೆಗಳನ್ನು ಹುಡುಕಿ",
        "search_placeholder": "ಉದಾ: ಸಾಲ, ಸಬ್ಸಿಡಿ, ಮಾರಾಟಗಾರ, ಆಹಾರ...",
        "no_schemes": "ಯಾವುದೇ ಹೊಂದಾಣಿಕೆಯ ಯೋಜನೆಗಳು ಕಂಡುಬಂದಿಲ್ಲ. ಬೇರೆ ಕೀವರ್ಡ್‌ನೊಂದಿಗೆ ಹುಡುಕಿ.",
        "scheme_note": "ಗಮನಿಸಿ: ಯೋಜನೆಯ ನಿಯಮಗಳು ಮತ್ತು ಅರ್ಹತಾ ಮಾನದಂಡಗಳು ಸರ್ಕಾರದ ಮಾರ್ಗಸೂಚಿಗಳಿಗೆ ಒಳಪಟ್ಟಿರುತ್ತವೆ. ಅರ್ಜಿ ಸಲ್ಲಿಸುವ ಮೊದಲು ಹತ್ತಿರದ ಶಾಖೆ ಅಥವಾ ಸಾಮಾನ್ಯ ಸೇವಾ ಕೇಂದ್ರಗಳಲ್ಲಿ (CSC) ವಿವರಗಳನ್ನು ಪರಿಶೀಲಿಸಿ.",
        
        # Tab 3: Financial Assistant
        "finance_title": "ಹಣಕಾಸು ಸಹಾಯಕ",
        "profit_tab": "📊 ಲಾಭ ಅಂದಾಜು",
        "emi_tab": "🏦 ಸಾಲ ಇಎಂಐ ಕ್ಯಾಲ್ಕುಲೇಟರ್",
        "profit_est": "ಲಾಭ ಅಂದಾಜು ಕ್ಯಾಲ್ಕುಲೇಟರ್",
        "quantity": "ಮಾರಾಟವಾದ ಪ್ರಮಾಣ",
        "purchase": "ಪ್ರತಿ ಘಟಕಕ್ಕೆ ಖರೀದಿ ಬೆಲೆ",
        "selling": "ಪ್ರತಿ ಘಟಕಕ್ಕೆ ಮಾರಾಟ ಬೆಲೆ",
        "other": "ಇತರ/ಕಾರ್ಯಾಚರಣೆ ವೆಚ್ಚಗಳು",
        "total_cost": "ಒಟ್ಟು ವೆಚ್ಚ",
        "revenue": "ಒಟ್ಟು ಆದಾಯ",
        "profit": "ನಿವ್ವಳ ಲಾಭ",
        "positive": "ಅದ್ಭುತ! ನಿಮ್ಮ ವ್ಯವಹಾರ ಮಾದರಿಯು ನಿವ್ವಳ ಲಾಭವನ್ನು ತೋರಿಸುತ್ತಿದೆ.",
        "break_even": "ನೀವು ಬ್ರೇಕ್-ಇವೆನ್ ಹಂತದಲ್ಲಿದ್ದೀರಿ (ಲಾಭವೂ ಇಲ್ಲ, ನಷ್ಟವೂ ಇಲ್ಲ).",
        "loss": "ಎಚ್ಚರಿಕೆ: ನಿಮ್ಮ ಪ್ರಸ್ತುತ ಬೆಲೆ ನಿಗದಿಯಿಂದ ನಷ್ಟ ಉಂಟಾಗುತ್ತದೆ.",
        "loan": "ಸಾಲದ ಮೊತ್ತ (₹)",
        "rate": "ವಾರ್ಷಿಕ ಬಡ್ಡಿ ದರ (%)",
        "period": "ಸಾಲದ ಅವಧಿ (ವರ್ಷಗಳು)",
        "monthly": "ಮಾಸಿಕ ಇಎಂಐ",
        "total_payment": "ಒಟ್ಟು ಪಾವತಿ",
        "interest": "ಪಾವತಿಸಬೇಕಾದ ಒಟ್ಟು ಬಡ್ಡಿ",
        "loan_note": "ಗಮನಿಸಿ: ಬ್ಯಾಂಕ್ ನೀತಿಗಳ ಆಧಾರದ ಮೇಲೆ ಸಾಲದ ನಿಯಮಗಳು ಬದಲಾಗಬಹುದು."
    }
}

# ============================================================
# SIDEBAR SETUP & LANGUAGE STATE
# ============================================================
st.sidebar.header(translations["English"]["settings"])

# Using key="language" to persist language state across the app seamlessly
language = st.sidebar.selectbox(
    "Select Language", 
    ["English", "Hindi (हिन्दी)", "Kannada (ಕನ್ನಡ)"],
    key="language"
)

# Active dictionary based on user selection
t = translations[language]

user_location = st.sidebar.selectbox(t["market_loc"], ["Hubballi", "Dharwad", "Belagavi", "Bengaluru"])

# App Header
st.title(t["title"])
st.subheader(t["subtitle"])

# Main Navigation Tabs
tab1, tab2, tab3 = st.tabs([t["tab1"], t["tab2"], t["tab3"]])

# Helper currency formatter
def money(amount):
    return f"₹{amount:,.2f}"


# ============================================================
# TAB 1: MARKET PRICES
# ============================================================
with tab1:
    st.header(t["tab1"])
    st.write(t["market_desc"])
    
    crop_input = st.text_input(t["crop_prompt"], placeholder=t["crop_placeholder"])
    
    if st.button(t["check_btn"]):
        if not crop_input.strip():
            st.warning(t["enter_crop_warning"])
        else:
            formatted_price = t["price_result"].format(crop=crop_input.capitalize(), location=user_location)
            st.success(formatted_price)
            st.caption(t["market_source"])
            
    st.markdown("---")
    st.subheader(t["board_header"])
    st.write(t["board_sub"].format(location=user_location))
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
            <div class="market-card">
                <div>
                    <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
                        <span style="font-size: 1.5rem;">🌾</span>
                        <span class="card-title">Tomato</span>
                    </div>
                    <div class="card-category">{t["veg"]}</div>
                </div>
                <div style="margin-top: 16px;">
                    <div class="card-price">₹30.00 / kg</div>
                    <div style="color: #059669; font-size: 0.875rem; font-weight: 600; margin-top: 4px;">{t["increasing"]}</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
            <div class="market-card">
                <div>
                    <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
                        <span style="font-size: 1.5rem;">🌾</span>
                        <span class="card-title">Onion</span>
                    </div>
                    <div class="card-category">{t["veg"]}</div>
                </div>
                <div style="margin-top: 16px;">
                    <div class="card-price">₹35.00 / kg</div>
                    <div style="color: #2563eb; font-size: 0.875rem; font-weight: 600; margin-top: 4px;">{t["stable"]}</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
            <div class="market-card">
                <div>
                    <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
                        <span style="font-size: 1.5rem;">🌾</span>
                        <span class="card-title">Potato</span>
                    </div>
                    <div class="card-category">{t["veg"]}</div>
                </div>
                <div style="margin-top: 16px;">
                    <div class="card-price">₹28.00 / kg</div>
                    <div style="color: #2563eb; font-size: 0.875rem; font-weight: 600; margin-top: 4px;">{t["stable"]}</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
            <div class="market-card">
                <div>
                    <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
                        <span style="font-size: 1.5rem;">🌾</span>
                        <span class="card-title">Carrot</span>
                    </div>
                    <div class="card-category">{t["veg"]}</div>
                </div>
                <div style="margin-top: 16px;">
                    <div class="card-price">₹40.00 / kg</div>
                    <div style="color: #059669; font-size: 0.875rem; font-weight: 600; margin-top: 4px;">{t["increasing"]}</div>
                </div>
            </div>
        """, unsafe_allow_html=True)


# ============================================================
# TAB 2: GOVERNMENT SCHEMES
# ============================================================
with tab2:
    st.header(t["tab2"])
    st.write(t["schemes_desc"])
    
    SCHEMES = [
        {
            "name": "PMEGP (Prime Minister's Employment Generation Programme)",
            "best_for": "New micro-enterprises in manufacturing and eligible service/non-farm activities.",
            "description": "A credit-linked government programme that supports new micro-enterprises through bank finance and margin-money subsidy. It is designed to create self-employment and employment opportunities, especially for rural and aspiring entrepreneurs.",
            "key": "Credit-linked subsidy up to 15% to 35% of project cost depending on category and area.",
            "why": "Ideal for setting up small manufacturing units, rural workshops, or agro-processing ventures.",
            "source": "Ministry of Micro, Small and Medium Enterprises (MSME)"
        },
        {
            "name": "PM Mudra Yojana (PMMY)",
            "best_for": "Small businesses needing working capital or business expansion finance.",
            "description": "Provides collateral-free institutional credit for eligible micro enterprises in manufacturing, trading, services and allied agricultural activities.",
            "key": "Loans categorized into Shishu (up to ₹50k), Kishor (₹50k–₹5L), and Tarun (₹5L–₹10L).",
            "why": "Collateral-free nature makes it very accessible for local shopkeepers and micro-vendors.",
            "source": "Department of Financial Services, Ministry of Finance"
        },
        {
            "name": "PM SVANidhi (PM Street Vendor's AtmaNirbhar Nidhi)",
            "best_for": "Eligible street vendors.",
            "description": "A micro-credit and support programme for street vendors. The restructured scheme includes progressive working-capital loans, digital adoption incentives and broader livelihood support.",
            "key": "Working capital loans starting at ₹10,000 with interest subsidies on timely repayment.",
            "why": "Tailored specifically for mobile vendors and micro-retailers looking to expand stock or digitize payments.",
            "source": "Ministry of Housing and Urban Affairs"
        },
        {
            "name": "PM FME (Formalisation of Micro Food Processing Enterprises)",
            "best_for": "Micro food-processing businesses and eligible SHGs/FPOs/cooperatives.",
            "description": "Supports formalisation, upgrading and capacity building for micro food-processing enterprises. Eligible individual units can receive credit-linked capital subsidy subject to scheme conditions.",
            "key": "35% capital subsidy for eligible micro food units with credit support.",
            "why": "Best for pickle makers, flour mills, spice grinders, and local food packaging units.",
            "source": "Ministry of Food Processing Industries"
        },
        {
            "name": "Kisan Credit Card (KCC)",
            "best_for": "Farmers and eligible agricultural/allied activities.",
            "description": "Provides formal credit access for agricultural and allied working-capital needs, subject to lending and eligibility conditions.",
            "key": "Timely short-term credit with interest subvention options for farmers.",
            "why": "Helps cover seasonal crop cultivation expenses, post-harvest costs, and maintenance of farm assets.",
            "source": "Ministry of Agriculture and Farmers Welfare / NABARD"
        }
    ]

    search_query = st.text_input(t["search_schemes"], placeholder=t["search_placeholder"])

    shown_schemes = []
    for scheme in SCHEMES:
        searchable_text = (scheme["name"] + " " + scheme["best_for"] + " " +
                           scheme["description"] + " " + scheme["why"]).lower()
        if not search_query or search_query.lower() in searchable_text:
            shown_schemes.append(scheme)

    SCHEME_TRANSLATIONS = {
        "Hindi (हिन्दी)": {
            "best": {
                "New micro-enterprises in manufacturing and eligible service/non-farm activities.": "विनिर्माण और पात्र सेवा/गैर-कृषि गतिविधियों वाले नए सूक्ष्म उद्यम।",
                "Small businesses needing working capital or business expansion finance.": "कार्यशील पूंजी या व्यवसाय विस्तार के लिए वित्त की जरूरत वाले छोटे व्यवसाय।",
                "Eligible street vendors.": "पात्र स्ट्रीट वेंडर।",
                "Micro food-processing businesses and eligible SHGs/FPOs/cooperatives.": "सूक्ष्म खाद्य-प्रसंस्करण व्यवसाय और पात्र SHG/FPO/सहकारी संस्थाएँ।",
                "Farmers and eligible agricultural/allied activities.": "किसान और पात्र कृषि/संबद्ध गतिविधियाँ।"
            },
            "desc": {
                "A credit-linked government programme that supports new micro-enterprises through bank finance and margin-money subsidy. It is designed to create self-employment and employment opportunities, especially for rural and aspiring entrepreneurs.": "यह बैंक वित्त और मार्जिन-मनी सब्सिडी के माध्यम से नए सूक्ष्म उद्यमों को सहायता देने वाला क्रेडिट-लिंक्ड सरकारी कार्यक्रम है।",
                "Provides collateral-free institutional credit for eligible micro enterprises in manufacturing, trading, services and allied agricultural activities.": "विनिर्माण, व्यापार, सेवा और संबद्ध कृषि गतिविधियों वाले पात्र सूक्ष्म उद्यमों के लिए बिना जमानत संस्थागत ऋण उपलब्ध कराता है।",
                "A micro-credit and support programme for street vendors. The restructured scheme includes progressive working-capital loans, digital adoption incentives and broader livelihood support.": "स्ट्रीट वेंडरों के लिए सूक्ष्म ऋण और सहायता कार्यक्रम।",
                "Supports formalisation, upgrading and capacity building for micro food-processing enterprises. Eligible individual units can receive credit-linked capital subsidy subject to scheme conditions.": "सूक्ष्म खाद्य-प्रसंस्करण उद्यमों के औपचारिकीकरण, उन्नयन और क्षमता निर्माण में सहायता करता है।",
                "Provides formal credit access for agricultural and allied working-capital needs, subject to lending and eligibility conditions.": "कृषि और संबद्ध कार्यशील पूंजी जरूरतों के लिए पात्रता और ऋण शर्तों के अनुसार औपचारिक ऋण सुविधा प्रदान करता है।"
            }
        },
        "Kannada (ಕನ್ನಡ)": {
            "best": {
                "New micro-enterprises in manufacturing and eligible service/non-farm activities.": "ಉತ್ಪಾದನೆ ಮತ್ತು ಅರ್ಹ ಸೇವೆ/ಕೃಷಿಯೇತರ ಚಟುವಟಿಕೆಗಳ ಹೊಸ ಸಣ್ಣ ಉದ್ಯಮಗಳು.",
                "Small businesses needing working capital or business expansion finance.": "ಕಾರ್ಯನಿರ್ವಹಣಾ ಬಂಡವಾಳ ಅಥವಾ ವ್ಯವಹಾರ ವಿಸ್ತರಣೆಗೆ ಹಣಕಾಸು ಬೇಕಿರುವ ಸಣ್ಣ ವ್ಯವಹಾರಗಳು.",
                "Eligible street vendors.": "ಅರ್ಹ ಬೀದಿ ವ್ಯಾಪಾರಿಗಳು.",
                "Micro food-processing businesses and eligible SHGs/FPOs/cooperatives.": "ಸಣ್ಣ ಆಹಾರ ಸಂಸ್ಕರಣಾ ವ್ಯವಹಾರಗಳು ಮತ್ತು ಅರ್ಹ SHG/FPO/ಸಹಕಾರಿ ಸಂಸ್ಥೆಗಳು.",
                "Farmers and eligible agricultural/allied activities.": "ರೈತರು ಮತ್ತು ಅರ್ಹ ಕೃಷಿ/ಸಂಬಂಧಿತ ಚಟುವಟಿಕೆಗಳು."
            },
            "desc": {
                "A credit-linked government programme that supports new micro-enterprises through bank finance and margin-money subsidy. It is designed to create self-employment and employment opportunities, especially for rural and aspiring entrepreneurs.": "ಬ್ಯಾಂಕ್ ಹಣಕಾಸು ಮತ್ತು ಮಾರ್ಜಿನ್-ಮನಿ ಸಬ್ಸಿಡಿ ಮೂಲಕ ಹೊಸ ಸಣ್ಣ ಉದ್ಯಮಗಳಿಗೆ ಬೆಂಬಲ ನೀಡುವ ಕ್ರೆಡಿಟ್-ಲಿಂಕ್ಡ್ ಸರ್ಕಾರಿ ಕಾರ್ಯಕ್ರಮ.",
                "Provides collateral-free institutional credit for eligible micro enterprises in manufacturing, trading, services and allied agricultural activities.": "ಉತ್ಪಾದನೆ, ವ್ಯಾಪಾರ, ಸೇವೆ ಮತ್ತು ಸಂಬಂಧಿತ ಕೃಷಿ ಚಟುವಟಿಕೆಗಳ ಅರ್ಹ ಸಣ್ಣ ಉದ್ಯಮಗಳಿಗೆ ಜಾಮೀನು ಇಲ್ಲದ ಸಂಸ್ಥಾತ್ಮಕ ಸಾಲ ಒದಗಿಸುತ್ತದೆ.",
                "A micro-credit and support programme for street vendors. The restructured scheme includes progressive working-capital loans, digital adoption incentives and broader livelihood support.": "ಬೀದಿ ವ್ಯಾಪಾರಿಗಳಿಗೆ ಸೂಕ್ಷ್ಮ ಸಾಲ ಮತ್ತು ಬೆಂಬಲ ಕಾರ್ಯಕ್ರಮ.",
                "Supports formalisation, upgrading and capacity building for micro food-processing enterprises. Eligible individual units can receive credit-linked capital subsidy subject to scheme conditions.": "ಸಣ್ಣ ಆಹಾರ ಸಂಸ್ಕರಣಾ ಉದ್ಯಮಗಳ ಔಪಚಾರಿಕೀಕರಣ, ಉನ್ನತೀಕರಣ ಮತ್ತು ಸಾಮರ್ಥ್ಯ ವೃದ್ಧಿಗೆ ಬೆಂಬಲ ನೀಡುತ್ತದೆ.",
                "Provides formal credit access for agricultural and allied working-capital needs, subject to lending and eligibility conditions.": "ಕೃಷಿ ಮತ್ತು ಸಂಬಂಧಿತ ಕಾರ್ಯನಿರ್ವಹಣಾ ಬಂಡವಾಳ ಅಗತ್ಯಗಳಿಗೆ ಸಾಲ ಮತ್ತು ಅರ್ಹತಾ ಷರತ್ತುಗಳಂತೆ ಅಧಿಕೃತ ಸಾಲ ಸೌಲಭ್ಯ ಒದಗಿಸುತ್ತದೆ."
            }
        }
    }

    def get_scheme_text(kind, value):
        return SCHEME_TRANSLATIONS.get(language, {}).get(kind, {}).get(value, value)

    if not shown_schemes:
        st.info(t["no_schemes"])
    else:
        for scheme in shown_schemes:
            with st.expander(scheme["name"]):
                best_text = get_scheme_text('best', scheme['best_for'])
                desc_text = get_scheme_text('desc', scheme['description'])
                
                st.markdown(f"**Best For:** {best_text}")
                st.write(desc_text)
                st.markdown(f"**Key Benefit:** {scheme['key']}")
                st.markdown(f"**Why it helps:** {scheme['why']}")
                st.caption(f"Official Data Source: {scheme['source']}")

    st.warning(t["scheme_note"])


# ============================================================
# TAB 3: FINANCIAL ASSISTANT
# ============================================================
with tab3:
    st.header(t["finance_title"])
    
    fin_tab1, fin_tab2 = st.tabs([t["profit_tab"], t["emi_tab"]])

    with fin_tab1:
        st.subheader(t["profit_est"])
        col1, col2 = st.columns(2)
        with col1:
            quantity = st.number_input(t["quantity"], min_value=1.0, value=100.0)
            purchase_price = st.number_input(t["purchase"], min_value=0.0, value=20.0)
        with col2:
            selling_price = st.number_input(t["selling"], min_value=0.0, value=30.0)
            other_costs = st.number_input(t["other"], min_value=0.0, value=0.0)

        total_cost = quantity * purchase_price + other_costs
        revenue = quantity * selling_price
        profit = revenue - total_cost

        a, b, c = st.columns(3)
        a.metric(t["total_cost"], money(total_cost))
        b.metric(t["revenue"], money(revenue))
        c.metric(t["profit"], money(profit))

        if profit > 0:
            st.success(t["positive"])
        elif profit == 0:
            st.info(t["break_even"])
        else:
            st.error(t["loss"])

    with fin_tab2:
        st.subheader(t["emi_tab"].replace("🏦 ", ""))
        
        col1, col2, col3 = st.columns(3)
        with col1:
            principal = st.number_input(t["loan"], min_value=1000.0, value=100000.0, step=5000.0)
        with col2:
            annual_rate = st.number_input(t["rate"], min_value=0.0, value=10.0, step=0.5)
        with col3:
            years = st.number_input(t["period"], min_value=1, value=3)

        months = years * 12
        monthly_rate = annual_rate / 12 / 100
        
        if monthly_rate == 0:
            emi = principal / months
        else:
            emi = principal * monthly_rate * (1 + monthly_rate) ** months / ((1 + monthly_rate) ** months - 1)

        total_payment = emi * months
        total_interest = total_payment - principal

        a, b, c = st.columns(3)
        a.metric(t["monthly"], money(emi))
        b.metric(t["total_payment"], money(total_payment))
        c.metric(t["interest"], money(total_interest))
        
        st.caption(t["loan_note"])
