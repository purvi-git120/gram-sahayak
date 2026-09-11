import streamlit as st

# Page Configuration
st.set_page_config(page_title="Gram Sahayak", page_icon="🌾", layout="centered")

# Custom styling to ensure dark theme and readable white card text
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
            
    st.markdown("---")
    st.subheader("🧺 Crop Market Board")
    st.write(f"Showing  crops for the selected demonstration market: {user_location}")
    
    # Display cards in a 4-column layout with dark readable text on white background
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
            <div class="market-card">
                <div>
                    <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
                        <span style="font-size: 1.5rem;">🌾</span>
                        <span class="card-title">Tomato</span>
                    </div>
                    <div class="card-category">Vegetable</div>
                </div>
                <div style="margin-top: 16px;">
                    <div class="card-price">₹30.00 / kg</div>
                    <div style="color: #059669; font-size: 0.875rem; font-weight: 600; margin-top: 4px;">📈 Increasing</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class="market-card">
                <div>
                    <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
                        <span style="font-size: 1.5rem;">🌾</span>
                        <span class="card-title">Onion</span>
                    </div>
                    <div class="card-category">Vegetable</div>
                </div>
                <div style="margin-top: 16px;">
                    <div class="card-price">₹35.00 / kg</div>
                    <div style="color: #2563eb; font-size: 0.875rem; font-weight: 600; margin-top: 4px;">➡️ Stable</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
            <div class="market-card">
                <div>
                    <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
                        <span style="font-size: 1.5rem;">🌾</span>
                        <span class="card-title">Potato</span>
                    </div>
                    <div class="card-category">Vegetable</div>
                </div>
                <div style="margin-top: 16px;">
                    <div class="card-price">₹28.00 / kg</div>
                    <div style="color: #2563eb; font-size: 0.875rem; font-weight: 600; margin-top: 4px;">➡️ Stable</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
            <div class="market-card">
                <div>
                    <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
                        <span style="font-size: 1.5rem;">🌾</span>
                        <span class="card-title">Carrot</span>
                    </div>
                    <div class="card-category">Vegetable</div>
                </div>
                <div style="margin-top: 16px;">
                    <div class="card-price">₹40.00 / kg</div>
                    <div style="color: #059669; font-size: 0.875rem; font-weight: 600; margin-top: 4px;">📈 Increasing</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

