/**
 * BharatYatra - India Tourist Place Finder, Roadmaps & Travel Management
 * Simple, attractive, highly responsive frontend logic for all devices
 */

// Global State
const state = {
  places: [],
  filteredPlaces: [],
  bookings: [],
  selectedPlace: null,
  activeCategory: 'all',
  activeRegion: 'all',
  activeSort: 'rating',
  searchQuery: '',
  wishlist: new Set(JSON.parse(localStorage.getItem('by_wishlist') || '[]')),
  mainMap: null,
  roadmapMap: null,
  mapMarkers: [],
  currentLightboxIndex: 0,
  currentLightboxImages: [],
  activeItineraryIndex: 0
};

// DOM Init
document.addEventListener('DOMContentLoaded', () => {
  initApp();
  setupEventListeners();
});

async function initApp() {
  await Promise.all([
    fetchPlaces(),
    fetchBookings(),
    fetchStats()
  ]);

  initMainMap();
  setupCategoryPills();
  setupRegionPills();

  // Set default minimum booking date to tomorrow
  const tomorrow = new Date();
  tomorrow.setDate(tomorrow.getDate() + 1);
  const minDateStr = tomorrow.toISOString().split('T')[0];
  const dateInputs = document.querySelectorAll('input[type="date"]');
  dateInputs.forEach(input => {
    input.min = minDateStr;
    if (!input.value) input.value = minDateStr;
  });
}

// -------------------------------------------------------------
// Data Fetching & Sync
// -------------------------------------------------------------
async function fetchPlaces() {
  try {
    const res = await fetch('/api/places');
    const data = await res.json();
    if (data.success && data.places) {
      state.places = data.places;
      state.filteredPlaces = [...data.places];
      renderPlacesGrid();
      updateMapMarkers();
      populateRoadmapSelector();
    }
  } catch (err) {
    console.error('Failed to load places:', err);
    showToast('Failed to load destinations. Please check server.', 'error');
  }
}

async function fetchBookings() {
  try {
    const res = await fetch('/api/bookings');
    const data = await res.json();
    if (data.success && data.bookings) {
      state.bookings = data.bookings;
      renderBookings();
      updateBookingBadge();
    }
  } catch (err) {
    console.error('Failed to load bookings:', err);
  }
}

async function fetchStats() {
  try {
    const res = await fetch('/api/stats');
    const data = await res.json();
    if (data.success && data.stats) {
      const s = data.stats;
      const elDest = document.getElementById('stat-destinations');
      const elStates = document.getElementById('stat-states');
      const elBookings = document.getElementById('stat-bookings');
      const elRating = document.getElementById('stat-rating');

      if (elDest) elDest.innerText = `${s.totalDestinations}+`;
      if (elStates) elStates.innerText = `${s.supportedStates} States`;
      if (elBookings) elBookings.innerText = `${s.totalBookings}+ Passes`;
      if (elRating) elRating.innerText = `${s.averageRating} ★`;
    }
  } catch (err) {
    console.error('Failed to load stats:', err);
  }
}

// -------------------------------------------------------------
// Search & Filter Listeners
// -------------------------------------------------------------
function setupEventListeners() {
  const searchInput = document.getElementById('global-search-input');
  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      state.searchQuery = e.target.value.trim().toLowerCase();
      applyFilters();
    });
  }

  const sortSelect = document.getElementById('sort-filter');
  if (sortSelect) {
    sortSelect.addEventListener('change', (e) => {
      state.activeSort = e.target.value;
      applyFilters();
    });
  }

  // Booking quantity input
  const bookingQty = document.getElementById('booking-quantity');
  if (bookingQty) {
    bookingQty.addEventListener('input', recalculateBookingPrice);
  }

  const bookingTier = document.getElementById('booking-tier-select');
  if (bookingTier) {
    bookingTier.addEventListener('change', recalculateBookingPrice);
  }

  // Add Place Form
  const addPlaceForm = document.getElementById('add-place-form');
  if (addPlaceForm) {
    addPlaceForm.addEventListener('submit', handleAddPlaceSubmit);
  }

  // Escape to close modals
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeAllModals();
  });
}

function setupCategoryPills() {
  const pills = document.querySelectorAll('.category-pill');
  pills.forEach(pill => {
    pill.addEventListener('click', () => {
      pills.forEach(p => p.classList.remove('active-cat', 'bg-orange-600', 'text-white'));
      pills.forEach(p => p.classList.add('bg-white', 'text-slate-700', 'border-slate-200'));

      pill.classList.remove('bg-white', 'text-slate-700', 'border-slate-200');
      pill.classList.add('active-cat', 'bg-orange-600', 'text-white');

      state.activeCategory = pill.getAttribute('data-category') || 'all';
      applyFilters();
    });
  });
}

function setupRegionPills() {
  const pills = document.querySelectorAll('.region-pill');
  pills.forEach(pill => {
    pill.addEventListener('click', () => {
      pills.forEach(p => p.classList.remove('active-reg', 'bg-slate-900', 'text-white'));
      pills.forEach(p => p.classList.add('bg-slate-100', 'text-slate-700'));

      pill.classList.remove('bg-slate-100', 'text-slate-700');
      pill.classList.add('active-reg', 'bg-slate-900', 'text-white');

      state.activeRegion = pill.getAttribute('data-region') || 'all';
      applyFilters();
    });
  });
}

function applyFilters() {
  let list = [...state.places];

  // Search query
  if (state.searchQuery) {
    const q = state.searchQuery;
    list = list.filter(p => 
      p.name.toLowerCase().includes(q) ||
      p.state.toLowerCase().includes(q) ||
      p.region.toLowerCase().includes(q) ||
      p.category.toLowerCase().includes(q) ||
      p.tagline.toLowerCase().includes(q) ||
      (p.thingsToDo && p.thingsToDo.some(t => t.toLowerCase().includes(q)))
    );
  }

  // Category filter
  if (state.activeCategory && state.activeCategory !== 'all') {
    list = list.filter(p => p.category.toLowerCase() === state.activeCategory.toLowerCase());
  }

  // Region filter
  if (state.activeRegion && state.activeRegion !== 'all') {
    list = list.filter(p => p.region.toLowerCase() === state.activeRegion.toLowerCase());
  }

  // Sorting
  if (state.activeSort === 'price_low') {
    list.sort((a, b) => (a.entryFee || 0) - (b.entryFee || 0));
  } else if (state.activeSort === 'price_high') {
    list.sort((a, b) => (b.entryFee || 0) - (a.entryFee || 0));
  } else if (state.activeSort === 'reviews') {
    list.sort((a, b) => (b.reviewsCount || 0) - (a.reviewsCount || 0));
  } else {
    // Top rated default
    list.sort((a, b) => (b.rating || 0) - (a.rating || 0));
  }

  state.filteredPlaces = list;
  renderPlacesGrid();

  const countBadge = document.getElementById('results-count');
  if (countBadge) {
    countBadge.innerText = `${list.length} Beautiful Place${list.length === 1 ? '' : 's'} in India`;
  }
}

