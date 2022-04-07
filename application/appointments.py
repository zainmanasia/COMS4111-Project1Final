import logging

SEARCH = """
    WITH APT AS(
SELECT
	*
FROM
	appointment a NATURAL JOIN
    tutor t NATURAL JOIN
    client c NATURAL JOIN
    preferences p 

)
SELECT
	APT.appointment_date
    APT.appointment_time
    APT.appointment_duration
    APT.t_name
    APT.tutor_id
    APT.c_id
    APT.c_name
FROM 
	APT
WHERE
    {criteria} = {value}

"""

CRITERIA = {
    "appointment_id": "{}",
    "tutor_id": "{}",
    "client_id": "{}"
}

  

def fetch_appointments(args):
    query = SEARCH
    if 'appointment_id' in args and len(args['appointment_id']) > 0:
        query = query.format(criteria = "APT.appointment_id", value = args["appointment_id"])
    elif 'tutor_id' in args and len(args['tutor_id']) > 0:
        query = query.format(criteria = "APT.tutor_id", value = args["tutor_id"])
    elif 'client_id' in args and len(args['client_id']) > 0:
        query = query.format(criteria = "APT.c_id", value = args["client_id"])
    else :
        query = query.format(criteria = "1", value = "1")

    if 'limit' in args:
        query = query + " LIMIT 1"
    print(query)
    return query