# ----------------- TAB 2: GOVERNMENT SCHEMES -----------------
with tab2:
    st.header(t["tab2"])
    st.write("Find out which business or agricultural schemes you qualify for.")
    
    # Comprehensive Scheme Dataset for Rural Micro-Entrepreneurs & Farmers
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
        },
        {
            "name": "Agriculture Infrastructure Fund (AIF)",
            "best_for": "Post-harvest infrastructure and eligible community farming assets.",
            "description": "Provides financing support for eligible agriculture infrastructure such as post-harvest management and community farming assets.",
            "key": "Interest subvention of 3% per annum up to ₹2 crore for viable agriculture infrastructure projects.",
            "why": "Great for cold storage, sorting units, warehousing, and primary processing facilities.",
            "source": "Ministry of Agriculture and Farmers Welfare"
        },
        {
            "name": "Agri-Clinic and Agri-Business Centres (ACABC)",
            "best_for": "Eligible agriculture-trained entrepreneurs providing farm-related services.",
            "description": "Supports trained agricultural professionals/eligible candidates in setting up agri-clinics and agri-business centres that provide advisory and agricultural services to farmers.",
            "key": "Subsidy-backed financial support through commercial banks for trained agri-graduates.",
            "why": "Empowers skilled youth to offer soil testing, input supply, and extension services locally.",
            "source": "Ministry of Agriculture and Farmers Welfare"
        },
        {
            "name": "Deendayal Antyodaya Yojana - NRLM (DAY-NRLM)",
            "best_for": "Rural women-led Self Help Groups and rural livelihoods.",
            "description": "A rural livelihoods programme that works through Self Help Groups and community institutions to improve access to finance, skills, enterprise support and sustainable livelihoods.",
            "key": "Revolving fund and community investment support for networked Self Help Groups (SHGs).",
            "why": "Crucial for community-led micro-enterprises and group-based village economic activities.",
            "source": "Ministry of Rural Development"
        },
        {
            "name": "PM Vishwakarma Scheme",
            "best_for": "Eligible traditional artisans and craftspeople.",
            "description": "Supports eligible traditional artisans and craftspeople with recognition, skill development, toolkit support, credit and market-oriented assistance under the scheme.",
            "key": "End-to-end support including PM Vishwakarma certificate, toolkit incentive up to ₹15,000, and collateral-free credit.",
            "why": "Designed specifically for traditional craftsmen like carpenters, blacksmiths, potters, and weavers.",
            "source": "Ministry of Micro, Small and Medium Enterprises (MSME)"
        },
        {
            "name": "PM-KUSUM (Pradhan Mantri Kisan Urja Suraksha evam Utthaan Mahabhiyan)",
            "best_for": "Eligible farmers and agricultural energy/solar applications.",
            "description": "Supports solar-energy-related interventions in agriculture, including eligible solar pumps and other components under the scheme.",
            "key": "Financial assistance to install standalone solar pumps and grid-connected solar power plants.",
            "why": "Helps farmers secure reliable daytime solar power for irrigation and reduce diesel dependence.",
            "source": "Ministry of New and Renewable Energy (MNRE)"
        }
    ]

    # Search Box for filtering schemes dynamically
    search_query = st.text_input("🔎 Search Schemes", placeholder="e.g., loan, subsidy, vendor, food...")

    # Filter schemes based on search query
    shown_schemes = []
    for scheme in SCHEMES:
        searchable_text = (scheme["name"] + " " + scheme["best_for"] + " " +
                           scheme["description"] + " " + scheme["why"]).lower()
        if not search_query or search_query.lower() in searchable_text:
            shown_schemes.append(scheme)

    # Dictionary for translating scheme descriptions/best_for text dynamically into Hindi and Kannada
    SCHEME_TRANSLATIONS = {
        "Hindi (हिन्दी)": {
            "best": {
                "New micro-enterprises in manufacturing and eligible service/non-farm activities.": "विनिर्माण और पात्र सेवा/गैर-कृषि गतिविधियों वाले नए सूक्ष्म उद्यम।",
                "Small businesses needing working capital or business expansion finance.": "कार्यशील पूंजी या व्यवसाय विस्तार के लिए वित्त की जरूरत वाले छोटे व्यवसाय।",
                "Eligible street vendors.": "पात्र स्ट्रीट वेंडर।",
                "Micro food-processing businesses and eligible SHGs/FPOs/cooperatives.": "सूक्ष्म खाद्य-प्रसंस्करण व्यवसाय और पात्र SHG/FPO/सहकारी संस्थाएँ।",
                "Farmers and eligible agricultural/allied activities.": "किसान और पात्र कृषि/संबद्ध गतिविधियाँ।",
                "Post-harvest infrastructure and eligible community farming assets.": "फसल कटाई के बाद की अवसंरचना और पात्र सामुदायिक कृषि परिसंपत्तियाँ।",
                "Eligible agriculture-trained entrepreneurs providing farm-related services.": "पात्र कृषि-प्रशिक्षित उद्यमी जो कृषि संबंधी सेवाएँ देते हैं।",
                "Rural women-led Self Help Groups and rural livelihoods.": "ग्रामीण महिलाओं के नेतृत्व वाले स्वयं सहायता समूह और ग्रामीण आजीविका।",
                "Eligible traditional artisans and craftspeople.": "पात्र पारंपरिक कारीगर और शिल्पकार।",
                "Eligible farmers and agricultural energy/solar applications.": "पात्र किसान और कृषि ऊर्जा/सौर अनुप्रयोग।"
            },
            "desc": {
                "A credit-linked government programme that supports new micro-enterprises through bank finance and margin-money subsidy. It is designed to create self-employment and employment opportunities, especially for rural and aspiring entrepreneurs.": "यह बैंक वित्त और मार्जिन-मनी सब्सिडी के माध्यम से नए सूक्ष्म उद्यमों को सहायता देने वाला क्रेडिट-लिंक्ड सरकारी कार्यक्रम है। इसका उद्देश्य विशेष रूप से ग्रामीण और नए उद्यमियों के लिए स्वरोजगार और रोजगार के अवसर बनाना है।",
                "Provides collateral-free institutional credit for eligible micro enterprises in manufacturing, trading, services and allied agricultural activities.": "विनिर्माण, व्यापार, सेवा और संबद्ध कृषि गतिविधियों वाले पात्र सूक्ष्म उद्यमों के लिए बिना जमानत संस्थागत ऋण उपलब्ध कराता है।",
                "A micro-credit and support programme for street vendors. The restructured scheme includes progressive working-capital loans, digital adoption incentives and broader livelihood support.": "स्ट्रीट वेंडरों के लिए सूक्ष्म ऋण और सहायता कार्यक्रम। पुनर्गठित योजना में क्रमिक कार्यशील पूंजी ऋण, डिजिटल अपनाने के प्रोत्साहन और व्यापक आजीविका सहायता शामिल है।",
                "Supports formalisation, upgrading and capacity building for micro food-processing enterprises. Eligible individual units can receive credit-linked capital subsidy subject to scheme conditions.": "सूक्ष्म खाद्य-प्रसंस्करण उद्यमों के औपचारिकीकरण, उन्नयन और क्षमता निर्माण में सहायता करता है। पात्र व्यक्तिगत इकाइयों को योजना की शर्तों के अनुसार क्रेडिट-लिंक्ड पूंजी सब्सिडी मिल सकती है।",
                "Provides formal credit access for agricultural and allied working-capital needs, subject to lending and eligibility conditions.": "कृषि और संबद्ध कार्यशील पूंजी जरूरतों के लिए पात्रता और ऋण शर्तों के अनुसार औपचारिक ऋण सुविधा प्रदान करता है।",
                "Provides financing support for eligible agriculture infrastructure such as post-harvest management and community farming assets.": "फसल कटाई के बाद प्रबंधन और सामुदायिक कृषि परिसंपत्तियों जैसी पात्र कृषि अवसंरचना के लिए वित्तीय सहायता प्रदान करता है।",
                "Supports trained agricultural professionals/eligible candidates in setting up agri-clinics and agri-business centres that provide advisory and agricultural services to farmers.": "प्रशिक्षित कृषि पेशेवरों/पात्र उम्मीदवारों को किसानों के लिए सलाह और कृषि सेवाएँ देने वाले एग्री-क्लिनिक और एग्री-बिजनेस केंद्र स्थापित करने में सहायता करता है।",
                "A rural livelihoods programme that works through Self Help Groups and community institutions to improve access to finance, skills, enterprise support and sustainable livelihoods.": "स्वयं सहायता समूहों और सामुदायिक संस्थाओं के माध्यम से वित्त, कौशल, उद्यम सहायता और टिकाऊ आजीविका तक पहुँच बेहतर करने वाला ग्रामीण आजीविका कार्यक्रम।",
                "Supports eligible traditional artisans and craftspeople with recognition, skill development, toolkit support, credit and market-oriented assistance under the scheme.": "पात्र पारंपरिक कारीगरों और शिल्पकारों को पहचान, कौशल विकास, टूलकिट, ऋण और बाजार-उन्मुख सहायता प्रदान करता है।",
                "Supports solar-energy-related interventions in agriculture, including eligible solar pumps and other components under the scheme.": "कृषि में सौर ऊर्जा से जुड़े उपायों, पात्र सौर पंपों और योजना के अन्य घटकों को सहायता देता है।"
            }
        },
        "Kannada (ಕನ್ನಡ)": {
            "best": {
                "New micro-enterprises in manufacturing and eligible service/non-farm activities.": "ಉತ್ಪಾದನೆ ಮತ್ತು ಅರ್ಹ ಸೇವೆ/ಕೃಷಿಯೇತರ ಚಟುವಟಿಕೆಗಳ ಹೊಸ ಸಣ್ಣ ಉದ್ಯಮಗಳು.",
                "Small businesses needing working capital or business expansion finance.": "ಕಾರ್ಯನಿರ್ವಹಣಾ ಬಂಡವಾಳ ಅಥವಾ ವ್ಯವಹಾರ ವಿಸ್ತರಣೆಗೆ ಹಣಕಾಸು ಬೇಕಿರುವ ಸಣ್ಣ ವ್ಯವಹಾರಗಳು.",
                "Eligible street vendors.": "ಅರ್ಹ ಬೀದಿ ವ್ಯಾಪಾರಿಗಳು.",
                "Micro food-processing businesses and eligible SHGs/FPOs/cooperatives.": "ಸಣ್ಣ ಆಹಾರ ಸಂಸ್ಕರಣಾ ವ್ಯವಹಾರಗಳು ಮತ್ತು ಅರ್ಹ SHG/FPO/ಸಹಕಾರಿ ಸಂಸ್ಥೆಗಳು.",
                "Farmers and eligible agricultural/allied activities.": "ರೈತರು ಮತ್ತು ಅರ್ಹ ಕೃಷಿ/ಸಂಬಂಧಿತ ಚಟುವಟಿಕೆಗಳು.",
                "Post-harvest infrastructure and eligible community farming assets.": "ಕೊಯ್ಲಿನ ನಂತರದ ಮೂಲಸೌಕರ್ಯ ಮತ್ತು ಅರ್ಹ ಸಮುದಾಯ ಕೃಷಿ ಆಸ್ತಿಗಳು.",
                "Eligible agriculture-trained entrepreneurs providing farm-related services.": "ಕೃಷಿ ತರಬೇತಿ ಪಡೆದ ಅರ್ಹ ಉದ್ಯಮಿಗಳು ಮತ್ತು ಕೃಷಿ ಸಂಬಂಧಿತ ಸೇವಾ ಪೂರೈಕೆದಾರರು.",
                "Rural women-led Self Help Groups and rural livelihoods.": "ಗ್ರಾಮೀಣ ಮಹಿಳೆಯರ ನೇತೃತ್ವದ ಸ್ವಸಹಾಯ ಗುಂಪುಗಳು ಮತ್ತು ಗ್ರಾಮೀಣ ಜೀವನೋಪಾಯ.",
                "Eligible traditional artisans and craftspeople.": "ಅರ್ಹ ಸಾಂಪ್ರದಾಯಿಕ ಕುಶಲಕರ್ಮಿಗಳು ಮತ್ತು ಶಿಲ್ಪಿಗಳು.",
                "Eligible farmers and agricultural energy/solar applications.": "ಅರ್ಹ ರೈತರು ಮತ್ತು ಕೃಷಿ ಶಕ್ತಿ/ಸೌರ ಅನ್ವಯಿಕೆಗಳು."
            },
            "desc": {
                "A credit-linked government programme that supports new micro-enterprises through bank finance and margin-money subsidy. It is designed to create self-employment and employment opportunities, especially for rural and aspiring entrepreneurs.": "ಬ್ಯಾಂಕ್ ಹಣಕಾಸು ಮತ್ತು ಮಾರ್ಜಿನ್-ಮನಿ ಸಬ್ಸಿಡಿ ಮೂಲಕ ಹೊಸ ಸಣ್ಣ ಉದ್ಯಮಗಳಿಗೆ ಬೆಂಬಲ ನೀಡುವ ಕ್ರೆಡಿಟ್-ಲಿಂಕ್ಡ್ ಸರ್ಕಾರಿ ಕಾರ್ಯಕ್ರಮ. ವಿಶೇಷವಾಗಿ ಗ್ರಾಮೀಣ ಮತ್ತು ಹೊಸ ಉದ್ಯಮಿಗಳಿಗೆ ಸ್ವಯಂ ಉದ್ಯೋಗ ಹಾಗೂ ಉದ್ಯೋಗಾವಕಾಶಗಳನ್ನು ಸೃಷ್ಟಿಸುವುದು ಇದರ ಉದ್ದೇಶ.",
                "Provides collateral-free institutional credit for eligible micro enterprises in manufacturing, trading, services and allied agricultural activities.": "ಉತ್ಪಾದನೆ, ವ್ಯಾಪಾರ, ಸೇವೆ ಮತ್ತು ಸಂಬಂಧಿತ ಕೃಷಿ ಚಟುವಟಿಕೆಗಳ ಅರ್ಹ ಸಣ್ಣ ಉದ್ಯಮಗಳಿಗೆ ಜಾಮೀನು ಇಲ್ಲದ ಸಂಸ್ಥಾತ್ಮಕ ಸಾಲ ಒದಗಿಸುತ್ತದೆ.",
                "A micro-credit and support programme for street vendors. The restructured scheme includes progressive working-capital loans, digital adoption incentives and broader livelihood support.": "ಬೀದಿ ವ್ಯಾಪಾರಿಗಳಿಗೆ ಸೂಕ್ಷ್ಮ ಸಾಲ ಮತ್ತು ಬೆಂಬಲ ಕಾರ್ಯಕ್ರಮ. ಪರಿಷ್ಕೃತ ಯೋಜನೆಯಲ್ಲಿ ಹಂತ ಹಂತದ ಕಾರ್ಯನಿರ್ವಹಣಾ ಬಂಡವಾಳ ಸಾಲ, ಡಿಜಿಟಲ್ ಬಳಕೆಗೆ ಪ್ರೋತ್ಸಾಹ ಮತ್ತು ಜೀವನೋಪಾಯ ಬೆಂಬಲ ಸೇರಿವೆ.",
                "Supports formalisation, upgrading and capacity building for micro food-processing enterprises. Eligible individual units can receive credit-linked capital subsidy subject to scheme conditions.": "ಸಣ್ಣ ಆಹಾರ ಸಂಸ್ಕರಣಾ ಉದ್ಯಮಗಳ ಔಪಚಾರಿಕೀಕರಣ, ಉನ್ನತೀಕರಣ ಮತ್ತು ಸಾಮರ್ಥ್ಯ ವೃದ್ಧಿಗೆ ಬೆಂಬಲ ನೀಡುತ್ತದೆ. ಅರ್ಹ ವೈಯಕ್ತಿಕ ಘಟಕಗಳಿಗೆ ಯೋಜನೆಯ ಷರತ್ತುಗಳಂತೆ ಕ್ರೆಡಿಟ್-ಲಿಂಕ್ಡ್ ಬಂಡವಾಳ ಸಬ್ಸಿಡಿ ದೊರೆಯಬಹುದು.",
                "Provides formal credit access for agricultural and allied working-capital needs, subject to lending and eligibility conditions.": "ಕೃಷಿ ಮತ್ತು ಸಂಬಂಧಿತ ಕಾರ್ಯನಿರ್ವಹಣಾ ಬಂಡವಾಳ ಅಗತ್ಯಗಳಿಗೆ ಸಾಲ ಮತ್ತು ಅರ್ಹತಾ ಷರತ್ತುಗಳಂತೆ ಅಧಿಕೃತ ಸಾಲ ಸೌಲಭ್ಯ ಒದಗಿಸುತ್ತದೆ.",
                "Provides financing support for eligible agriculture infrastructure such as post-harvest management and community farming assets.": "ಕೊಯ್ಲಿನ ನಂತರದ ನಿರ್ವಹಣೆ ಮತ್ತು ಸಮುದಾಯ ಕೃಷಿ ಆಸ್ತಿಗಳಂತಹ ಅರ್ಹ ಕೃಷಿ ಮೂಲಸೌಕರ್ಯಕ್ಕೆ ಹಣಕಾಸು ಬೆಂಬಲ ನೀಡುತ್ತದೆ.",
                "Supports trained agricultural professionals/eligible candidates in setting up agri-clinics and agri-business centres that provide advisory and agricultural services to farmers.": "ತರಬೇತಿ ಪಡೆದ ಕೃಷಿ ವೃತ್ತಿಪರರು/ಅರ್ಹ ಅಭ್ಯರ್ಥಿಗಳು ರೈತರಿಗೆ ಸಲಹೆ ಮತ್ತು ಕೃಷಿ ಸೇವೆ ನೀಡುವ ಅಗ್ರಿ-ಕ್ಲಿನಿಕ್ ಮತ್ತು ಅಗ್ರಿ-ಬಿಸಿನೆಸ್ ಕೇಂದ್ರಗಳನ್ನು ಸ್ಥಾಪಿಸಲು ಬೆಂಬಲ ನೀಡುತ್ತದೆ.",
                "A rural livelihoods programme that works through Self Help Groups and community institutions to improve access to finance, skills, enterprise support and sustainable livelihoods.": "ಸ್ವಸಹಾಯ ಗುಂಪುಗಳು ಮತ್ತು ಸಮುದಾಯ ಸಂಸ್ಥೆಗಳ ಮೂಲಕ ಹಣಕಾಸು, ಕೌಶಲ್ಯ, ಉದ್ಯಮ ಬೆಂಬಲ ಮತ್ತು ಶಾಶ್ವತ ಜೀವನೋಪಾಯಕ್ಕೆ ಪ್ರವೇಶವನ್ನು ಸುಧಾರಿಸುವ ಗ್ರಾಮೀಣ ಜೀವನೋಪಾಯ ಕಾರ್ಯಕ್ರಮ.",
                "Supports eligible traditional artisans and craftspeople with recognition, skill development, toolkit support, credit and market-oriented assistance under the scheme.": "ಅರ್ಹ ಸಾಂಪ್ರದಾಯಿಕ ಕುಶಲಕರ್ಮಿಗಳು ಮತ್ತು ಶಿಲ್ಪಿಗಳಿಗೆ ಮಾನ್ಯತೆ, ಕೌಶಲ್ಯ ಅಭಿವೃದ್ಧಿ, ಟೂಲ್‌ಕಿಟ್, ಸಾಲ ಮತ್ತು ಮಾರುಕಟ್ಟೆ ಆಧಾರಿತ ಸಹಾಯ ನೀಡುತ್ತದೆ.",
                "Supports solar-energy-related interventions in agriculture, including eligible solar pumps and other components under the scheme.": "ಅರ್ಹ ಸೌರ ಪಂಪ್‌ಗಳು ಮತ್ತು ಯೋಜನೆಯ ಇತರ ಘಟಕಗಳನ್ನು ಒಳಗೊಂಡಂತೆ ಕೃಷಿಯಲ್ಲಿ ಸೌರಶಕ್ತಿ ಸಂಬಂಧಿತ ಕ್ರಮಗಳಿಗೆ ಬೆಂಬಲ ನೀಡುತ್ತದೆ."
            }
        }
    }

    def get_scheme_text(kind, value):
        return SCHEME_TRANSLATIONS.get(language, {}).get(kind, {}).get(value, value)

    if not shown_schemes:
        st.info("No matching schemes found. Try searching with a different keyword.")
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

    st.warning("Note: Scheme rules, eligibility criteria, and financial caps are subject to government guidelines. Verify details with local branch offices or common service centers (CSCs) before applying.")