function resetFilters() {
  state.searchQuery = '';
  state.activeCategory = 'all';
  state.activeRegion = 'all';
  state.activeSort = 'rating';

  const searchInput = document.getElementById('global-search-input');
  if (searchInput) searchInput.value = '';

  const catPills = document.querySelectorAll('.category-pill');
  catPills.forEach((p, idx) => {
    if (idx === 0) {
      p.classList.add('active-cat', 'bg-orange-600', 'text-white');
      p.classList.remove('bg-white', 'text-slate-700', 'border-slate-200');
    } else {
      p.classList.remove('active-cat', 'bg-orange-600', 'text-white');
      p.classList.add('bg-white', 'text-slate-700', 'border-slate-200');
    }
  });

  const regPills = document.querySelectorAll('.region-pill');
  regPills.forEach((p, idx) => {
    if (idx === 0) {
      p.classList.add('active-reg', 'bg-slate-900', 'text-white');
      p.classList.remove('bg-slate-100', 'text-slate-700');
    } else {
      p.classList.remove('active-reg', 'bg-slate-900', 'text-white');
      p.classList.add('bg-slate-100', 'text-slate-700');
    }
  });

  applyFilters();
}

function quickSearchLocation(loc) {
  const searchInput = document.getElementById('global-search-input');
  if (searchInput) {
    searchInput.value = loc;
    state.searchQuery = loc.toLowerCase();
    applyFilters();
    scrollToSection('places-section');
  }
}

// -------------------------------------------------------------
// Render Places Grid (Responsive Cards)
// -------------------------------------------------------------
function renderPlacesGrid() {
  const container = document.getElementById('places-grid');
  if (!container) return;

  if (state.filteredPlaces.length === 0) {
    container.innerHTML = `
      <div class="col-span-full py-16 text-center bg-white rounded-3xl border border-slate-200 p-8 shadow-sm">
        <div class="w-16 h-16 rounded-full bg-orange-50 text-orange-600 flex items-center justify-center mx-auto mb-4 text-2xl">
          <i class="fa-solid fa-compass"></i>
        </div>
        <h3 class="text-xl font-bold text-slate-900 mb-2 font-heading">No Indian destination found</h3>
        <p class="text-slate-500 text-sm max-w-md mx-auto mb-6">
          Try typing a state or city like "Jaipur", "Kerala", "Ladakh", "Varanasi", "Goa", or "Kashmir".
        </p>
        <button onclick="resetFilters()" class="px-5 py-2.5 bg-orange-600 hover:bg-orange-700 text-white font-bold rounded-xl text-xs transition">
          Reset All Filters
        </button>
      </div>
    `;
    return;
  }

  container.innerHTML = state.filteredPlaces.map(place => {
    const isWishlisted = state.wishlist.has(place.id);
    const photoCount = (place.gallery && place.gallery.length) || 1;
    const hotelCount = (place.nearbyHotels && place.nearbyHotels.length) || 0;

    return `
      <div class="india-card bg-white rounded-3xl overflow-hidden border border-slate-200 shadow-sm flex flex-col group">
        
        <!-- Image with Tag Badges -->
        <div class="relative h-60 sm:h-64 overflow-hidden cursor-pointer" onclick="openRoadmapView('${place.id}')">
          <img 
            src="${place.heroImage}" 
            alt="${place.name}" 
            loading="lazy"
            class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105"
            onerror="this.src='https://images.unsplash.com/photo-1524492412937-b28074a5d7da?auto=format&fit=crop&w=800&q=80'"
          />
          <div class="absolute inset-0 bg-gradient-to-t from-slate-950/85 via-black/20 to-transparent"></div>

          <!-- Top Pills -->
          <div class="absolute top-3.5 left-3.5 flex items-center gap-2">
            <span class="px-3 py-1 rounded-full text-xs font-bold bg-white/95 text-slate-800 shadow-sm backdrop-blur">
              ${place.category}
            </span>
            <span class="px-2.5 py-1 rounded-full text-xs font-bold bg-amber-500 text-white flex items-center gap-1 shadow-sm">
              ★ ${place.rating}
            </span>
          </div>

          <!-- Top Right: Wishlist & Gallery Counter -->
          <div class="absolute top-3.5 right-3.5 flex items-center gap-2">
            <button 
              onclick="event.stopPropagation(); toggleWishlist('${place.id}')" 
              class="w-9 h-9 rounded-full ${isWishlisted ? 'bg-rose-500 text-white' : 'bg-white/90 text-slate-700 hover:text-rose-500'} backdrop-blur flex items-center justify-center transition shadow-sm"
              title="Save to favorites"
            >
              <i class="fa-${isWishlisted ? 'solid' : 'regular'} fa-heart text-sm"></i>
            </button>
            <span class="px-2.5 py-1 rounded-full text-xs font-semibold bg-black/60 text-white backdrop-blur flex items-center gap-1">
              <i class="fa-regular fa-image text-[11px]"></i> ${photoCount}
            </span>
          </div>

          <!-- Bottom Location Overlay -->
          <div class="absolute bottom-3.5 left-3.5 right-3.5 text-white">
            <div class="flex items-center gap-1.5 text-xs font-semibold text-amber-300 mb-1">
              <i class="fa-solid fa-location-dot"></i>
              <span>${place.state}, India</span>
            </div>
            <h3 class="text-xl sm:text-2xl font-black font-heading line-clamp-1 group-hover:text-amber-300 transition-colors">
              ${place.name}
            </h3>
          </div>
        </div>

        <!-- Card Body -->
        <div class="p-5 flex-1 flex flex-col justify-between">
          <div>
            <p class="text-slate-600 text-xs sm:text-sm line-clamp-2 leading-relaxed mb-4">
              ${place.tagline || place.description}
            </p>

            <!-- Quick Experience Badges -->
            <div class="flex flex-wrap gap-1.5 mb-4">
              <span class="px-2.5 py-1 bg-orange-50 text-orange-700 rounded-lg text-xs font-semibold flex items-center gap-1">
                <i class="fa-solid fa-route text-[10px]"></i> Roadmaps & Itineraries
              </span>
              <span class="px-2.5 py-1 bg-sky-50 text-sky-700 rounded-lg text-xs font-semibold flex items-center gap-1">
                <i class="fa-solid fa-hotel text-[10px]"></i> ${hotelCount} Hotels
              </span>
            </div>
          </div>

          <!-- Price & Primary Action Buttons -->
          <div class="pt-3 border-t border-slate-100 flex items-center justify-between gap-3">
            <div>
              <span class="text-[10px] font-bold uppercase tracking-wider text-slate-400 block">Entry / Pass</span>
              <div class="flex items-baseline gap-1">
                <span class="text-lg sm:text-xl font-extrabold text-slate-900">
                  ${place.entryFee === 0 ? 'Free Entry' : `₹${place.entryFee}`}
                </span>
                ${place.entryFee > 0 ? '<span class="text-[11px] text-slate-500">/ person</span>' : ''}
              </div>
            </div>

            <div class="flex items-center gap-2">
              <button 
                onclick="openRoadmapView('${place.id}')" 
                class="px-3.5 py-2.5 rounded-xl border border-orange-200 hover:border-orange-500 hover:bg-orange-50 text-orange-700 font-bold text-xs transition flex items-center gap-1.5"
                title="View travel roadmaps and itineraries"
              >
                <i class="fa-solid fa-map"></i>
                <span class="hidden sm:inline">Roadmap</span>
              </button>

              <button 
                onclick="openBookingModal('${place.id}')" 
                class="px-4 py-2.5 rounded-xl bg-slate-900 hover:bg-orange-600 text-white font-bold text-xs transition shadow-sm flex items-center gap-1.5"
              >
                <i class="fa-solid fa-ticket text-xs"></i>
                <span>Book Pass</span>
              </button>
            </div>
          </div>

        </div>

      </div>
    `;
  }).join('');
}

