# Manjari Taxi

> A premium, highly-structured Django-based Cab Booking platform featuring modular CSS architecture, vehicle fleet management, automated asset minification, and clean directory separation.

## 📁 Clean Architecture Layout

The codebase is structured into four primary isolated folders to maximize readability and maintainability:

*   **`frontend/`**: The presentation layer.
    *   `src/`: Contains raw source code templates (HTML), stylesheets (CSS), and client scripts (JS).
    *   `assets/`: Dedicated folder for static assets (images, logs, custom scripts) and dynamic user-uploaded media.
    *   `scripts/`: Python utility scripts for minification and image compression (converting JPEG/PNG to responsive WebP format).
*   **`backend/`**: The Django application engine.
    *   `manage.py`: Django administration command-line utility.
    *   `src/config/`: App configuration (routing, ASGI/WSGI gateway setups, settings).
    *   `src/core/` & `src/bookings/`: App controllers, routing rules, forms, context processors, and custom template tags.
*   **`database/`**: Single source of truth for schemas and migrations.
    *   `models/`: Domain models separated by concerns (`core` models like Service/Vehicle/Review and `bookings` models).
    *   `migrations/`: Database schema version history.
    *   `clean_db.py`: Standalone Python script to sanitize database values (e.g., non-numeric seats cleanup).
*   **`tests/`**: Contains the full automated test suite separated from business logic.

---

## 🚀 Key Features

*   🚖 **Active Fleet & Service Management**: Dynamically list cabs with customizable features (e.g., AC, luggage space) and seat categories.
*   📅 **Dynamic Rides Booking Engine**: Dynamic forms, validations, and fare calculations.
*   🗺️ **SEO Route Landing Pages**: Dynamic rendering of landing pages targeting passenger routes.
*   ⚡ **Asset Optimization**: Built-in scripts to minify CSS/JS files and dynamically convert/resize images to responsive WebP sizes.
*   🧹 **Database Sanitization**: Clean migrations structure and independent database maintenance script.

---

## 🛠️ Quick Start

1. **Setup Environment**:
   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Run Migrations**:
   ```bash
   python backend/manage.py migrate
   ```

3. **Start the Development Server**:
   ```bash
   python backend/manage.py runserver
   ```

4. **Run Tests**:
   ```bash
   python backend/manage.py test
   ```
