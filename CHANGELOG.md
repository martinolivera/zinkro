# CHANGELOG - Zinkro Calendar

All notable changes to this project will be documented in this file.

## v1.0.1 - March 20, 2026: Critical Logic Fixes

### Fixed
- **Day Zero year calculation**: Day Zero (March 20) now returns the current year (Y+10000) instead of (0, None, None, True)
- **Year transition logic**: Year changes ON Day Zero, not after. Dates before March 20 now correctly belong to the previous year
- **Leap year Day 366**: Added special "Day 366" for the day before Day Zero in leap years (March 19)
- **Visual grid hover tooltips**: Fixed date display in grid tooltips (now uses March 20 as reference, not March 21)

### Changed
- `gregorian_to_zinkro()` algorithm completely rewritten for correct date mapping
- Updated 11 unit tests with correct expected values
- Variable naming: `gregStart` → `gregZeroDay` for clarity

### Test Results
```
11/11 tests passing ✓
- test_leap_year_feb_29 ✓
- test_leap_year_march_1 ✓
- test_leap_year_march_19 ✓
- test_leap_year_march_19_special_day ✓ (NEW)
- test_leap_year_march_20_day_zero ✓
- test_leap_year_march_21 ✓
- test_normal_year_march_1 ✓
- test_normal_year_march_19 ✓
- test_normal_year_march_20 ✓
- test_normal_year_march_20_day_zero ✓
- test_normal_year_march_21 ✓
```

### Example: 2028 (Leap Year)
```
Feb 28, 2028 → (12027, 13, 9)           # Previous year
Feb 29, 2028 → (12027, 13, 10)          # Leap day
Mar 1, 2028  → (12027, 13, 11)          # Previous year
Mar 18, 2028 → (12027, 13, 28)          # Last day of month 13
Mar 19, 2028 → (12027, 13, 366)         # Special pre-Day Zero day
Mar 20, 2028 → (12028, None, None, True) # ← YEAR CHANGES HERE!
Mar 21, 2028 → (12028, 1, 1)            # First day of year
```

---

## v1.0.0 - March 20, 2026: Initial Release

### Added
- Complete Zinkro calendar implementation (13 months × 28 days + 1 Day Zero)
- Bidirectional conversion: Gregorian ↔ Zinkro
- Holocene Era support (year = Gregorian year + 10000)
- Bilingual web interface (Spanish/English)
- Interactive visual calendar grid
- Command-line conversion tool (`convert.py`)
- Full leap year support
- Comprehensive unit test suite

### Features
- **Calendar Structure**: 13 months of 28 days each + 1 Day Zero (March 20)
- **Year Zero**: Represents the spring equinox as a day outside of time
- **Leap Years**: Standard Gregorian leap year rules with proper day handling
- **Era Alignment**: Synchronized with spring equinox, not arbitrary date

### Files
- `zinkro.py` - Core calendar logic
- `convert.py` - CLI tool
- `views/` - Web interface (6 HTML files, bilingual)
- `tests/` - Unit tests
- `views/zinkro.js` - Frontend conversion logic

### Known Limitations
- Web interface limited to year range 2026-2100
- Mobile responsiveness can be improved
- No timezone support (assumes UTC/local time)

---

## Version History

| Version | Date | Status | Notes |
|---------|------|--------|-------|
| 1.0.1 | Mar 20, 2026 | Stable | Critical logic fixes |
| 1.0.0 | Mar 20, 2026 | Stable | Initial release |

---

## Semantic Versioning

This project follows [Semantic Versioning](https://semver.org/):
- **MAJOR**: Breaking changes to calendar logic
- **MINOR**: New features (new languages, new tools, etc.)
- **PATCH**: Bug fixes and improvements

---

**Current Version**: 1.0.1  
**Last Updated**: March 20, 2026  
**Maintained by**: Zinkro Project
