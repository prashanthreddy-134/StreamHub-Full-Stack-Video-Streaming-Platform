$ErrorActionPreference = 'Stop'
Write-Host '=== StreamHub setup ===' -ForegroundColor Cyan
if (-not (Get-Command python -ErrorAction SilentlyContinue)) { throw 'Python was not found. Install Python 3.11 and enable Add Python to PATH.' }
python --version
if (-not (Test-Path '.venv')) { python -m venv .venv }
& .\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
if (-not (Test-Path '.env')) {
  Copy-Item '.env.example' '.env'
  Write-Host 'Created .env from .env.example. Edit DB_PASSWORD and SECRET_KEY before continuing.' -ForegroundColor Yellow
  notepad .env
  Read-Host 'Save and close .env, then press Enter'
}
Write-Host 'Checking Django configuration...' -ForegroundColor Cyan
python manage.py check
Write-Host 'If MySQL is running and credentials in .env are correct, migrations will now be created and applied.' -ForegroundColor Cyan
python manage.py makemigrations videos
python manage.py migrate
Write-Host 'Create your administrator account:' -ForegroundColor Cyan
python manage.py createsuperuser
Write-Host 'Setup complete. Run .\run.ps1 to start StreamHub.' -ForegroundColor Green
