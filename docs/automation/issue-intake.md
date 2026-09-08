# Idé till GitHub Issue

## Mål

Varje användaridé ska snabbt bli spårbar och användbar för teamet utan att användaren behöver skriva en teknisk specifikation.

## Standardbeteende

När användaren beskriver en ny idé ska Product Planner:

1. sammanfatta problemet och den önskade effekten
2. ställa endast frågor som påverkar scope, risk, data, kostnad eller arkitektur
3. skapa ett Issue-utkast så snart det finns tillräckligt med information
4. fylla i alla kända fält och markera antaganden tydligt
5. sätta labels `draft` och `needs-discovery`
6. inte starta implementation ännu

När användaren godkänner scope får Issue:t `ready-for-build`. Den etiketten är den enda normala signalen för att byggflödet får starta.

`ready-for-build` betyder godkänt scope, inte att uppgiften är reserverad.
Före skrivning krävs bekräftad reservation enligt
[parallellt byggarbete](../operating-model/parallel-builds.md). Issue:t ska ange
ansvarig person, huvudagent/bygguppgift, unik branch, skrivområden, resurser och
beroenden. Absoluta lokala sökvägar med personuppgifter ska inte publiceras.

## Issue-innehåll

Varje Issue ska, när informationen finns, innehålla:

- kort och konkret titel
- problem och användarvärde
- målgrupp och primärt användningsfall
- föreslagen lösning på rätt abstraktionsnivå
- acceptanskriterier
- out-of-scope
- öppna frågor och antaganden
- tekniska begränsningar och beroenden
- data-, privacy- och säkerhetsaspekter
- kostnads- och driftpåverkan
- föreslagen agentordning
- definition of done
- länk till relaterad chatt eller ADR

## Integration

Issue-skapandet ska använda en godkänd GitHub-integration eller ett projektbegränsat MCP-verktyg med minsta möjliga behörighet. Verktyget bör ha separata operationer för:

- `create_issue_draft`
- `update_issue_draft`
- `add_issue_labels`
- `mark_ready_for_build`
- `link_issue_to_pull_request`

Det ska inte finnas en automatisk delete-operation i idéflödet. Merge och produktion ska vara separata, mänskligt skyddade operationer.

## Kvalitetsregel

Ett fullständigt Issue är inte samma sak som ett färdigt beslut. Om en fråga kan påverka personuppgifter, säkerhet, arkitektur, produktion eller kostnad ska den stå kvar som en explicit beslutspunkt.