function toggleWishlist(placeId) {
  if (state.wishlist.has(placeId)) {
    state.wishlist.delete(placeId);
    showToast('Removed from saved places', 'info');
  } else {
    state.wishlist.add(placeId);
    showToast('Saved to your favorite Indian places!', 'success');
  }
  localStorage.setItem('by_wishlist', JSON.stringify([...state.wishlist]));
  renderPlacesGrid();
}

// -------------------------------------------------------------
// LOCATION ROADMAP & LIFESPAN ITINERARY DRAWER / MODAL
// (The core feature requested by the user!)
// -------------------------------------------------------------
function openRoadmapView(placeId) {
  const place = state.places.find(p => p.id === placeId);
  if (!place) return;
  state.selectedPlace = place;

  const modal = document.getElementById('roadmap-modal');
  if (!modal) return;

  // Header Details
  document.getElementById('roadmap-place-title').innerText = place.name;
  document.getElementById('roadmap-place-subtitle').innerText = `${place.state}, India • ${place.category} • ${place.rating} ★ (${place.reviewsCount.toLocaleString()} reviews)`;
  document.getElementById('roadmap-place-hero').src = place.heroImage;
  document.getElementById('roadmap-place-desc').innerText = place.description;

  // Weather badge
  const weatherEl = document.getElementById('roadmap-weather-badge');
  if (weatherEl && place.weather) {
    weatherEl.innerHTML = `
      <i class="fa-solid fa-${place.weather.icon || 'sun'} text-amber-500 mr-1.5"></i>
      <span>${place.weather.temp} - ${place.weather.condition}</span>
    `;
  }

  // Best Time
  const bestTimeEl = document.getElementById('roadmap-best-time');
  if (bestTimeEl) bestTimeEl.innerText = place.bestTimeToVisit || 'October to March';

  // 1. How to Reach Roadmap (Flight, Train, Road)
  renderHowToReachRoadmap(place);

  // 2. Lifespan Itineraries (1-2 Days, 3-4 Days, 5+ Days)
  renderLifespanItineraries(place);

  // 3. Suggestions & Things to Do
  renderThingsToDo(place);

  // 4. Photo Gallery Thumbnails
  renderRoadmapGallery(place);

  // 5. Nearby Hotels
  renderRoadmapHotels(place);

  // 6. Nearby Sights
  renderRoadmapNearbyPlaces(place);

  // Switch to default tab
  switchRoadmapTab('itinerary');

  // Open Modal
  modal.classList.remove('hidden');
  document.body.classList.add('overflow-hidden');

  // Load Leaflet mini roadmap
  setTimeout(() => initRoadmapMiniMap(place), 200);
}

function switchRoadmapTab(tabName) {
  const tabs = ['itinerary', 'reach', 'hotels', 'sights', 'gallery'];
  tabs.forEach(t => {
    const btn = document.getElementById(`tab-btn-${t}`);
    const section = document.getElementById(`tab-content-${t}`);
    if (btn && section) {
      if (t === tabName) {
        btn.classList.add('bg-orange-600', 'text-white', 'shadow-sm');
        btn.classList.remove('bg-slate-100', 'text-slate-700');
        section.classList.remove('hidden');
      } else {
        btn.classList.remove('bg-orange-600', 'text-white', 'shadow-sm');
        btn.classList.add('bg-slate-100', 'text-slate-700');
        section.classList.add('hidden');
      }
    }
  });
}

