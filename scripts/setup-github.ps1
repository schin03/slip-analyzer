# One-time setup of labels, milestones, and Sprint 0 issues.
# Run from the repo root:  powershell -ExecutionPolicy Bypass -File scripts/setup-github.ps1
$repo = "schin03/slip-analyzer"

$labels = @(
  @("type: story","1D76DB","User-facing capability"),
  @("type: bug","D73A4A","Something is broken"),
  @("type: task","0E8A16","Technical/engineering work"),
  @("type: research","5319E7","Time-boxed investigation"),
  @("type: decision","FBCA04","Needs a recorded decision (ADR)"),
  @("area: backend","C5DEF5","FastAPI / Python"),
  @("area: frontend","C5DEF5","React / UI"),
  @("area: data","C5DEF5","Providers, ingestion, storage"),
  @("area: analytics","C5DEF5","Scoring and methodology"),
  @("area: docs","C5DEF5","Documentation"),
  @("area: infra","C5DEF5","CI, Docker, hosting"),
  @("blocked","B60205","Waiting on something external")
)
foreach ($l in $labels) {
  gh label create $l[0] --color $l[1] --description $l[2] --repo $repo --force | Out-Null
  Write-Host "label: $($l[0])"
}

$milestones = @(
  @("v0.1 Skeleton","Repo, tooling, CI, deployable skeleton"),
  @("v0.2 Mock Vertical Slice","Top Picks end to end on mock data"),
  @("v0.3 Live Data","Real odds and stats with caching"),
  @("v1.0 Public Beta","Pairings, tracking, polish, disclaimers")
)
foreach ($m in $milestones) {
  try { gh api "repos/$repo/milestones" -f title="$($m[0])" -f description="$($m[1])" | Out-Null; Write-Host "milestone: $($m[0])" }
  catch { Write-Host "milestone exists or failed: $($m[0])" }
}

function New-Issue($title, $body, $labels) {
  gh issue create --repo $repo --title $title --body $body --label $labels --milestone "v0.1 Skeleton" | Out-Null
  Write-Host "issue: $title"
}

New-Issue "Set up repo workflow: labels, milestones, templates" "Issue/PR templates, labels, milestones.`n`n**Acceptance**`n- [ ] Templates visible when opening a new issue/PR`n- [ ] Labels and milestones exist" "type: task,area: infra"
New-Issue "Write README, architecture doc, and initial ADRs" "README with disclaimers, ADRs 0001-0004, architecture stub.`n`n**Acceptance**`n- [ ] README explains purpose, disclaimers, stack`n- [ ] ADRs committed" "type: task,area: docs"
New-Issue "Backend skeleton: FastAPI /health, pytest, ruff" "**Acceptance**`n- [ ] GET /health returns status ok`n- [ ] One passing test`n- [ ] ruff passes" "type: task,area: backend"
New-Issue "OddsProvider interface and mock provider" "Define the provider abstraction and a mock implementation labeled with bookmaker, source, and timestamp.`n`n**Acceptance**`n- [ ] Interface documented`n- [ ] Mock returns sample NBA props`n- [ ] Unit test" "type: task,area: data"
New-Issue "PostgreSQL via Docker Compose and Alembic baseline" "**Acceptance**`n- [ ] docker compose up starts Postgres`n- [ ] Alembic baseline migration runs" "type: task,area: infra"
New-Issue "Frontend skeleton: dark shell and freshness chip" "**Acceptance**`n- [ ] Dark layout with header, source/freshness chip, disclaimer footer`n- [ ] Calls backend /health" "type: task,area: frontend"
New-Issue "CI: lint and test on pull requests" "**Acceptance**`n- [ ] GitHub Actions runs backend and frontend checks on PRs" "type: task,area: infra"
New-Issue "R-1: Verify The Odds API coverage and terms" "Get a free key, check which bookmakers/markets (esp. Bet365, NBA props) are returned, confirm free credit allowance, read terms.`n`n**Output**: update ADR-0002." "type: research,area: data"
New-Issue "R-2: Player stats and game-log data source options" "Compare options (nba_api, balldontlie, paid feeds) on terms, reliability, injuries/minutes availability.`n`n**Output**: options table and ADR." "type: research,area: data"
New-Issue "Deploy skeleton to free hosting" "Verify current free tiers for frontend, backend, and database, present options, then deploy." "type: task,area: infra"
