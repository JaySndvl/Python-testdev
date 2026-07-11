param(
    [Parameter(Position = 0)]
    [string]$Message = "Update project files"
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$changes = git status --porcelain
if (-not $changes) {
    Write-Host "No changes to commit."
    exit 0
}

git add -A

git commit -m $Message
git push
