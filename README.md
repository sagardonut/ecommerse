#### ⚠️Still Under Construction 👷‍♂️
# Django E-Commerce with Stripe Checkout

This project is a feature-rich **E-Commerce platform** built with **Django**. It includes a shopping cart system, Stripe payment gateway integration, and dynamic product management. The platform offers a seamless shopping experience with modern payment options like credit/debit cards, CashApp Pay, and more.

---

## Features

### 🛒 E-Commerce Functionalities
- Add, update, and remove items in the cart.
- Display total prices dynamically based on cart contents.
- Checkout multiple items using Stripe.

### 💳 Payment Integration
- Secure payment processing with Stripe Checkout.
- Supports multiple payment methods (Card, CashApp Pay, etc.).
- Automatically calculates total amount and handles Stripe payment sessions.

### 🖼️ Product Management
- Dynamic product creation via the admin panel.
- Support for product images, prices, and descriptions.
- Automatic Stripe product and price ID synchronization.

### 📦 Backend Features
- Modular and clean architecture using Django.
- Webhooks to confirm payment and update order status.
- Fully functional admin panel for product management.

### 🌍 Deployment Ready
- Compatible with tools like **ngrok** for local Stripe testing.
- Configurable environment variables for production.

---

## Tech Stack

- **Backend:** Django, Python
- **Frontend:** HTML, CSS
- **Payment Gateway:** Stripe API
- **Database:** SQLite (default, can be configured for PostgreSQL/MySQL)
- **Others:** ngrok for local HTTPS tunneling, pip for dependency management.

---

## Getting Started

Follow these steps to get the project running on your local machine.

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/django-ecommerce-stripe.git
cd ecommerse
```
### 2. set .env file & Create a stripe account and import the followings keys
```bash
STRIPE_PUBLICABLE_KEY =
STRIPE_SECRET_KEY =
STRIPE_WEBHOOK_SECRET =
```
### 3. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
### 4.  Run the Development Server
```bash
python manage.py runserver
```