function renderHowToReachRoadmap(place) {
  const container = document.getElementById('roadmap-how-to-reach');
  if (!container) return;

  const h = place.howToReach || {};

  container.innerHTML = `
    <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
      
      <!-- By Flight -->
      <div class="p-4 rounded-2xl bg-sky-50/70 border border-sky-100 flex flex-col justify-between">
        <div>
          <div class="w-10 h-10 rounded-xl bg-sky-600 text-white flex items-center justify-center text-base mb-3 shadow-sm">
            <i class="fa-solid fa-plane-departure"></i>
          </div>
          <h4 class="font-bold text-slate-900 text-sm mb-1 font-heading">By Flight (Airways)</h4>
          <p class="text-xs text-slate-600 leading-relaxed">${h.flight || 'Nearest airport connects to Delhi, Mumbai, and Bengaluru with daily scheduled flights.'}</p>
        </div>
        <span class="mt-3 text-[11px] font-semibold text-sky-700 flex items-center gap-1">
          <i class="fa-solid fa-clock text-xs"></i> Fastest Option
        </span>
      </div>

      <!-- By Train -->
      <div class="p-4 rounded-2xl bg-amber-50/70 border border-amber-100 flex flex-col justify-between">
        <div>
          <div class="w-10 h-10 rounded-xl bg-amber-600 text-white flex items-center justify-center text-base mb-3 shadow-sm">
            <i class="fa-solid fa-train"></i>
          </div>
          <h4 class="font-bold text-slate-900 text-sm mb-1 font-heading">By Train (Railways)</h4>
          <p class="text-xs text-slate-600 leading-relaxed">${h.train || 'Major junction connecting Vande Bharat, Rajdhani, and express trains from all metros.'}</p>
        </div>
        <span class="mt-3 text-[11px] font-semibold text-amber-800 flex items-center gap-1">
          <i class="fa-solid fa-shield-halved text-xs"></i> Scenic & Budget Friendly
        </span>
      </div>

      <!-- By Road -->
      <div class="p-4 rounded-2xl bg-emerald-50/70 border border-emerald-100 flex flex-col justify-between">
        <div>
          <div class="w-10 h-10 rounded-xl bg-emerald-600 text-white flex items-center justify-center text-base mb-3 shadow-sm">
            <i class="fa-solid fa-car-side"></i>
          </div>
          <h4 class="font-bold text-slate-900 text-sm mb-1 font-heading">By Road & Highway</h4>
          <p class="text-xs text-slate-600 leading-relaxed">${h.road || 'Well-maintained National Highway networks and scenic state expressways with rest plazas.'}</p>
        </div>
        <span class="mt-3 text-[11px] font-semibold text-emerald-800 flex items-center gap-1">
          <i class="fa-solid fa-route text-xs"></i> Great for Road Trips
        </span>
      </div>

    </div>
  `;
}

function renderLifespanItineraries(place) {
  const tabsContainer = document.getElementById('itinerary-duration-tabs');
  const planContainer = document.getElementById('itinerary-days-timeline');
  if (!tabsContainer || !planContainer) return;

  const itineraries = place.itineraries || [];
  if (itineraries.length === 0) {
    planContainer.innerHTML = `<p class="text-slate-500 text-sm py-4">Custom itinerary available upon request.</p>`;
    return;
  }

  // Duration Selector Tabs
  tabsContainer.innerHTML = itineraries.map((it, idx) => `
    <button 
      onclick="setItineraryIndex(${idx})"
      class="px-4 py-2 rounded-xl text-xs font-bold transition flex items-center gap-1.5 ${idx === state.activeItineraryIndex ? 'bg-slate-900 text-white shadow-sm' : 'bg-slate-100 hover:bg-slate-200 text-slate-700'}"
    >
      <i class="fa-regular fa-clock text-xs"></i>
      <span>${it.duration}</span>
    </button>
  `).join('');

  const currentItinerary = itineraries[state.activeItineraryIndex] || itineraries[0];

  // Render Day-by-Day sequence
  planContainer.innerHTML = `
    <div class="mb-3 flex items-center justify-between">
      <span class="text-xs font-bold text-orange-700 bg-orange-100 px-3 py-1 rounded-full uppercase tracking-wider">
        Recommended Roadmap: ${currentItinerary.duration}
      </span>
      <span class="text-xs text-slate-400 font-medium">${(currentItinerary.plan || []).length} Days Total</span>
    </div>

    <div class="space-y-4 timeline-stem pt-2">
      ${(currentItinerary.plan || []).map((day, i) => `
        <div class="relative pl-10">
          <div class="absolute left-2.5 top-1.5 w-6 h-6 rounded-full bg-orange-600 text-white flex items-center justify-center text-xs font-extrabold shadow z-10">
            ${i + 1}
          </div>
          <div class="bg-white p-4 rounded-2xl border border-slate-200 shadow-sm">
            <div class="flex items-center justify-between mb-1">
              <span class="text-xs font-bold text-orange-600 uppercase tracking-wider">${day.day}</span>
              <span class="text-xs font-bold text-slate-800">${day.title}</span>
            </div>
            <p class="text-xs sm:text-sm text-slate-600 leading-relaxed mt-1">
              ${day.activities}
            </p>
          </div>
        </div>
      `).join('')}
    </div>
  `;
}

function setItineraryIndex(index) {
  state.activeItineraryIndex = index;
  if (state.selectedPlace) {
    renderLifespanItineraries(state.selectedPlace);
  }
}

function renderThingsToDo(place) {
  const container = document.getElementById('roadmap-things-to-do');
  if (!container) return;

  const suggestions = place.thingsToDo || [];
  container.innerHTML = suggestions.map((s, idx) => `
    <div class="p-3.5 rounded-2xl bg-slate-50 border border-slate-200/80 flex items-start gap-3">
      <div class="w-7 h-7 rounded-lg bg-orange-100 text-orange-600 flex items-center justify-center text-xs font-bold flex-shrink-0 mt-0.5">
        ${idx + 1}
      </div>
      <p class="text-xs sm:text-sm text-slate-700 font-medium leading-relaxed">${s}</p>
    </div>
  `).join('');
}

function renderRoadmapGallery(place) {
  const container = document.getElementById('roadmap-gallery-grid');
  if (!container || !place.gallery) return;

  container.innerHTML = place.gallery.map((url, idx) => `
    <div 
      class="h-32 sm:h-36 rounded-2xl overflow-hidden relative cursor-pointer group border border-slate-200"
      onclick="openLightbox('${place.id}', ${idx})"
    >
      <img src="${url}" class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110" />
      <div class="absolute inset-0 bg-black/20 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center text-white">
        <i class="fa-solid fa-expand text-lg"></i>
      </div>
    </div>
  `).join('');
}

