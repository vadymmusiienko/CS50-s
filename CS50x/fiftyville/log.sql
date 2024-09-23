-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Find the crime scene report
SELECT * FROM crime_scene_reports WHERE street = 'Humphrey Street' AND day = 28 AND month = 7;
-- The crime happened at 10:15 am, 3 interviews present at the time

-- Find 3 interviews from the crime scene
SELECT name, transcript FROM interviews WHERE day = 28 AND month = 7;
-- (Ruth) got into a car at the bakery, look for the cars at the bakery at that time (within ten minutes of the theft)
-- (Eugene) recognized the thief, he was at ATM on Leggett Street earlier that morining (withdrawing)
-- (Raymond)The thief called someone as leaving the bakery (less than 1 minute call), he is taking the earliest flight out of Fiftyville tomorrow (ACCOMPLICE bought the ticket)

-- Check cars leaving the bakery at the time of the crime
SELECT license_plate FROM bakery_security_logs WHERE day = 28 AND month = 7 AND hour = 10 AND minute <= 25 AND activity = 'exit';
-- Suspect's licence plate: 5P2BI95, 94KL13X, 6P58WS2, 4328GD8, G412CB7, L93JTIZ, 322W7JE, 0NTHK55

-- Check ATM transactions in the morning of of the crime
SELECT account_number FROM atm_transactions WHERE month = 7 AND day = 28 AND atm_location = 'Leggett Street' AND transaction_type = 'withdraw';
-- Account number - withdraw amount: 28500762 - 48, 28296815 - 20, 76054385 - 60, 49610011 - 50, 16153065 - 80, 25506511 - 20, 81061156 - 30, 26013199 - 35

-- Check the phone calls (1 minute) around 10:15
SELECT caller FROM phone_calls WHERE month = 7 AND day = 28 AND duration < 60;

-- Find who was withdrawing money (person id)
SELECT person_id FROM bank_accounts WHERE account_number IN (SELECT account_number FROM atm_transactions WHERE month = 7 AND day = 28 AND atm_location = 'Leggett Street' AND transaction_type = 'withdraw');

-- Find id of the airport in Fiftyville
SELECT id FROM airports WHERE city = 'Fiftyville';

-- Find the flights' id of the first flight from Fiftyville in the morning of 29th.
SELECT id FROM flights WHERE month = 7 AND day = 29 AND origin_airport_id = (SELECT id FROM airports WHERE city = 'Fiftyville') ORDER BY hour, minute LIMIT 1;

-- Find out the passport numbers of our suspects
SELECT passport_number FROM passengers WHERE flight_id IN (SELECT id FROM flights WHERE month = 7 AND day = 29 AND origin_airport_id = (SELECT id FROM airports WHERE city = 'Fiftyville') ORDER BY hour, minute LIMIT 1);


-- Find the thief
SELECT name FROM people WHERE
phone_number IN (SELECT caller FROM phone_calls WHERE month = 7 AND day = 28 AND duration < 60)
AND license_plate IN
(SELECT license_plate FROM bakery_security_logs WHERE day = 28 AND month = 7 AND hour = 10 AND minute < 30 AND activity = 'exit')
AND id IN
(SELECT person_id FROM bank_accounts WHERE account_number IN (SELECT account_number FROM atm_transactions WHERE month = 7 AND day = 28 AND atm_location = 'Leggett Street' AND transaction_type = 'withdraw'))
AND passport_number IN
(SELECT passport_number FROM passengers WHERE flight_id IN (SELECT id FROM flights WHERE month = 7 AND day = 29 AND origin_airport_id = (SELECT id FROM airports WHERE city = 'Fiftyville') ORDER BY hour, minute LIMIT 1));
-- Bruce is the thief

-- Find the accomplies' phone number
SELECT receiver FROM phone_calls WHERE caller = (SELECT phone_number FROM people WHERE name = 'Bruce') AND month = 7 AND day = 28 AND duration < 60;

-- Find the accomplies
SELECT name FROM people WHERE phone_number = (SELECT receiver FROM phone_calls WHERE caller = (SELECT phone_number FROM people WHERE name = 'Bruce') AND month = 7 AND day = 28 AND duration < 60);
-- Robin is the accomplies

-- Find the city the thief escaped to
SELECT city FROM airports WHERE id = (SELECT destination_airport_id FROM flights WHERE month = 7 AND day = 29 AND origin_airport_id = (SELECT id FROM airports WHERE city = 'Fiftyville') ORDER BY hour, minute LIMIT 1);
-- the thief escaped to New York City
