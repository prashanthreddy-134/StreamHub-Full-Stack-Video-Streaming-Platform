$ErrorActionPreference = 'Stop'
if (-not (Test-Path '.venv\Scripts\Activate.ps1')) { throw 'Virtual environment missing. Run .\setup.ps1 first.' }
& .\.venv\Scripts\Activate.ps1
# Use a separate local SQLite database for the automated test suite. The app's normal configuration remains MySQL.
$env:DB_ENGINE = 'sqlite'
python manage.py check
python manage.py test videos --verbosity 2
if ($LASTEXITCODE -ne 0) { throw 'Automated tests failed. Review the traceback above.' }
Remove-Item Env:DB_ENGINE -ErrorAction SilentlyContinue
Write-Host 'All automated Django tests passed.' -ForegroundColor Green
