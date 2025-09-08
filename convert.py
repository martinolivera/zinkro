import argparse
from zinkro import ZinkroCalendar, SimpleDate
import os

parser = argparse.ArgumentParser(description="Conversor de fechas entre calendario gregoriano y Zinkro.")
parser.add_argument('--start', type=str, help="Fecha de inicio del calendario Zinkro (YYYY-MM-DD)")
subparsers = parser.add_subparsers(dest='command')

# Subcomando: gregorian_to_zinkro
g2z = subparsers.add_parser('g2z', help='Convierte fecha gregoriana a Zinkro')
g2z.add_argument('date', type=str, help='Fecha gregoriana (YYYY-MM-DD)')

# Subcomando: zinkro_to_gregorian
z2g = subparsers.add_parser('z2g', help='Convierte fecha Zinkro a gregoriana')
z2g.add_argument('year', type=int, help='Año Zinkro')
z2g.add_argument('month', type=int, nargs='?', help='Mes Zinkro (1-13, omitir para Día Zero)')
z2g.add_argument('day', type=int, nargs='?', help='Día Zinkro (1-28, omitir para Día Zero)')

args = parser.parse_args()

# Leer punto de inicio por defecto desde zinkro.conf si no se especifica --start
def get_default_start_date():
    conf_path = os.path.join(os.path.dirname(__file__), "zinkro.conf")
    try:
        with open(conf_path, "r") as f:
            for line in f:
                if line.startswith("START_DATE="):
                    return line.strip().split("=")[1]
    except Exception:
        pass
    return "2025-01-01"

if args.start:
    start_date_str = args.start
else:
    start_date_str = get_default_start_date()
start_date = SimpleDate.from_string(start_date_str)
cal = ZinkroCalendar(start_date=start_date)

if args.command == 'g2z':
    date = SimpleDate.from_string(args.date)
    year, month, day, dia_zero = cal.gregorian_to_zinkro(date)
    if dia_zero:
        print(f"{args.date} => Zinkro: Año {year}, Día Zero")
    else:
        print(f"{args.date} => Zinkro: Año {year}, Mes {month}, Día {day}")
elif args.command == 'z2g':
    year = args.year
    month = args.month if args.month is not None else None
    day = args.day if args.day is not None else None
    fecha = cal.zinkro_to_gregorian(year, month, day)
    if month is None:
        print(f"Zinkro: Año {year}, Día Zero => {fecha}")
    else:
        print(f"Zinkro: Año {year}, Mes {month}, Día {day} => {fecha}")
else:
    parser.print_help()