# ------------------------------------------------------------
# TRANSLATION & UTILITY HELPERS (Ensure these are defined globally)
# ------------------------------------------------------------

# Ensure 'language' state variable is initialized (defaults to English if not set)
if "language" not in st.session_state:
    st.session_state["language"] = "English"

language = st.session_state["language"]

# Master translation dictionary containing finance UI strings
GLOBAL_TR = {
    "English": {
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
        "break_even": "आप सम-विच्छेद (ब्रेक-इवन) बिंदु पर हैं (न लाभ, न हानि)।",
        "loss": "चेतावनी: आपकी वर्तमान कीमत से नुकसान हो रहा है।",
        "loan": "ऋण राशि (₹)",
        "rate": "वार्षिक ब्याज दर (%)",
        "period": "ऋण अवधि (वर्ष)",
        "monthly": "मासिक ईएमआई",
        "total_payment": "कुल भुगतान",
        "interest": "देय कुल ब्याज",
        "loan_note": "नोट: बैंक की नीतियों और व्यक्तिगत क्रेडिट मूल्यांकन के आधार पर वास्तविक ऋण शर्तें और ब्याज अलग हो सकते हैं।"
    },
    "Kannada (ಕನ್ನಡ)": {
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
        "loan_note": "ಗಮನಿಸಿ: ಬ್ಯಾಂಕ್ ನೀತಿಗಳು ಮತ್ತು ವೈಯಕ್ತಿಕ ಕ್ರೆಡಿಟ್ ಮೌಲ್ಯಮಾಪನದ ಆಧಾರದ ಮೇಲೆ ವಾಸ್ತವ ಸಾಲದ ನಿಯಮಗಳು ಬದಲಾಗಬಹುದು."
    }
}

