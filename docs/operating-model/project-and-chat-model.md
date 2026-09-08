# Projekt- och chattmodell

Det här dokumentet beskriver hur teamet använder Codex utan att blanda ihop projekt, chattar och agentroller.

## Grundmodell

### Ett Codex-projekt

Ett lokalt Codex-projekt motsvarar normalt ett repo eller en sammanhållen kodbas. Projektet ger chattarna en gemensam arbetsmapp, projektkonfiguration och beständiga instruktioner.

I det här repo:t är `UTVECKLINGSTEAMS` ett sådant projekt. Det innehåller teamets operativsystem, inte produktkod.

Skapa inte ett nytt lokalt projekt bara för att få en ny chatt eller en ny agentroll. Det leder till parallella projektdefinitioner och gör sidofältet svårtolkat.

### En Codex-chatt

En chatt är en fokuserad arbetsström i projektet. Skapa en ny chatt när utfallet eller ansvaret ändras, till exempel:

- discovery av en idé
- arkitektur för ett Issue
- implementation av ett Issue
- felsökning av ett avgränsat problem
- review av en Pull Request
- releaseförberedelse

Chattarna ska ligga i det projekt som äger repot. En chatt är inte ett nytt projekt.

## Beständig kontext

En ny chatt ska kunna börja utan att användaren kopierar hela historiken från en annan chatt. Därför har teamet flera nivåer av beständig kontext:

1. `AGENTS.md` innehåller regler, guardrails och agentgränser.
2. `PROJECT_PROFILE.md` innehåller projektets identitet, mål och teknikprofil.
3. `docs/` innehåller arbetsmodell, beslut och integrationsregler.
4. GitHub Issues innehåller krav, scope, acceptanskriterier och status.
5. ADR:er innehåller större arkitekturbeslut.
6. Pull Requests innehåller ändringar, verifiering och kvarvarande risker.
7. Chattens historik innehåller det pågående resonemanget för just den arbetsströmmen.

Projektet delar projektfiler och instruktioner mellan sina chattar, men en ny chatt ska inte förutsättas känna till hela meddelandehistoriken från andra chattar. Viktiga beslut ska därför skrivas till rätt beständig källa.

## Teamets rekommenderade struktur

### Nu: färdigställ teamet

Använd en enda aktuell setup-chatt i projektet `UTVECKLINGSTEAMS`. Den kan fortsätta heta `Sätt upp agnostiskt utvecklingsteam`.

En särskild `00 – Control Room` behövs inte nu. Den är bara en valfri koordineringschatt om antalet parallella arbetsströmmar senare gör nästa steg svårt att se.

### Senare: arbete i teamets repo

När teamets egna dokument eller konfiguration ska ändras skapas fokuserade chattar i samma projekt, exempelvis:

- `Agentroller och guardrails`
- `GitHub och Codex-automation`
- `Issue-intake`
- `Security och human gates`
- `Review av teamkonfiguration`

### Framtida produktrepo

När en produkt får en egen kodbas, mapp eller GitHub-repository får den ett eget Codex-projekt. Då kopieras eller genereras teamets återanvändbara arbetsmodell till produktrepo:t genom dess `AGENTS.md`, `PROJECT_PROFILE.md` och `.codex/`.

Produktens discovery-, architecture-, build-, review- och releasechattar ligger sedan i produktens projekt.

## Codex först

Teamet kräver inte vanlig ChatGPT-chatt. Codex är den primära arbetsytan för:

- coachning och kravförtydligande
- planering och Issue-förberedelse
- filändringar och dokumentation
- testning och verifiering
- agentdelegation
- Pull Requests och releaseunderlag

Välj körläge efter risk och isolering:

- `Local` för läsning och kontrollerad lokal utveckling
- `Worktree` för isolerade ändringar och parallellt arbete
- `Cloud` när arbetet ska köras i en konfigurerad fjärrmiljö

Vanlig ChatGPT-chatt är valfri för fristående arbete som inte behöver repo- eller teamkontext. Den är inte en obligatorisk del av utvecklingsflödet.
