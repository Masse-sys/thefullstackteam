# Verifiering av parallellt byggarbete

Datum: 2026-09-08. Issue: [#1](https://github.com/Masse-sys/thefullstackteam/issues/1).

## Genomförda GitHub-prov

Två separata temporära kloner och Git-processer synkroniserades före första
pushen mot `refs/heads/codex/coordination-pilot-20260908` i detta repo.
Numren 900001/900002 är uttryckligen syntetiska prov-ID:n, inte verkliga Issues.

| Prov | Resultat |
|---|---|
| Samma uppgift, olika paths | Exakt en bokning accepterades, exit 2 och 0. |
| Olika uppgifter, åtskilda paths | Båda bokningarna accepterades, exit 0 och 0. |
| Release från rätt session/arbetskopia | Lyckades för samtliga bokningar. |
| Slutligt tillstånd | Tom journal, version 1. |

Fjärrcommit efter prov:
[`379ca8f5b60b47ff9c7081bfee1800c3181f06d1`](https://github.com/Masse-sys/thefullstackteam/commit/379ca8f5b60b47ff9c7081bfee1800c3181f06d1).

Provets reservationer: `e33cd66b677f45efb947e35a14a8533c`,
`61486f6eb8b1420d802cc8972af24a23`, `8e34cc18c5ac497584cc1b1f873fee5a`.
Inga main-pushar, force-pushar eller raderingar användes i provet.

## Lokala integrationstester

`python -m unittest discover -s tests -v` kör riktiga Git-processer mot en
temporär bare remote, med separata kloner och synkroniserade samtidiga pushes.
Testerna omfattar samma uppgift, katalogöverlapp, delad resurs, åtskilda områden,
fel session/arbetskopia, release/återbokning, scopeöverskridande, namnbyte,
okänd/trasig journal, offline samt förlorat pushkvitto. Ett kombinationsprov
visar också att två var för sig fungerande ändringar kan ge beteendefel efter
en textmässigt konfliktfri sammanslagning.

Det första Windows-provet hittade ett CRLF-fel vid konstruktion av Git-trädet.
NUL-avgränsning rättade felet. Journalen reparerades med fast-forward commit
utan att den befintliga reservationen förlorades. Python 3.12+ krävs för att
även kunna avvisa Windows-junctions.

## Granskningsresultat och begränsningar

En separat QA-agent granskade algoritmen read-only och utförde GitHub-provet.
Inget blockerande CAS-fel hittades. Kompatibilitetsfyndet om Python åtgärdades.

Detta verifierar samtidiga processer mot riktig GitHub med samma autentisering.
Det verifierar inte två kollegors separata konton eller datorinstallationer.
`check` är en aktuell nettodiffskontroll, inte ett OS-skrivlås. Medvetet kringgående
och manipulation av journalen ligger utanför skyddet. En kraschad ägares bokning
ligger kvar och kräver kontrollerad återhämtning. Delade resurser mellan repos
och oberoende mänsklig granskare måste fortfarande konfigureras.

Main-skydden är sparade: PR, obligatorisk aktuell kontroll, ingen bypass,
ingen force-push eller radering.

## Negativt PR-prov mot GitHub

På PR #2 lades ett avsiktligt underkänt test i en separat provcommit
`09fc5feed1dacf8c9fda6949ef8d14cca2a6ee90`. GitHub körde den obligatoriska
kontrollen och rapporterade failure:
[körning 34224912704](https://github.com/Masse-sys/thefullstackteam/actions/runs/34224912704).
PR-sidan visade kontrollen som Required och knappen Merge pull request som
inaktiverad, även för repots ägare. Detta observerades före rättningen.

Provfilen är därefter borttagen. Slutlig CI kontrolleras på den nya committen
och redovisas i [PR #2](https://github.com/Masse-sys/thefullstackteam/pull/2).
De tolv ordinarie lokala integrationstesterna och konfigurationskontrollen
passerade före provfilen lades till.
