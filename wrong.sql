SELECT CONCAT(e.FIRST_NAME, ' ', e.LAST_NAME) AS 'Nama',
       12 * e.salary "Annual Salary (12x Salary)"
       SUM(b.BONUS_AMOUNT) AS "Total Bonus"
       ((12 * e.salary)+(SUM(b.BONUS_AMOUNT)) AS "Total Paid 2016"
FROM Worker e,
     Bonus b,
ON e.WORKER_ID = b.WORKER_REF_ID
WHERE e.department = 'Admin' and 'Account';
