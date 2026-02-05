# Josh's Board - Bus Arrivals at 1st Ave & 34th St

## Overview
Bus arrivals display for M15 and M34 routes, mounted on a south wall.

## Stop Configuration
| Stop ID | Route | Direction | Arrow |
|---------|-------|-----------|-------|
| 403359 | M34-SBS | Westbound → Javits | → |
| 403480 | M15 | Northbound (uptown via 1st Ave) | ↓ |
| 405610 | M15 | Southbound (downtown via 2nd Ave) | ↑ |

## Arrow Icons (South Wall Mounting)
Arrows oriented for viewer facing north:
- **→ right** (tile 40): M34 westbound to Javits/Hudson Yards
- **↓ down** (tile 38): M15 uptown (going away from viewer)
- **↑ up** (tile 39): M15 downtown (coming toward viewer)

## Route Variants
All variants show the same directional arrow:
- **M15, M15+, M15-SBS** → ↑ or ↓ based on direction
- **M34-SBS, M34+, M34A-SBS** → →

## Known Issues
- **AQI not showing**: IQAir API key expired. Update `secrets.py` with valid key.

## Deploying Updates
1. Connect board via USB-C
2. Mount appears at `/Volumes/CIRCUITPY`
3. Copy files:
   - `code.py` → `/Volumes/CIRCUITPY/code.py`
   - `mta_sheet.bmp` → `/Volumes/CIRCUITPY/img/mta_sheet.bmp`
   - Fill `secrets_template.py` → `/Volumes/CIRCUITPY/secrets.py`

## WiFi
Board connects to WiFi configured in `secrets.py`. If WiFi drops, display shows "WiFi LOST" in red.
