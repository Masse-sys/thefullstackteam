# The Fullstack Team — Codex operating instructions

## Uppdrag

Detta repo är ett Codex-baserat utvecklingsteams operativsystem. Det är inte en produktapplikation och ska inte fyllas med påhittad produktkod. Alla filer, regler, arbetsflöden och framtida implementationer ska göra teamet snabbare, säkrare och mer återanvändbart.

All implementation och dokumentation skrivs av Codex eller delegerade Codex-agenter. Användaren ska inte behöva arbeta i terminalen.

## Arbetsmodell

1. Förstå önskat utfall och definition of done.
2. Om det gäller en ny idé: skapa eller uppdatera ett GitHub Issue-utkast innan implementation.
3. Ställ bara frågor som påverkar produkt, risk, arkitektur, data eller kostnad.
4. Skriv en kort plan och identifiera berörda områden.
5. Använd worktree och separat branch för ändringar.
6. Delegera läsintensiv research, testanalys och granskning när det ger verklig nytta.
7. Undvik parallella skrivagenter på samma filer. En agent ska vara huvudansvarig för varje skrivyta.
8. Kör relevanta valideringar innan Pull Request.
9. Sammanfatta ändringar, tester, kvarvarande risker och eventuella mänskliga beslut.

## Projekt- och chattmodell

- Detta repo används som ett lokalt Codex-projekt för teamets operativsystem.
- Ett projekt motsvarar normalt ett repo eller en sammanhållen kodbas.
- Flera chattar får och bör ligga i samma projekt när de behöver samma instruktioner, filer och beslutskontext.
- Skapa inte ett nytt lokalt projekt bara för att skapa en ny chatt eller agentroll.
- En ny idé, feature, felsökning eller review får en egen chatt i det projekt som äger arbetet.
- Projektets filer, Issues, ADR:er och Pull Requests är den beständiga kontexten. En ny chatt ska inte förutsättas känna till hela historiken från andra chattar.

## Routing mellan chattar

- Allt arbete kan utföras i Codex. Vanlig ChatGPT-chatt är valfri och krävs inte för detta team.
- Produktidé, research, prioritering och beslut hör hemma i en Discovery- eller planeringschatt i rätt Codex-projekt.
- Filändringar, tester, brancher och Pull Requests hör hemma i en bygg-, test- eller reviewchatt i rätt Codex-projekt.
- En särskild Control Room-chatt är valfri och ska bara skapas om koordineringen annars blir svår att överblicka.
- Arkitektur och ADR:er ska skrivas innan större implementationer.
- Varje konkret feature ska ha en egen byggchatt och ett eget Issue.
- Om information saknas för att bygga säkert: stanna och fråga användaren.

## Agentgränser

- Product Planner äger problemformulering, scope och acceptanskriterier.
- Architect äger tekniska beslut och ADR:er, men implementerar inte lösningen utan uttryckligt uppdrag.
- Implementer äger tilldelade kodändringar och ska inte ändra orelaterade områden.
- Data/Integration äger datakontrakt, migrationer och externa integrationer inom tilldelad scope.
- QA äger teststrategi, testfall, fixtures och verifieringsresultat.
- Security Reviewer arbetar read-only och ändrar inte kod för att dölja eller kringgå fynd.
- Release äger CI/CD- och releaseförberedelser, men får inte själv godkänna produktion.

## Hårda regler

- Skriv aldrig direkt till `main`.
- Skapa aldrig en produktionsrelease utan mänskligt godkännande.
- Ändra inte secrets, IAM, autentisering, behörigheter eller destruktiva migrationer utan mänsklig kontrollpunkt.
- Lägg aldrig riktiga personuppgifter, CV:n, ljudfiler eller API-nycklar i repo, fixtures eller loggar.
- Lägg inte in nya produktionsberoenden utan att dokumentera varför, licens och påverkan.
- Ändra inte arkitekturkontrakt utan ADR eller uppdaterad designanteckning.
- CI, branch protection och CODEOWNERS är kontrollmekanismer; agentinstruktioner ersätter dem inte.

## Definition of Ready

En uppgift är redo när den har:

- tydligt problem och önskat resultat
- användare eller målgrupp
- acceptanskriterier
- kända begränsningar
- risk- och dataklassning
- föreslagen scope och vad som inte ingår
- identifierad mänsklig beslutspunkt, om sådan finns

## Definition of Done

En uppgift är klar när:

- implementationen är begränsad till avtalad scope
- tester eller verifiering är tillagda och körda
- dokumentation och ADR är uppdaterade vid behov
- säkerhets- och datagränser är verifierade
- CI passerar
- Pull Request har begriplig sammanfattning
- öppna risker och mänskliga beslut är tydligt markerade

## Reservation vid parallellt byggarbete

Följ [parallellt byggarbete](docs/operating-model/parallel-builds.md).
Varje bygguppgift måste före skrivning ha egen worktree och unik branch samt
en bekräftad reservation från `tools/coordinate.py` i repots gemensamma journal.
På annan dator får en separat klon användas med unik branch. Kontrollera aktiv
reservation och scope före skrivpass och PR. Vid STOP eller nätverksfel pausas
berört skrivarbete. En etikett eller ledig chatt ersätter inte reservationen.
Reservera både filer och delade resurser. Ingen automatisk timeout/övertagning.
Behåll reservationen genom granskning och rättningar; släpp när arbetet avslutas.
Alla byggagenter ska använda samma journal, inte en per person.

## Delegation av deluppgifter

Använd subagents för parallell, avgränsad och huvudsakligen läsintensiv analys. Ge varje agent ett konkret uppdrag, tillåtna filer, förväntat resultat och rapportformat. Vänta in resultat innan en skrivagent integrerar ändringar.
