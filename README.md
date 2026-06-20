# AC073-VANUR Data Entry System

Web application to enter **Part Number**, **BLO Name**, **BLO Designation**, and **BLO Mobile Number** into SQL Server, view reports, and export to Excel (`.xlsx`).

## Prerequisites

1. **SQL Server** (Express or full edition) installed and running
2. **ODBC Driver 17 for SQL Server** — [Download from Microsoft](https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server)
3. **Python 3.10+**

## Setup

### 1. Create the database

Open **SQL Server Management Studio (SSMS)** and run:

```
database/schema.sql
```

Or run from command line:

```powershell
sqlcmd -S localhost\SQLEXPRESS -E -i database\schema.sql
```

### 2. Configure connection

Copy the example env file and edit your SQL Server settings:

```powershell
copy .env.example .env
```

Edit `.env`:

| Setting | Description |
|---------|-------------|
| `DB_SERVER` | e.g. `localhost\SQLEXPRESS` or `.\SQLEXPRESS` |
| `DB_NAME` | `AC073_VANUR` |
| `USE_WINDOWS_AUTH` | `true` for Windows login, `false` for SQL login |
| `DB_USER` / `DB_PASSWORD` | Only if using SQL Server authentication |

### 3. Install Python packages

```powershell
cd C:\Users\delld\OneDrive\Desktop\data
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 4. Run the application

```powershell
python app.py
```

Open in browser: **http://127.0.0.1:5000**

### 5. Production / domain deployment

For a **public domain** (e.g. `https://yourdomain.com`), use the production server:

```powershell
python run_production.py
```

Default port is **8080**. Set in `.env`:

```
HOST=0.0.0.0
PORT=8080
```

#### Option A — Windows Server + IIS (recommended for your own domain)

1. Install **Python 3.10+** and **HttpPlatformHandler** for IIS
2. Point your domain DNS **A record** to your server IP
3. Create an IIS site bound to your domain (port 80/443)
4. Set the site physical path to this project folder
5. Add a `web.config` that runs `run_production.py` via HttpPlatformHandler
6. Open Windows Firewall for port 8080 (or the port you choose)

#### Option B — Cloud VPS (Azure, AWS, DigitalOcean)

1. Deploy this folder to the VPS
2. Install Python, SQL Server (or use Azure SQL)
3. Run `python run_production.py` behind **nginx** or **Caddy** as reverse proxy
4. Point your domain to the VPS IP and enable HTTPS (Let's Encrypt)

#### Option C — Quick test on a domain (tunnel)

Use **ngrok** or **Cloudflare Tunnel** to expose local port 5000/8080 to a public URL without opening firewall ports.

```powershell
ngrok http 8080
```

## Mobile usage

The app is optimized for phones and tablets:

- **Bottom navigation** on mobile (Entry / Report)
- **Touch-friendly** buttons and inputs (48px minimum tap size)
- **Card layout** on mobile for the report (easier to read than a wide table)
- **Tap to call** BLO mobile numbers from the report
- **Safe area support** for notched phones (iPhone, etc.)

### Access from your phone (same Wi-Fi)

1. Start the app: `python app.py`
2. Find your PC IP address:

```powershell
ipconfig
```

Look for **IPv4 Address** (e.g. `192.168.1.105`).

3. On your phone browser, open:

```
http://YOUR_PC_IP:5000
```

Example: `http://192.168.1.105:5000`

> **Note:** Windows Firewall may ask to allow Python — click **Allow** so your phone can connect.

## Features

| Page | Description |
|------|-------------|
| **Data Entry** | Form with Part Number, BLO Name, BLO Designation, BLO Mobile Number (HTML + JavaScript) |
| **Report** | View all saved records from SQL Server |
| **Export .xlsx** | Download report as Excel file |
| **Mobile** | Responsive layout, bottom nav, tap-to-call |

## Project structure

```
data/
├── app.py              # Flask application
├── config.py           # Database connection settings
├── models.py           # SQLAlchemy model
├── requirements.txt
├── database/
│   └── schema.sql      # SQL Server table script
├── templates/
│   ├── index.html      # Data entry form
│   └── report.html     # Report + export
└── static/
    ├── style.css
    └── app.js           # Client-side validation & save
```
