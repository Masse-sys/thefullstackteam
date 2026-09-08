# Bootstrap-checklista

Teamets repo-grund är incheckad. Följande steg görs i Codex- och GitHub-gränssnitten.

## Codex desktop

- Lägg till den lokala projektmappen som ett lokalt Codex-projekt.
- Använd Codex som teamets primära arbetsyta för både planering och implementation.
- Kontrollera att projektet använder `.codex/agents/`.
- Konfigurera lokal miljö och återanvändbara actions i Codex desktop.
- Använd worktree för bakgrundsarbete och parallella uppgifter.
- Skapa nya arbetschattar inifrån samma Codex-projekt; skapa inte ett nytt lokalt projekt för varje chatt.
- Använd en särskild Control Room endast om teamets koordinering senare kräver det.

## Projektgränser

- `UTVECKLINGSTEAMS` är projektet för teamets operativsystem och ska inte innehålla produktkod.
- Ett framtida produktrepo får ett eget lokalt Codex-projekt när det har en egen kodbas, mapp eller GitHub-repository.
- Teamets arbetssätt ska då återanvändas genom produktrepots `AGENTS.md`, `PROJECT_PROFILE.md` och `.codex/`-konfiguration, inte genom att blanda flera repos i samma projekt.

## GitHub

- Kontrollera att `main` pekar på den första bootstrap-committen.
- Skydda `main` så att merge kräver Pull Request.
- Kräv att CI passerar innan merge.
- Kräv CODEOWNERS-granskning.
- Stäng av force-push och radering av `main`.
- Skapa labels: `draft`, `needs-discovery`, `ready-for-build`, `blocked`, `security` och `risk-high`.
- Anslut repot till Codex Cloud.
- Aktivera automatisk Code Review och Security Review enligt teamets åtkomstnivå.

Codex kan därefter arbeta från GitHub Issues och Pull Requests, och skriva tillbaka resultat till en branch eller Pull Request.

## Issue-automation

För att idéflödet ska kunna skapa Issues direkt krävs en godkänd GitHub-anslutning med Issue-skrivbehörighet. Den bör exponera minsta möjliga operationer enligt [`docs/automation/issue-intake.md`](../automation/issue-intake.md).

Standard är:

```text
idé → draft Issue → discovery → ready-for-build → Codex Build-chatt
```

Issue-skapandet får vara automatiskt. Byggstart, merge och produktion ska ha separata kontrollpunkter.

## Kontroll före första produktfeature

- [ ] GitHub-anslutning för Issue-skapande är aktiv
- [ ] Codex Cloud når repot
- [ ] `main` är skyddad
- [ ] första automatiska Code Review är verifierad
- [ ] första draft Issue är skapad och komplett
- [ ] första byggchatt har körts i worktree
