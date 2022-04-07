import logging

SEARCH = """
    WITH APT AS(
SELECT
	*
FROM
	appointment a NATURAL JOIN
    tutor t NATURAL JOIN
    client c NATURAL JOIN
    appointment transaction receipt r 
    

)
SELECT
	APT.appointment_date
    APT.appointment_time
    APT.appointment_duration
    APT.t_name
    APT.tutor_id
    APT.c_id
    APT.c_name
    APT.t_rating
    APT.c_rating
    APT.overall_rating
FROM 
	APT
WHERE
    {criteria} = {value}

"""

CRITERIA = {
    "supervisor_id": "{}",
    
}

  

def fetch_forsupervisor(args):
    query = SEARCH
    if 'supervisor_id' in args and len(args['supervisor_id']) > 0:
        query = query.format(criteria = "APT.supervisor_id", value = args["supervisor_id"])
    else :
        query = query.format(criteria = "1", value = "1")

    if 'limit' in args:
        query = query + " LIMIT 1"
    print(query)
    return query