function renderRoadmapHotels(place) {
  const container = document.getElementById('roadmap-hotels-list');
  if (!container) return;

  const hotels = place.nearbyHotels || [];
  if (hotels.length === 0) {
    container.innerHTML = `<p class="text-slate-500 text-xs py-4">Hotel recommendations are being updated.</p>`;
    return;
  }

  container.innerHTML = hotels.map(h => `
    <div class="bg-white p-4 rounded-2xl border border-slate-200 flex flex-col sm:flex-row gap-4 hover:shadow-md transition">
      <div class="w-full sm:w-44 h-32 rounded-xl overflow-hidden relative flex-shrink-0">
        <img src="${h.image}" class="w-full h-full object-cover" />
        <span class="absolute top-2 left-2 px-2 py-0.5 rounded-md bg-amber-500 text-white text-xs font-bold shadow">
          ★ ${h.rating}
        </span>
      </div>
      <div class="flex-1 flex flex-col justify-between">
        <div>
          <div class="flex items-start justify-between gap-2">
            <div>
              <h4 class="font-bold text-slate-900 text-base font-heading">${h.name}</h4>
              <p class="text-xs text-orange-600 font-medium flex items-center gap-1 mt-0.5">
                <i class="fa-solid fa-location-dot"></i> ${h.distance}
              </p>
            </div>
            <div class="text-right">
              <span class="text-lg font-black text-slate-900">₹${h.pricePerNight.toLocaleString()}</span>
              <span class="text-[11px] text-slate-400 block">/ night</span>
            </div>
          </div>
          <div class="flex flex-wrap gap-1.5 mt-2.5">
            ${(h.amenities || []).map(a => `
              <span class="px-2 py-0.5 rounded bg-slate-100 text-slate-600 text-[11px] font-medium">${a}</span>
            `).join('')}
          </div>
        </div>
        <div class="mt-3 pt-2.5 border-t border-slate-100 flex items-center justify-between">
          <span class="text-xs text-emerald-600 font-bold flex items-center gap-1">
            <i class="fa-solid fa-check"></i> Free Cancellation Available
          </span>
          <button 
            onclick="simulateBookingRoom('${h.name}', ${h.pricePerNight})" 
            class="px-4 py-1.5 bg-slate-900 hover:bg-orange-600 text-white text-xs font-bold rounded-xl transition"
          >
            Reserve Stay
          </button>
        </div>
      </div>
    </div>
  `).join('');
}

function renderRoadmapNearbyPlaces(place) {
  const container = document.getElementById('roadmap-nearby-sights');
  if (!container) return;

  const sights = place.nearbyPlaces || [];
  if (sights.length === 0) {
    container.innerHTML = `<p class="text-slate-500 text-xs py-4">Nearby sights data updating.</p>`;
    return;
  }

  container.innerHTML = sights.map(s => `
    <div class="bg-white p-4 rounded-2xl border border-slate-200 flex flex-col sm:flex-row gap-4 hover:shadow-md transition">
      <div class="w-full sm:w-36 h-28 rounded-xl overflow-hidden relative flex-shrink-0">
        <img src="${s.image}" class="w-full h-full object-cover" />
        <span class="absolute top-2 left-2 px-2 py-0.5 rounded bg-black/70 text-white text-[10px] font-medium backdrop-blur">
          ${s.distance}
        </span>
      </div>
      <div class="flex-1 flex flex-col justify-between">
        <div>
          <span class="text-[10px] font-bold text-orange-600 uppercase tracking-wider">${s.category}</span>
          <h4 class="font-bold text-slate-900 text-sm mt-0.5">${s.name}</h4>
          <p class="text-xs text-slate-600 mt-1 leading-relaxed">${s.description}</p>
        </div>
        <div class="mt-2 text-xs text-amber-500 font-bold flex items-center gap-1">
          <i class="fa-solid fa-star"></i> ${s.rating || 4.8} / 5.0
        </div>
      </div>
    </div>
  `).join('');
}

function simulateBookingRoom(name, price) {
  showToast(`Connecting to partner portal for ${name} (₹${price.toLocaleString()}/night)...`, 'success');
}

// -------------------------------------------------------------
// Interactive Roadmap Leaflet Mini-Map
// -------------------------------------------------------------
function initRoadmapMiniMap(place) {
  const container = document.getElementById('roadmap-mini-map');
  if (!container || typeof L === 'undefined') return;

  if (state.roadmapMap) {
    state.roadmapMap.remove();
  }

  state.roadmapMap = L.map('roadmap-mini-map', {
    center: [place.coordinates.lat, place.coordinates.lng],
    zoom: 12,
    scrollWheelZoom: false
  });

  L.tileLayer('https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png', {
    maxZoom: 18
  }).addTo(state.roadmapMap);

  // Landmark Marker
  const mainIcon = L.divIcon({
    className: 'main-pin',
    html: `
      <div class="w-9 h-9 rounded-full bg-orange-600 border-2 border-white shadow-lg flex items-center justify-center text-white text-xs font-bold animate-bounce">
        <i class="fa-solid fa-monument"></i>
      </div>
    `,
    iconSize: [36, 36],
    iconAnchor: [18, 36]
  });

  L.marker([place.coordinates.lat, place.coordinates.lng], { icon: mainIcon })
    .bindPopup(`<b>${place.name}</b><br><span class="text-xs text-slate-500">${place.state}</span>`)
    .addTo(state.roadmapMap);

  // Plot hotels
  (place.nearbyHotels || []).forEach((h, i) => {
    const latOffset = (i === 0 ? 0.006 : (i === 1 ? -0.005 : 0.004));
    const lngOffset = (i === 0 ? 0.005 : (i === 1 ? -0.006 : -0.005));

    const hIcon = L.divIcon({
      className: 'hotel-pin',
      html: `
        <div class="px-2 py-0.5 rounded-md bg-slate-900 text-white text-[10px] font-bold shadow flex items-center gap-1">
          <i class="fa-solid fa-hotel text-amber-400"></i> ₹${h.pricePerNight}
        </div>
      `,
      iconSize: [65, 22]
    });

    L.marker([place.coordinates.lat + latOffset, place.coordinates.lng + lngOffset], { icon: hIcon })
      .bindPopup(`<b>${h.name}</b><br><span class="text-xs text-orange-600">${h.distance}</span>`)
      .addTo(state.roadmapMap);
  });
}

function populateRoadmapSelector() {
  const select = document.getElementById('roadmap-quick-selector');
  if (!select) return;

  select.innerHTML = state.places.map((p, idx) => `
    <option value="${p.id}" ${idx === 0 ? 'selected' : ''}>
      ${p.name} (${p.state})
    </option>
  `).join('');

  select.addEventListener('change', (e) => {
    openRoadmapView(e.target.value);
  });
}

// -------------------------------------------------------------
// Interactive Leaflet Global India Map
// -------------------------------------------------------------
function initMainMap() {
  const container = document.getElementById('leaflet-map');
  if (!container || typeof L === 'undefined') return;

  // Center on India
  state.mainMap = L.map('leaflet-map', {
    center: [22.5, 78.9],
    zoom: 5,
    scrollWheelZoom: false
  });

  L.tileLayer('https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png', {
    attribution: '&copy; CartoDB & OpenStreetMap',
    maxZoom: 18
  }).addTo(state.mainMap);

  updateMapMarkers();
}

