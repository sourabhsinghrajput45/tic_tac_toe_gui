param([switch]$Loop)

$ProjectPath = $PWD.Path
Set-Location $ProjectPath
$LogFile = Join-Path $ProjectPath "run_log.txt"
$ErrorActionPreference = "Continue"

function Log($Msg, $Color="Gray") {
    $ts = (Get-Date).ToString("yyyy-MM-dd HH:mm:ss")
    $line = "[$ts] $Msg"
    Write-Host $line -ForegroundColor $Color
    Add-Content -Path $LogFile -Value $line
}

function Pause-End {
    Write-Host ""
    Write-Host "Press ENTER to close..." -ForegroundColor Yellow
    [void](Read-Host)
}

Log "---------------------------------------------" "DarkGray"
Log "Project path: $ProjectPath" "Cyan"

# --- Python check ---
if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Log "Python not found. Please install Python 3.11+." "Red"
    Pause-End; exit 1
}
Log "Python detected: $(python --version)" "Green"

# --- uv check ---
if (-not (Get-Command uv -ErrorAction SilentlyContinue)) {
    Log "Installing uv..." "Yellow"
    pip install uv -q | Out-Null
    if (-not (Get-Command uv -ErrorAction SilentlyContinue)) {
        Log "uv installation failed." "Red"
        Pause-End; exit 1
    }
}
Log "uv ready." "Green"

# --- Sync dependencies ---
Log "Running 'uv sync'..." "Yellow"
try {
    uv sync | Tee-Object -FilePath $LogFile -Append
    Log "Dependencies synced successfully." "Green"
} catch {
    Log "Dependency sync failed: $($_.Exception.Message)" "Red"
    Pause-End; exit 1
}

# --- Run game ---
try {
    if ($Loop) {
        while ($true) {
            Log "Launching Tic-Tac-Toe (loop mode)..." "Cyan"
            uv run python tic_tac_toe.py | Tee-Object -FilePath $LogFile -Append
            Log "Restarting in 5 seconds..." "DarkYellow"
            Start-Sleep -Seconds 5
        }
    } else {
        Log "Launching Tic-Tac-Toe..." "Cyan"
        uv run python tic_tac_toe.py | Tee-Object -FilePath $LogFile -Append
        Log "Game closed normally." "Green"
    }
}
catch {
    Log "Runtime error: $($_.Exception.Message)" "Red"
}

Log "Script finished." "DarkGray"
Pause-End
