# Codex project configuration

Den här mappen innehåller projektets delade Codex-konfiguration.

- `config.toml` innehåller gemensamma agentinställningar.
- `agents/` innehåller projektets custom agents.
- lokal miljö, setup och actions konfigureras från Codex desktop och ska delas via repo när konfigurationen är stabil.

## Så används projektet

- `UTVECKLINGSTEAMS` är ett lokalt Codex-projekt, inte en produktkodbas.
- Skapa flera chattar i samma projekt för setup, discovery, arkitektur, implementation, test och review.
- Skapa inte ett nytt lokalt projekt bara för att få en ny arbetschatt.
- Använd worktree för ändringar som ska kunna köras parallellt eller granskas isolerat.
- Lägg beständiga beslut i `AGENTS.md`, `PROJECT_PROFILE.md`, `docs/`, GitHub Issues och Pull Requests.
- All kod- och dokumentationsändring ska göras av Codex eller delegerade agenter.

Ändra inte agentregler för att kringgå en säkerhets- eller kvalitetskontroll. Uppdatera i stället reglerna med tydlig motivering och lägg till verifiering i CI när det går.