def tr(key):
    """Safe translation retrieval function"""
    lang_dict = GLOBAL_TR.get(language, GLOBAL_TR["English"])
    return lang_dict.get(key, GLOBAL_TR["English"].get(key, key))

def money(amount):
    """Currency formatter helper"""
    return f"₹{amount:,.2f}"


# ============================================================
# TAB 3: FINANCIAL ASSISTANT (Corrected Block)
# ============================================================

with tab3:
    st.header("💰 " + tr("finance_title"))
    
    # Nested sub-tabs for Profit Estimation and Loan EMI Calculator
    fin_tab1, fin_tab2 = st.tabs([tr("profit_tab"), tr("emi_tab")])

    # Sub-Tab 1: Profit Estimation Calculator
    with fin_tab1:
        st.subheader(tr("profit_est"))
        col1, col2 = st.columns(2)
        with col1:
            quantity = st.number_input(tr("quantity"), min_value=1.0, value=100.0)
            purchase_price = st.number_input(tr("purchase"), min_value=0.0, value=20.0)
        with col2:
            selling_price = st.number_input(tr("selling"), min_value=0.0, value=30.0)
            other_costs = st.number_input(tr("other"), min_value=0.0, value=0.0)

        total_cost = quantity * purchase_price + other_costs
        revenue = quantity * selling_price
        profit = revenue - total_cost

        a, b, c = st.columns(3)
        a.metric(tr("total_cost"), money(total_cost))
        b.metric(tr("revenue"), money(revenue))
        c.metric(tr("profit"), money(profit))

        if profit > 0:
            st.success(tr("positive"))
        elif profit == 0:
            st.info(tr("break_even"))
        else:
            st.error(tr("loss"))

    # Sub-Tab 2: Loan EMI Calculator
    with fin_tab2:
        emi_tab_title = tr("emi_tab").replace("🏦 ", "")
        st.subheader(emi_tab_title)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            principal = st.number_input(tr("loan"), min_value=1000.0, value=100000.0, step=5000.0)
        with col2:
            annual_rate = st.number_input(tr("rate"), min_value=0.0, value=10.0, step=0.5)
        with col3:
            years = st.number_input(tr("period"), min_value=1, value=3)

        months = years * 12
        monthly_rate = annual_rate / 12 / 100
        
        if monthly_rate == 0:
            emi = principal / months
        else:
            emi = principal * monthly_rate * (1 + monthly_rate) ** months / ((1 + monthly_rate) ** months - 1)

        total_payment = emi * months
        total_interest = total_payment - principal

        a, b, c = st.columns(3)
        a.metric(tr("monthly"), money(emi))
        b.metric(tr("total_payment"), money(total_payment))
        c.metric(tr("interest"), money(total_interest))
        
        st.caption(tr("loan_note"))
