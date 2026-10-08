# Calendario di pubblicazione

Type: grilling
Status: resolved

## Question

Come si pubblicano i capitoli nel tempo? Opzioni emerse:
- tutti con la data del giorno in cui sono scritti, pubblicati al push;
- uno a settimana con date future. Hugo non pubblica un post con data futura finché non
  avviene una nuova build: serve un workflow schedulato (cron) che ricostruisca il sito, oppure
  push manuali alla data giusta.

Decidere la cadenza e, se servono date future, come garantire la build alla data.

## Answer

Resolved 2026-10-08 (decisione utente).
- Cadenza: settimanale, di martedì.
- Tutti i capitoli retrodatati in settimane passate, serie che termina il martedì scorso (2026-10-06).
- Niente date future, niente cron: la build la fa uno script esterno (fuori scope).
- Date: 00=2026-07-21, 01=2026-07-28, 02=2026-08-04, 03=2026-08-11, 04=2026-08-18,
  05=2026-08-25, 06=2026-09-01, 07=2026-09-08, 08=2026-09-15, 09=2026-09-22,
  10=2026-09-29, 11=2026-10-06. Ora 09:00+02:00, `lastmod` = `date`.
