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

    </div>

</body>
</html>