function updateMapMarkers() {
  if (!state.mainMap || typeof L === 'undefined') return;

  state.mapMarkers.forEach(m => state.mainMap.removeLayer(m));
  state.mapMarkers = [];

  state.places.forEach(place => {
    if (!place.coordinates || !place.coordinates.lat) return;

    const customPin = L.divIcon({
      className: 'custom-pin',
      html: `
        <div class="w-8 h-8 rounded-full bg-orange-600 border-2 border-white shadow-md flex items-center justify-center text-white text-xs font-bold hover:scale-125 transition-transform">
          <i class="fa-solid fa-map-pin"></i>
        </div>
      `,
      iconSize: [32, 32],
      iconAnchor: [16, 32],
      popupAnchor: [0, -30]
    });

    const marker = L.marker([place.coordinates.lat, place.coordinates.lng], { icon: customPin }).addTo(state.mainMap);

    const popupHtml = `
      <div class="w-60 overflow-hidden rounded-xl bg-white shadow">
        <img src="${place.heroImage}" class="w-full h-24 object-cover" />
        <div class="p-3">
          <span class="text-[10px] font-bold text-orange-600 uppercase tracking-wider">${place.category}</span>
          <h4 class="font-bold text-slate-900 text-sm line-clamp-1 mt-0.5">${place.name}</h4>
          <p class="text-xs text-slate-500">${place.state}, India</p>
          <div class="mt-2 pt-2 border-t border-slate-100 flex items-center justify-between">
            <span class="text-xs font-bold text-slate-800">${place.entryFee === 0 ? 'Free' : `₹${place.entryFee}`}</span>
            <button 
              onclick="openRoadmapView('${place.id}')"
              class="px-2.5 py-1 bg-orange-600 hover:bg-orange-700 text-white font-bold text-xs rounded-lg"
            >
              Roadmap
            </button>
          </div>
        </div>
      </div>
    `;

    marker.bindPopup(popupHtml);
    state.mapMarkers.push(marker);
  });
}

// -------------------------------------------------------------
// Ticket Booking Flow in INR (₹)
// -------------------------------------------------------------
function openBookingModal(placeId, selectedTierId = null) {
  const place = state.places.find(p => p.id === placeId);
  if (!place) return;
  state.selectedPlace = place;

  const modal = document.getElementById('booking-modal');
  if (!modal) return;

  document.getElementById('booking-dest-id').value = place.id;
  document.getElementById('booking-dest-image').src = place.heroImage;
  document.getElementById('booking-dest-name').innerText = place.name;
  document.getElementById('booking-dest-location').innerText = `${place.state}, India`;
  document.getElementById('booking-dest-rating').innerText = `${place.rating} ★`;

  const tierSelect = document.getElementById('booking-tier-select');
  if (tierSelect && place.ticketTiers) {
    tierSelect.innerHTML = place.ticketTiers.map(t => `
      <option value="${t.id}" data-price="${t.price}" data-name="${t.name}" ${selectedTierId === t.id ? 'selected' : ''}>
        ${t.name} — ₹${t.price} / person
      </option>
    `).join('');
  }

  const qty = document.getElementById('booking-quantity');
  if (qty) qty.value = 1;

  recalculateBookingPrice();

  modal.classList.remove('hidden');
  document.body.classList.add('overflow-hidden');
}

function recalculateBookingPrice() {
  const tierSelect = document.getElementById('booking-tier-select');
  const qtyInput = document.getElementById('booking-quantity');
  if (!tierSelect || !qtyInput) return;

  const opt = tierSelect.options[tierSelect.selectedIndex];
  const unitPrice = opt ? parseFloat(opt.getAttribute('data-price') || 100) : 100;
  const quantity = Math.max(1, parseInt(qtyInput.value) || 1);

  const subtotal = unitPrice * quantity;
  const serviceFee = 30.0; // standard low convenience fee in ₹
  const discount = subtotal >= 1000 ? 100.0 : 0.0;
  const total = subtotal + serviceFee - discount;

  document.getElementById('summary-unit-price').innerText = `₹${unitPrice.toFixed(0)}`;
  document.getElementById('summary-qty').innerText = quantity;
  document.getElementById('summary-subtotal').innerText = `₹${subtotal.toFixed(0)}`;
  document.getElementById('summary-service-fee').innerText = `₹${serviceFee.toFixed(0)}`;

  const discountRow = document.getElementById('summary-discount-row');
  if (discountRow) {
    if (discount > 0) {
      discountRow.classList.remove('hidden');
      document.getElementById('summary-discount').innerText = `-₹${discount.toFixed(0)}`;
    } else {
      discountRow.classList.add('hidden');
    }
  }

  document.getElementById('summary-total-price').innerText = `₹${total.toFixed(0)}`;
}

