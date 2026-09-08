# Kollegans första arbetsdag med teamet

## Var börjar jag?

Öppna en ny chatt i det befintliga Codex-projektet **Utvecklingsteam**. Beskriv
vem produkten hjälper, vilket problem den löser och vad du vill prova först.
Codex formulerar Issue och föreslår en liten leverans. Efter godkänt scope
förbereder Codex en bygguppgift med egen arbetskopia och reservation. Du provar
resultatet och ger feedback i bygguppgiften. Produktionsgodkännande ligger hos
en människa.

Du behöver inte skapa ett nytt projekt eller en undermapp för varje idé.
Innan produktkod byggs förbereder Codex rätt målrepo, separat arbetsyta och
teamets instruktioner där. Teamets repo innehåller arbetssättet,
inte alla produkters kod. Work är valfritt för research och affärsunderlag; kod hanteras
av Codex. Överlämna dokumenterade beslut och Issue, inte hela chatthistoriken.

## Vad behöver installeras?

| Behov | Krävs för vårt lokala arbetssätt? |
|---|---|
| Codex och ett konto med rätt tillgång | Ja. Kollegan loggar in själv. |
| Git och åtkomst till teamets och senare produktens GitHub-repo | Ja, för kloner, worktrees, reservationer och PR-flödet. |
| Python 3.12+ | Ja för just vårt reservationsverktyg; bundlad runtime går bra. |
| Node.js | Bara när valda verktyg eller JavaScript/TypeScript-kod behöver det. En Python-MCP kräver inte automatiskt Node.js. |
| Knowit PPT-skill och officiell mall | För alla PowerPoint-presentationer. Codex följer skillens brandregler och kör dess audit. |
| GitHub CLI | Rekommenderas för effektiv Issue/PR-automation; inloggad webbläsare kan användas. |
| PyYAML 6.0.3 | Endast för teamrepots utvecklingskontroller/CI, inte för reservationer. MIT-licens. |

Codex kontrollerar befintliga verktyg innan installation föreslås. Kollegan ska
inte behöva arbeta i terminalen. Konto-, företags- och administrationsgodkännanden
kan kräva kollegans eller IT:s medverkan. En ny appanslutning ger inte automatiskt
åtkomst till alla repos.

## Hur gör vi teamet tillgängligt?

1. Teamansvarig delar repo-länken, presentationen och [plan.md](../../plan.md).
   Varje kollega använder eget konto och godkänd åtkomst till Knowit-skillen.
2. Kollegan bifogar plan.md i en Codex-chatt. Codex återanvänder teamprojektet
   eller hjälper till att ansluta en egen lokal klon en gång. Därefter börjar
   varje idé som en ny chatt i samma teamprojekt. Ingen delad skrivmapp används.
3. Vid ny produkt inför Codex teamets AGENTS.md, relevanta agentinstruktioner,
   reservationsverktyget, mallar och anpassade kontroller. Produktens profil
   beskriver teknik, data och testkommandon. Detta sker via granskad ändring.
4. Teamansvarig godkänner produktens GitHub-skydd och granskarupplägg. Skydden
   är inställningar per repo och följer inte automatiskt med kopierade filer.
5. Kollegan kör en liten provuppgift via Codex innan större arbete startar.

Den konkreta startinstruktionen finns i [plan.md](../../plan.md). Codex utför
kontrollerna och redovisar vad som verifierats. Kollegan hjälper till med egen
inloggning, företagsgodkännande och att öppna den förberedda projektmappen om
Codex saknar appverktyg för det steget.

Kopiera aldrig någon annans personliga `.codex`-hemkatalog, credentials eller
API-nycklar. Personliga plugins/roller kan behöva konfigureras separat; en kopia
av repo-instruktionerna bevisar inte att alla lokala funktioner är aktiverade.

## Kostnad och fokus

Använd en liten tydlig uppgift per byggchatt. Läs bara relevanta filer, spara
beslut i repo/Issue och använd fler agenter när de har avgränsade deluppgifter.
Modellval prövas mot kvalitet och total förbrukning, inte enbart pris per token.

Källor kontrollerade 2026-09-08:
[Codex på Windows](https://learn.chatgpt.com/docs/windows/windows-app),
[Codex app](https://learn.chatgpt.com/docs/app),
[Projekt och chattar](https://learn.chatgpt.com/docs/projects).
