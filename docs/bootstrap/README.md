# Bootstrap-checklista

Teamets repo-grund är incheckad. Följande steg görs i Codex- och GitHub-gränssnitten.

## Codex desktop

- Lägg till den lokala projektmappen som ett lokalt Codex-projekt.
- Välj Codex när chatten ska läsa eller ändra filer.
- Kontrollera att projektet använder `.codex/agents/`.
- Konfigurera lokal miljö och återanvändbara actions i Codex desktop.
- Använd worktree för bakgrundsarbete och parallella uppgifter.
- Använd `00 – Control Room` som huvudchatt för coachning och beslut.

## ChatGPT-projekt

Skapa eller använd ett projekt för Control Room och lägg in routingtexten från [`docs/chatflows/chat-routing.md`](../chatflows/chat-routing.md) i projektinstruktionerna. Detta gör arbetssättet konsekvent mellan chattarna. När en uppgift kräver filändringar ska den startas i det lokala Codex-projektet.

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

För att Control Room ska kunna skapa Issues direkt krävs en godkänd GitHub-anslutning med Issue-skrivbehörighet. Den bör exponera minsta möjliga operationer enligt [`docs/automation/issue-intake.md`](../automation/issue-intake.md).

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