async function handleBookingFormSubmit(event) {
  event.preventDefault();
  const place = state.selectedPlace;
  if (!place) return;

  const tierSelect = document.getElementById('booking-tier-select');
  const opt = tierSelect.options[tierSelect.selectedIndex];
  const unitPrice = parseFloat(opt.getAttribute('data-price') || 100);
  const tierName = opt.getAttribute('data-name') || opt.text;
  const quantity = parseInt(document.getElementById('booking-quantity').value) || 1;

  const subtotal = unitPrice * quantity;
  const serviceFee = 30.0;
  const discount = subtotal >= 1000 ? 100.0 : 0.0;
  const totalAmount = subtotal + serviceFee - discount;

  const payload = {
    placeId: place.id,
    placeName: place.name,
    placeLocation: `${place.state}, India`,
    placeImage: place.heroImage,
    tierId: tierSelect.value,
    tierName: tierName,
    unitPrice: unitPrice,
    quantity: quantity,
    subtotal: subtotal,
    serviceFee: serviceFee,
    discount: discount,
    totalAmount: totalAmount,
    currency: 'INR',
    travelDate: document.getElementById('booking-travel-date').value,
    timeSlot: document.getElementById('booking-time-slot').value,
    customerName: document.getElementById('booking-guest-name').value,
    customerEmail: document.getElementById('booking-guest-email').value,
    customerPhone: document.getElementById('booking-guest-phone').value,
    specialRequests: document.getElementById('booking-special-requests').value
  };

  const submitBtn = document.getElementById('booking-submit-btn');
  const origText = submitBtn.innerHTML;
  submitBtn.disabled = true;
  submitBtn.innerHTML = `<i class="fa-solid fa-circle-notch fa-spin"></i> Generating Pass...`;

  try {
    const res = await fetch('/api/bookings', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    const data = await res.json();
    if (data.success && data.booking) {
      state.bookings.unshift(data.booking);
      renderBookings();
      updateBookingBadge();

      // Confetti celebration
      if (typeof confetti === 'function') {
        confetti({ particleCount: 75, spread: 60, origin: { y: 0.6 } });
      }

      closeModal('booking-modal');
      event.target.reset();
      displayTicketVoucher(data.booking);
      showToast('Booking Confirmed! Your digital pass is ready.', 'success');
    } else {
      showToast(data.error || 'Booking error', 'error');
    }
  } catch (err) {
    showToast('Network error during booking', 'error');
  } finally {
    submitBtn.disabled = false;
    submitBtn.innerHTML = origText;
  }
}

// -------------------------------------------------------------
// Digital Perforated Pass Modal
// -------------------------------------------------------------
function displayTicketVoucher(booking) {
  const modal = document.getElementById('ticket-voucher-modal');
  if (!modal) return;

  document.getElementById('ticket-code-badge').innerText = booking.id;
  document.getElementById('ticket-qr-code-img').src = `https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=${encodeURIComponent(booking.qrCodeData || booking.id)}`;
  document.getElementById('ticket-place-title').innerText = booking.placeName;
  document.getElementById('ticket-place-location').innerText = booking.placeLocation;
  document.getElementById('ticket-traveler-name').innerText = booking.customerName;
  document.getElementById('ticket-travel-date').innerText = booking.travelDate;
  document.getElementById('ticket-time-slot').innerText = booking.timeSlot;
  document.getElementById('ticket-tier-name').innerText = booking.tierName;
  document.getElementById('ticket-quantity').innerText = `${booking.quantity} Traveler${booking.quantity > 1 ? 's' : ''}`;
  document.getElementById('ticket-total-paid').innerText = `₹${booking.totalAmount.toFixed(0)}`;
  document.getElementById('ticket-barcode-num').innerText = booking.id;

  const printBtn = document.getElementById('ticket-print-btn');
  if (printBtn) {
    printBtn.onclick = () => window.print();
  }

  modal.classList.remove('hidden');
  document.body.classList.add('overflow-hidden');
}

function displayTicketVoucherById(id) {
  const b = state.bookings.find(item => item.id === id);
  if (b) displayTicketVoucher(b);
}

// -------------------------------------------------------------
// Manage Bookings Dashboard
// -------------------------------------------------------------
function renderBookings() {
  const container = document.getElementById('bookings-list-container');
  if (!container) return;

  if (state.bookings.length === 0) {
    container.innerHTML = `
      <div class="text-center py-12 bg-white rounded-3xl border border-dashed border-slate-300 p-6">
        <div class="w-14 h-14 rounded-full bg-orange-50 text-orange-600 flex items-center justify-center mx-auto mb-3 text-xl">
          <i class="fa-solid fa-ticket"></i>
        </div>
        <h4 class="text-base font-bold text-slate-800 mb-1">No passes booked yet</h4>
        <p class="text-slate-500 text-xs max-w-sm mx-auto mb-4">Book entry passes or day tours to access digital QR passes here.</p>
        <button onclick="scrollToSection('places-section')" class="px-4 py-2 bg-orange-600 text-white rounded-xl text-xs font-bold transition">
          Find Places to Book
        </button>
      </div>
    `;
    return;
  }

  container.innerHTML = state.bookings.map(b => {
    const isCancelled = b.status === 'Cancelled';

    return `
      <div class="bg-white rounded-2xl border ${isCancelled ? 'border-rose-200 bg-rose-50/20' : 'border-slate-200'} p-4 sm:p-5 flex flex-col md:flex-row items-start md:items-center justify-between gap-4 shadow-sm hover:shadow transition">
        <div class="flex items-center gap-3.5">
          <img src="${b.placeImage || 'https://images.unsplash.com/photo-1524492412937-b28074a5d7da?auto=format&fit=crop&w=400&q=80'}" class="w-16 h-16 sm:w-20 sm:h-20 rounded-xl object-cover flex-shrink-0" />
          <div>
            <div class="flex items-center gap-2 mb-1">
              <span class="px-2 py-0.5 rounded-full text-[10px] font-extrabold ${isCancelled ? 'bg-rose-100 text-rose-700' : 'bg-emerald-100 text-emerald-800'}">
                ● ${b.status}
              </span>
              <span class="font-mono text-xs text-slate-500 font-bold">${b.id}</span>
            </div>
            <h4 class="font-bold text-slate-900 text-sm sm:text-base font-heading">${b.placeName}</h4>
            <p class="text-xs text-slate-500 mt-0.5">
              <i class="fa-regular fa-calendar text-orange-600 mr-1"></i>${b.travelDate} • ${b.timeSlot}
            </p>
            <p class="text-xs text-slate-600 mt-1">
              <b>${b.tierName}</b> (${b.quantity} Traveler${b.quantity > 1 ? 's' : ''})
            </p>
          </div>
        </div>

        <div class="flex items-center justify-between md:justify-end gap-3 w-full md:w-auto pt-3 md:pt-0 border-t md:border-t-0 border-slate-100">
          <div class="text-left md:text-right">
            <span class="text-base sm:text-lg font-black text-slate-900">₹${b.totalAmount.toFixed(0)}</span>
            <span class="text-[10px] text-slate-400 block">Total Paid</span>
          </div>

          <div class="flex items-center gap-2">
            <button 
              onclick="displayTicketVoucherById('${b.id}')"
              class="px-3 py-2 bg-slate-900 hover:bg-orange-600 text-white font-bold text-xs rounded-xl transition flex items-center gap-1.5"
            >
              <i class="fa-solid fa-qrcode"></i>
              <span>Pass</span>
            </button>

            ${!isCancelled ? `
              <button 
                onclick="promptReschedule('${b.id}')"
                class="p-2 rounded-xl border border-slate-200 hover:border-orange-400 text-slate-700 text-xs transition"
                title="Reschedule Date"
              >
                <i class="fa-solid fa-calendar-days text-orange-600"></i>
              </button>
              <button 
                onclick="promptCancel('${b.id}')"
                class="p-2 rounded-xl border border-slate-200 hover:border-rose-400 text-slate-700 hover:text-rose-600 text-xs transition"
                title="Cancel Booking"
              >
                <i class="fa-solid fa-xmark"></i>
              </button>
            ` : ''}
          </div>
        </div>
      </div>
    `;
  }).join('');
}

function updateBookingBadge() {
  const badge = document.getElementById('nav-bookings-count');
  const activeCount = state.bookings.filter(b => b.status === 'Confirmed').length;
  if (badge) {
    badge.innerText = activeCount;
    badge.classList.toggle('hidden', activeCount === 0);
  }
}

async function promptCancel(bookingId) {
  if (!confirm(`Cancel booking ${bookingId}? Full refund will be processed.`)) return;

  try {
    const res = await fetch(`/api/bookings/${bookingId}`, { method: 'DELETE' });
    const data = await res.json();
    if (data.success) {
      const idx = state.bookings.findIndex(b => b.id === bookingId);
      if (idx !== -1) state.bookings[idx].status = 'Cancelled';
      renderBookings();
      updateBookingBadge();
      showToast('Booking cancelled successfully', 'info');
    }
  } catch (err) {
    showToast('Failed to cancel booking', 'error');
  }
}

function promptReschedule(bookingId) {
  const booking = state.bookings.find(b => b.id === bookingId);
  if (!booking) return;

  const newDate = prompt(`Enter new visit date (YYYY-MM-DD):`, booking.travelDate);
  if (!newDate || newDate === booking.travelDate) return;

  if (!/^\d{4}-\d{2}-\d{2}$/.test(newDate)) {
    alert('Please enter date in YYYY-MM-DD format');
    return;
  }

  rescheduleApi(bookingId, newDate);
}

async function rescheduleApi(bookingId, newDate) {
  try {
    const res = await fetch(`/api/bookings/${bookingId}`, {
      method: 'PATCH',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ travelDate: newDate })
    });
    const data = await res.json();
    if (data.success) {
      const idx = state.bookings.findIndex(b => b.id === bookingId);
      if (idx !== -1) state.bookings[idx].travelDate = newDate;
      renderBookings();
      showToast(`Rescheduled to ${newDate}!`, 'success');
    }
  } catch (err) {
    showToast('Error rescheduling', 'error');
  }
}

