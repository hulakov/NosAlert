import os
import sys

# Ensure root directory is in sys.path for relative imports when running directly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Load environment variables from .env file
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

from cli.parser import parse_args
from cli.alerts_service import check_active_alerts, check_alerts_history


def main():
    """CLI entry point for NosAlert."""
    args = parse_args()

    api_token = os.getenv("ALERTS_TOKEN", "YOUR_API_TOKEN_HERE")

    if api_token == "YOUR_API_TOKEN_HERE":
        print("\n⚠️  ЗВЕРНІТЬ УВАГУ:")
        print("Вкажіть ваш справжній API-токен у файлі .env")
        print("Відкрийте файл .env та вкажіть: ALERTS_TOKEN=ваш_справжній_токен\n")
        sys.exit(1)

    if args.history:
        check_alerts_history(api_token, location=args.location, period=args.period, limit=args.limit, verbose=args.verbose)
    else:
        check_active_alerts(api_token, location=args.location, verbose=args.verbose)


if __name__ == "__main__":
    main()
