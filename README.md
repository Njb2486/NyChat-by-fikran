# NyChat by FGNIL — Starter Project

**Tagline:** Meet Anyone, Anywhere in the World.

This starter provides the first backend foundation for NyChat. It is a development scaffold, not a finished or production-ready application.

## Included
- Django project scaffold
- Django REST Framework
- Custom user model using email as the login identifier
- Basic registration and profile endpoints
- Environment-variable example
- GitHub Actions basic checks
- Flutter/mobile and web implementation roadmap

## Requirements
- Python 3.11+
- PostgreSQL for deployment (SQLite is the default for local quick-start)
- Git

## Run locally
1. Create a virtual environment:
   `python -m venv .venv`
2. Activate it.
3. Install dependencies:
   `pip install -r requirements.txt`
4. Copy `.env.example` to `.env` and update values.
5. Run migrations:
   `python manage.py makemigrations accounts`
   `python manage.py migrate`
6. Create an admin:
   `python manage.py createsuperuser`
7. Start the server:
   `python manage.py runserver`

Admin: `/admin/`
API health: `/api/health/`
Register: `POST /api/auth/register/`
Profile: `GET /api/auth/profile/` (requires authentication)

## Important security notes
- This is an initial development scaffold. Do not deploy it publicly as-is.
- Configure a strong `SECRET_KEY`, `DEBUG=False`, `ALLOWED_HOSTS`, HTTPS, secure cookies, rate limits, logging, backups, and a production database before deployment.
- Email/phone OTP, 2FA, payments, wallets, WebRTC, and AI actions are not implemented by this starter.
- Do not store real money balances as a simple editable number. Production wallet transactions require a ledger, idempotency, reconciliation, provider approval, and security review.