// -------------------------------------------------------------
// Admin / Add Place
// -------------------------------------------------------------
function openAddPlaceModal() {
  const modal = document.getElementById('add-place-modal');
  if (modal) {
    modal.classList.remove('hidden');
    document.body.classList.add('overflow-hidden');
  }
}

async function handleAddPlaceSubmit(e) {
  e.preventDefault();
  const name = document.getElementById('new-place-name').value.trim();
  const stateVal = document.getElementById('new-place-state').value.trim();
  const region = document.getElementById('new-place-region').value;
  const category = document.getElementById('new-place-category').value;
  const fee = parseFloat(document.getElementById('new-place-fee').value) || 0;
  const image = document.getElementById('new-place-image').value.trim();
  const desc = document.getElementById('new-place-desc').value.trim();

  try {
    const res = await fetch('/api/places', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        name, state: stateVal, region, category, entryFee: fee, heroImage: image, description: desc
      })
    });
    const data = await res.json();
    if (data.success && data.place) {
      state.places.unshift(data.place);
      applyFilters();
      updateMapMarkers();
      closeModal('add-place-modal');
      e.target.reset();
      showToast(`'${name}' added to Indian destinations!`, 'success');
      scrollToSection('places-section');
    }
  } catch (err) {
    showToast('Failed to add place', 'error');
  }
}

// -------------------------------------------------------------
// Photo Lightbox
// -------------------------------------------------------------
function openLightbox(placeId, photoIndex = 0) {
  const place = state.places.find(p => p.id === placeId);
  if (!place || !place.gallery || place.gallery.length === 0) return;

  state.currentLightboxImages = place.gallery;
  state.currentLightboxIndex = photoIndex;

  const lightbox = document.getElementById('photo-lightbox');
  if (!lightbox) return;

  updateLightbox();
  lightbox.classList.remove('hidden');
  document.body.classList.add('overflow-hidden');
}

function updateLightbox() {
  const imgEl = document.getElementById('lightbox-image');
  const countEl = document.getElementById('lightbox-counter');
  if (!imgEl) return;

  imgEl.src = state.currentLightboxImages[state.currentLightboxIndex];
  if (countEl) countEl.innerText = `${state.currentLightboxIndex + 1} / ${state.currentLightboxImages.length}`;
}

function prevLightbox() {
  state.currentLightboxIndex = (state.currentLightboxIndex - 1 + state.currentLightboxImages.length) % state.currentLightboxImages.length;
  updateLightbox();
}

function nextLightbox() {
  state.currentLightboxIndex = (state.currentLightboxIndex + 1) % state.currentLightboxImages.length;
  updateLightbox();
}

// -------------------------------------------------------------
// Utilities & Modals
// -------------------------------------------------------------
function closeModal(id) {
  const el = document.getElementById(id);
  if (el) el.classList.add('hidden');
  document.body.classList.remove('overflow-hidden');
}

function closeAllModals() {
  ['roadmap-modal', 'booking-modal', 'ticket-voucher-modal', 'add-place-modal', 'photo-lightbox'].forEach(closeModal);
}

function scrollToSection(id) {
  const el = document.getElementById(id);
  if (el) el.scrollIntoView({ behavior: 'smooth' });
}

function showToast(message, type = 'info') {
  const toast = document.createElement('div');
  const colors = {
    success: 'bg-emerald-600 text-white',
    error: 'bg-rose-600 text-white',
    info: 'bg-slate-900 text-white'
  };

  toast.className = `fixed bottom-6 right-6 z-50 px-4 py-3 rounded-2xl shadow-xl flex items-center gap-2.5 text-xs sm:text-sm font-bold transition-all transform duration-300 translate-y-10 opacity-0 ${colors[type] || colors.info}`;
  toast.innerHTML = `
    <i class="fa-solid fa-${type === 'success' ? 'check-circle' : (type === 'error' ? 'triangle-exclamation' : 'circle-info')}"></i>
    <span>${message}</span>
  `;

  document.body.appendChild(toast);
  setTimeout(() => toast.classList.remove('translate-y-10', 'opacity-0'), 40);
  setTimeout(() => {
    toast.classList.add('translate-y-10', 'opacity-0');
    setTimeout(() => toast.remove(), 300);
  }, 3500);
}
