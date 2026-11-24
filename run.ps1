$ErrorActionPreference = 'Stop'
if (-not (Test-Path '.venv\Scripts\Activate.ps1')) { throw 'Virtual environment missing. Run .\setup.ps1 first.' }
& .\.venv\Scripts\Activate.ps1
python manage.py check
python manage.py runserver
