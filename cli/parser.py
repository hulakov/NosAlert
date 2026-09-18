import argparse


def parse_args():
    """Configures and parses command-line arguments for the NosAlert CLI."""
    parser = argparse.ArgumentParser(
        description="NosAlert CLI — Check active air raid alerts and historical alert data in Ukraine."
    )
    parser.add_argument(
        "-l", "--location",
        type=str,
        default="м. Київ",
        help="Location title or UID (default: 'м. Київ' / UID: 31)"
    )
    parser.add_argument(
        "-H", "--history",
        action="store_true",
        help="Fetch historical alert data instead of current active alerts"
    )
    parser.add_argument(
        "-p", "--period",
        type=str,
        default="month_ago",
        help="Period for alert history (default: month_ago)"
    )
    parser.add_argument(
        "-n", "--limit",
        type=int,
        default=10,
        help="Number of history records to display (default: 10)"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose output (prints all raw API requests and responses)"
    )

    return parser.parse_args()
