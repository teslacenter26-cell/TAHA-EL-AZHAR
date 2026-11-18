-- Une ligne par réussite. Horodatages normalisés à la seconde UTC.
SELECT s.id, s.compte, s.ip, s.instant AS reussite_utc, COUNT(*) AS echecs
FROM evenements AS s
JOIN evenements AS e ON e.compte = s.compte AND e.ip = s.ip
WHERE s.resultat = 'succes' AND e.resultat = 'echec'
  AND CAST(strftime('%s', e.instant) AS INTEGER) >= CAST(strftime('%s', s.instant) AS INTEGER) - 600
  AND CAST(strftime('%s', e.instant) AS INTEGER) < CAST(strftime('%s', s.instant) AS INTEGER)
GROUP BY s.id, s.compte, s.ip, s.instant
HAVING COUNT(*) >= 5
ORDER BY s.instant, s.id;
