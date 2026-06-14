# Manjari Taxi

A premium cab booking and fleet management web application built with Django, vanilla HTML/CSS, and JavaScript. The application features a dynamic services list, fleet showcase, customer review submission, a comprehensive booking system, automated email notifications for new bookings, rate limiting on public forms to prevent spam, and a progressive web app (PWA) offline experience.

---

## Table of Contents
1. [Introduction & Tech Stack](#introduction--tech-stack)
2. [Project Architecture](#project-architecture)
3. [Setup & Installation](#setup--installation)
4. [Development & Asset Compilation](#development--asset-compilation)
5. [Completed Improvements](#completed-improvements)
6. [Future Database Normalization Recommendations](#future-database-normalization-recommendations)
7. [Running Tests](#running-tests)

---

## Introduction & Tech Stack

Manjari Taxi provides users with a seamless interface to explore taxi services, review the active vehicle fleet, submit custom testimonials, and book rides.

### Tech Stack
- **Backend**: Python 3.x, Django 5.x
- **Database**: PostgreSQL (Production) / SQLite3 (Local & Testing)
- **Frontend**: Semantic HTML5, Custom Responsive CSS3 (Flexbox/Grid), Vanilla JavaScript
- **Caching & Rate Limiting**: Django's caching framework (supporting Database / Memcached / Redis backends)
- **Progressive Web App (PWA)**: Service Worker supporting asset and page caching for offline mode
- **Asset Pipeline**: Node-free Python minification script for CSS and JS files

---

## Project Architecture

The codebase is organized into modular Django applications following the standard Model-View-Template (MVT) pattern:

```text
manjari_taxi/
├── config/                  # Project configuration settings, routing, and WSGI/ASGI entry points
│   ├── settings.py          # Environment-aware Django settings
│   └── urls.py              # Main URL route routing table
├── core/                    # Core business logic, pages, reviews, and utility modules
│   ├── models.py            # Models for Services, Vehicles, and Reviews
│   ├── views.py             # Home and review submission logic
│   ├── admin.py             # Django Admin registration for services, vehicles, and reviews
│   └── utils.py             # Core utilities including form rate-limiting logic
├── bookings/                # Booking workflow engine
│   ├── models.py            # Booking data structure
│   ├── views.py             # Dynamic booking form handlers and validation
│   ├── forms.py             # Form definitions (integrating DB query choices)
│   └── tests.py             # Integrated unit test suite for bookings
├── static/                  # Static assets (original source files)
│   ├── css/                 # Custom stylesheet (style.css)
│   └── js/                  # Interaction logic (main.js) and service-worker.js
├── staticfiles/             # Minified and compiled production static assets (style.min.css, main.min.js)
├── templates/               # Reusable HTML templates and partials
│   ├── base.html            # HTML structural shell with SEO and Google Fonts
│   └── partials/            # Component partials (navbar, hero, services, fleet, contact, etc.)
├── scripts/                 # Automation scripts (CSS/JS minifier)
└── manage.py                # Django administrative execution utility
```

---

## Setup & Installation

Follow these steps to set up the project locally:

### 1. Clone the Repository & Navigate to Project Root
```bash
cd manjari_taxi
```

### 2. Create and Activate a Python Virtual Environment
**On Windows:**
```powershell
python -m venv .venv
.venv\Scripts\activate
```
**On macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env` file in the project root directory (next to `manage.py`). You can copy the template from `.env.example`:
```bash
cp .env.example .env
```
Open `.env` and fill in the values:
- `SECRET_KEY`: A secure, randomly generated key for Django.
- `DEBUG`: Set to `True` for development, `False` for production.
- `ALLOWED_HOSTS`: A comma-separated list of allowed domains.
- `DATABASE_URL`: Your PostgreSQL connection string (defaults to SQLite if not provided).
- `EMAIL_HOST_USER` & `EMAIL_HOST_PASSWORD`: Credentials for the automated booking notification system.

### 5. Apply Database Migrations
```bash
python manage.py migrate
```

### 6. Create a Superuser (Optional - for admin access)
```bash
python manage.py createsuperuser
```

### 7. Run the Local Development Server
```bash
python manage.py runserver
```
The site will be available at `http://127.0.0.1:8000/`.

---

## Development & Asset Compilation

To keep page load speeds fast, the application loads minified styles and scripts (`style.min.css` and `main.min.js`).

If you make modifications to `static/css/style.css` or `static/js/main.js`, compile the changes using the custom Python minifier script before running the app:
```bash
python scripts/minify_css.py
```
This script will minify the code, generate the files inside the `staticfiles/` directory, and update the static cache.

---

## Completed Improvements

We have executed a comprehensive optimization and refactoring pass resolving several critical security, functionality, accessibility, and performance issues:

1. **Insecure Secret Key Fixed**: Replaced the hardcoded fallback `SECRET_KEY` in `config/settings.py` with strict environment variable parsing using python-decouple.
2. **Credential Safety**: Added `.env` to `.gitignore` and provided [.env.example](.env.example) to guide developer setup without risking credential exposure.
3. **Automated Booking Notifications**: Added integration with Django's core mail module in `bookings/views.py` to notify the company admin immediately upon new bookings. The implementation includes failure-tolerance to ensure SMTP issues do not block booking saves.
4. **Form Rate-Limiting**: Integrated a custom cache-based IP rate limiter (`core/utils.py`) to prevent automated spam and abuse on booking and review forms.
5. **Mobile & Tablet Responsiveness**: Added viewport breakpoints and navigation overlays to ensure the interactive hamburger menu, grid elements, and typography layout adapt beautifully to tablet screens (769px to 1024px) and mobile.
6. **Template Accessibility & W3C/A11y Fixes**:
   - Fixed navigation landmark accessibility by retaining proper `aria-expanded` and ID bindings.
   - Added semantic visually-hidden titles (`<h2 class="sr-only">`) to section components to help screen readers.
   - Cleared duplicate `aria-label` tags from submit buttons to prevent double-speech screen reader announcements.
7. **PWA Offline Mode & Caching**: Adjusted `service-worker.js` to point to the correct compiled minified static assets and fall back gracefully to the homepage caching buffer when offline.
8. **MVT & Database Integration**: Upgraded the static `service_type` choices in the Booking form into a dynamic database-driven dropdown loaded directly from active `Service` records.
9. **Eliminated Unused Files**: Removed temporary files (`temp_perf_check.py`, `test_output.txt`, Lighthouse reports) and legacy modules to keep the repository clean and maintainable.

---

## Future Database Normalization Recommendations

Due to local constraints, the database schemas were left intact to avoid schema migration conflicts. However, we strongly recommend performing the following migrations in future major releases to ensure data normalization and integrity:

1. **Normalize Vehicle Seats**:
   - **Current State**: `Vehicle.seats` is a string field (`CharField`).
   - **Recommended State**: Convert to a `PositiveIntegerField` to enforce numeric inputs and allow range queries (e.g. filter by minimum number of passenger seats).
2. **Normalize Vehicle Features**:
   - **Current State**: `Vehicle.features` is stored as a raw text string.
   - **Recommended State**: Create a new model `VehicleFeature(name=CharField)` and link it to the `Vehicle` model using a `ManyToManyField`. This enables standardized tagging, searching, and filtering of vehicles based on capabilities (e.g., AC, WiFi, Leather Seats).
3. **Establish Service Relationship**:
   - **Current State**: `Booking.service_type` is stored as a plain `CharField`.
   - **Recommended State**: Establish a `ForeignKey` relationship pointing directly to the `Service` model. This guarantees referential integrity, eliminates hardcoded strings, and automatically cascades changes when services are renamed or updated.

---

## Running Tests

The application features a test suite covering form validations, rate limiting, SMTP failure-tolerance, and dynamic database dropdown choice rendering.

To run tests in an isolated local database environment:
```bash
python manage.py test
```
Django will automatically set up a local in-memory SQLite3 database, execute all test modules under `bookings/tests.py`, and output results.
