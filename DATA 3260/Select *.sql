Select * 
FROM    Conference


SELECT *
FROM    DIVISION

SELECT      C.ConferenceID,
            C.ConferenceName,
            D.DivisionName
FROM        Conference C
INNER JOIN  Division D ON C.ConferenceID = D.ConferenceID

-- Write the SQL to combine (JOIN) Team and Player Data

SELECT * FROM Team T
SELECT * FROM Player P
SELECT      T.TeamID,
            T.TeamName,
            P.PlayerID,
            P.LastName,
            P.FirstName
FROM        Team T
INNER JOIN  Player P ON T.TeamID = P.TeamID


SELECT      t.TeamName,
            Count(*)
FROM        Team T
INNER JOIN  Player P ON T.TeamID = P.TeamID
GROUP BY    T.TeamName


SELECT      *
FROM        Team T
INNER JOIN  Player P ON T.TeamID = P.TeamID

 -- Generate a count of divisions within each conference... 
SELECT      C.ConferenceName,
            Count(*) AS DivisionCount
FROM        Conference C
INNER JOIN  Division D ON C.ConferenceID = D.ConferenceID
GROUP BY    C.ConferenceName

--  7.4.B Get a count of the records in each table.
SELECT      'Conference' AS TableName,
            Count(*) AS RecordCount
FROM        Conference
UNION ALL
SELECT      'Division' AS TableName,
            Count(*) AS RecordCount
FROM        Division
UNION ALL
SELECT      'Team' AS TableName,
            Count(*) AS RecordCount
FROM        Team

SELECT    * 
From Student

    Insert Into Student (FirstName, LastName, CourseNumber, Section)
    Values ('William', 'Millar', 'Data3260', 02)

-- 7.4.C Return conference and division data together using an INNER JOIN
SELECT      C.ConferenceName,
            D.DivisionName
FROM        Conference C
INNER JOIN  Division D ON C.ConferenceID = D.ConferenceID

-- 7.4.D Return conference, division and team data together.
SELECT      C.ConferenceName,
            D.DivisionName,
            T.TeamName
FROM        Conference C
INNER JOIN  Division D ON C.ConferenceID = D.ConferenceID
INNER JOIN  Team T ON D.DivisionID = T.DivisionID

-- 7.4.E Return Team and Player data together so each player is listed on a team
SELECT      T.TeamName,
            P.LastName,
            P.FirstName
FROM        Team T
INNER JOIN  Player P ON T.TeamID = P.TeamID
