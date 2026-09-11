<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Market Prices - Hubballi</title>
    <!-- Tailwind CSS CDN for styling -->
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-[#0f172a] text-white min-h-screen font-sans p-6">

    <div class="max-w-7xl mx-auto space-y-8">
        
        <!-- Header Section -->
        <div>
            <div class="flex items-center space-x-3 mb-2">
                <span class="text-3xl">📊</span>
                <h1 class="text-3xl font-bold tracking-tight">Market Prices</h1>
            </div>
            <p class="text-slate-400 text-sm">
                Sample market information for Hubballi. Use it for demonstration and planning only; verify current local mandi prices before making financial decisions.
            </p>
        </div>

        <!-- Filter Section -->
        <div class="space-y-2">
            <label for="categoryFilter" class="block text-sm font-medium text-slate-300">Filter by crop category</label>
            <select id="categoryFilter" class="w-full md:w-64 bg-[#1e293b] border border-slate-700 text-white rounded-lg px-4 py-2.5 focus:outline-none focus:ring-2 focus:ring-indigo-500">
                <option value="All">All</option>
                <option value="Vegetable">Vegetable</option>
                <option value="Fruit">Fruit</option>
                <option value="Grain">Grain</option>
            </select>
        </div>

        <!-- Crop Market Board Section -->
        <div class="space-y-4">
            <div class="flex items-center space-x-2">
                <span class="text-2xl">🧺</span>
                <h2 class="text-xl font-semibold">Crop Market Board</h2>
            </div>
            <p class="text-slate-400 text-sm">Showing 46 crops for the selected demonstration market: Hubballi</p>

            <!-- Cards Grid with Fixed Dark Text on White Background Cards -->
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
                
                <!-- Card 1: Tomato -->
                <div class="bg-white text-slate-900 rounded-2xl p-5 shadow-lg flex flex-col justify-between space-y-4">
                    <div>
                        <div class="flex items-center space-x-2 mb-3">
                            <span class="text-2xl">🌾</span>
                            <h3 class="text-xl font-bold text-slate-900">Tomato</h3>
                        </div>
                        <p class="text-sm font-medium text-slate-600">Vegetable</p>
                    </div>
                    <div class="space-y-2">
                        <div class="text-2xl font-extrabold text-slate-800">₹30.00 / kg</div>
                        <div class="flex items-center space-x-1.5 text-sm font-medium text-emerald-600">
                            <span>📈</span>
                            <span>Increasing</span>
                        </div>
                    </div>
                </div>

                <!-- Card 2: Onion -->
                <div class="bg-white text-slate-900 rounded-2xl p-5 shadow-lg flex flex-col justify-between space-y-4">
                    <div>
                        <div class="flex items-center space-x-2 mb-3">
                            <span class="text-2xl">🌾</span>
                            <h3 class="text-xl font-bold text-slate-900">Onion</h3>
                        </div>
                        <p class="text-sm font-medium text-slate-600">Vegetable</p>
                    </div>
                    <div class="space-y-2">
                        <div class="text-2xl font-extrabold text-slate-800">₹35.00 / kg</div>
                        <div class="flex items-center space-x-1.5 text-sm font-medium text-blue-600">
                            <span>➡️</span>
                            <span>Stable</span>
                        </div>
                    </div>
                </div>

                <!-- Card 3: Potato -->
                <div class="bg-white text-slate-900 rounded-2xl p-5 shadow-lg flex flex-col justify-between space-y-4">
                    <div>
                        <div class="flex items-center space-x-2 mb-3">
                            <span class="text-2xl">🌾</span>
                            <h3 class="text-xl font-bold text-slate-900">Potato</h3>
                        </div>
                        <p class="text-sm font-medium text-slate-600">Vegetable</p>
                    </div>
                    <div class="space-y-2">
                        <div class="text-2xl font-extrabold text-slate-800">₹28.00 / kg</div>
                        <div class="flex items-center space-x-1.5 text-sm font-medium text-blue-600">
                            <span>➡️</span>
                            <span>Stable</span>
                        </div>
                    </div>
                </div>

                <!-- Card 4: Carrot -->
                <div class="bg-white text-slate-900 rounded-2xl p-5 shadow-lg flex flex-col justify-between space-y-4">
                    <div>
                        <div class="flex items-center space-x-2 mb-3">
                            <span class="text-2xl">🌾</span>
                            <h3 class="text-xl font-bold text-slate-900">Carrot</h3>
                        </div>
                        <p class="text-sm font-medium text-slate-600">Vegetable</p>
                    </div>
                    <div class="space-y-2">
                        <div class="text-2xl font-extrabold text-slate-800">₹40.00 / kg</div>
                        <div class="flex items-center space-x-1.5 text-sm font-medium text-emerald-600">
                            <span>📈</span>
                            <span>Increasing</span>
                        </div>
                    </div>
                </div>

            </div>
        </div>
import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Market Prices - Hubballi",
    page_icon="📊",
    layout="wide"
)

# Custom styling to ensure dark theme and readable white card text
st.markdown("""
    <style>
    .stApp {
        background-color: #0f172a;
        color: #ffffff;
    }
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

# Main Container
st.markdown('<div style="font-size: 2rem; font-weight: bold; display: flex; align-items: center; gap: 10px;">📊 Market Prices</div>', unsafe_allow_html=True)
st.markdown('<p style="color: #94a3b8; font-size: 0.9rem;">Sample market information for Hubballi. Use it for demonstration and planning only; verify current local mandi prices before making financial decisions.</p>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Filter Section
category = st.selectbox("Filter by crop category", ["All", "Vegetable", "Fruit", "Grain"])

st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<div style="font-size: 1.5rem; font-weight: 600; display: flex; align-items: center; gap: 10px;">🧺 Crop Market Board</div>', unsafe_allow_html=True)
st.markdown('<p style="color: #94a3b8; font-size: 0.85rem;">Showing 46 crops for the selected demonstration market: Hubballi</p>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Display Cards in a Grid using columns
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
    </div>

</body>
</html>
