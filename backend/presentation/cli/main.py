import argparse
import sys

from application.dependency_container import get_seeder_service

def create_parser() -> argparse.ArgumentParser:
    """Create and configure the argument parser."""
    parser = argparse.ArgumentParser(
        prog="opentax",
        description="OpenTax Backend CLI",
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Seed command
    seed_parser = subparsers.add_parser('seed', help='Seed the database with sample data')
    seed_parser.add_argument(
        '--payments', 
        type=int, 
        default=30, 
        help='Number of payments to create (default: 30)'
    )
    seed_parser.add_argument(
        '--invoices', 
        type=int, 
        default=30, 
        help='Number of invoices to create (default: 30)'
    )
    
    return parser


def handle_seed_command(args) -> int:
    """Handle the seed command."""
    try:
        print(f"Starting database seeding 🌱 ...")
        print(f"   Payments: {args.payments}")
        print(f"   Invoices: {args.invoices}")
        
        seeder_service = get_seeder_service()
        seeder_service.seed(num_payments=args.payments, num_invoices=args.invoices)
        
        print("Database seeding completed successfully!")
        return 0
        
    except Exception as e:
        print(f"Error during seeding: {e}", file=sys.stderr)
        return 1


def main() -> int:
    """Main CLI entry point."""
    parser = create_parser()
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return 1
    
    if args.command == 'seed':
        return handle_seed_command(args)
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
