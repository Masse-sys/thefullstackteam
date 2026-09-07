# AI-native operating model

## Grundsyn

Teamet ska använda AI som en del av hela utvecklingssystemet: från idé och research till implementation, test, säkerhet, dokumentation och uppföljning.

## Arbetssätt

- små vertikala leveranser i stället för stora ospecificerade projekt
- krav och acceptanskriterier före implementation
- kontrakt först för API:er, events och MCP
- tester och evals nära implementationen
- parallell research och review, sekventiellt skrivande på konfliktkänsliga filer
- varje ändring ska vara spårbar till ett Issue
- CI är den deterministiska kvalitetsgrinden
- agentgranskning är ett extra lager, inte en ersättning för tester eller mänskligt ansvar
- återkommande feedback förs tillbaka till `AGENTS.md`, agentinstruktioner eller återanvändbara skills

## Definition of Ready och Done

Se [`AGENTS.md`](../../AGENTS.md). Alla nya produktrepo ska ärva samma principer men beskriva sin egen teknikprofil i `PROJECT_PROFILE.md`.

