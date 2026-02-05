# Arrivals Board - Agent Instructions

## Device Connection
- **Device**: MatrixPortal S3
- **Mount Point**: `/Volumes/CIRCUITPY`
- **Serial Port**: `/dev/cu.usbmodem47D4DBA24C4D1`
- **Baud Rate**: 115200

## Reading Serial Logs
Use the venv with pyserial:
```bash
source .venv/bin/activate
python3 -c "
import serial, time
ser = serial.Serial('/dev/cu.usbmodem47D4DBA24C4D1', 115200, timeout=1)
start = time.time()
while time.time() - start < 15:
    if ser.in_waiting:
        print(ser.read(ser.in_waiting).decode('utf-8', errors='replace'), end='')
    time.sleep(0.1)
ser.close()
"
```

## Board Configurations

### Main Board (Keeton's - subway)
- Located in `nyc-MTA/`
- Uses subway station IDs and train lines
- Icons: Subway line bullets (A, C, E, 1, 2, 3, etc.)

### Josh's Board (buses at 1st Ave & 34th St)
- Located in `josh-board/`
- **Stop IDs**:
  - `403359` - M34-SBS Westbound (→ Javits)
  - `403480` - M15 Northbound (↓ uptown)
  - `405610` - M15 Southbound (↑ downtown)
- **Direction Icons** (for south wall mounting):
  - Tile 38: ↓ down arrow (N/uptown - going away)
  - Tile 39: ↑ up arrow (S/downtown - coming toward)
  - Tile 40: → right arrow (W/westbound to Javits)

## Backend API
- **URL**: `https://KeetonMartin.pythonanywhere.com`
- **Endpoints**:
  - `/api/mta-arrivals` - Subway arrivals
  - `/api/mta-bus-arrivals` - Bus arrivals
- **Known Issue**: Bus endpoint currently only returns M34+ data, not M15

## Deploying to a Board
1. Copy `code.py` to `/Volumes/CIRCUITPY/code.py`
2. Copy `img/mta_sheet.bmp` to `/Volumes/CIRCUITPY/img/mta_sheet.bmp`
3. Fill in `secrets_template.py` and copy as `/Volumes/CIRCUITPY/secrets.py`
