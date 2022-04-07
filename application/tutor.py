import logging

SEARCH = """
    WITH APT AS(
SELECT
	*
FROM
    client c NATURAL JOIN
    preferences p NATURAL JOIN
    provides v 


)
SELECT
	APT.c_id
    APT.c_name
    APT.c_email
    APT.c_location
    APT.c_gender
    APT.c_Vaxstatus
    APT.p_id
    APT.p_days_available
    APT.p_times_available
    APT.p_gender_preference
    APT.p_in_person_preference
    APT.p_vaxstatus_preference
FROM 
	APT
WHERE
    {criteria} = {value}
ORDER BY APT.consult_from DESC
"""

CRITERIA = {
    "c_gender": "{}",
    "c_location": "{}",
    "c_daysavailable": "{}",
    "c_timesavailable": "{}",
    "c_genderpreference": "{}",
    "c_inpersonpreference": "{}",
    "c_vaxstatuspreference": "{}"
}

  

def fetch_client(args):
    query = SEARCH
    if 'c_gender' in args and len(args['c_gender']) > 0:
        query = query.format(criteria = "APT.c_gender", value = args["c_gender"])
    elif 'c_location' in args and len(args['c_location']) > 0:
        query = query.format(criteria = "APT.c_location", value = args["c_location"])
    elif 'c_daysavailable' in args and len(args['c_daysavailable']) > 0:
        query = query.format(criteria = "APT.p_days_available", value = args["c_daysavailable"])
    elif 'c_timesavailable' in args and len(args['c_timesavailable']) > 0:
        query = query.format(criteria = "APT.p_times_available", value = args["c_timesavailable"])
    elif 'c_genderpreference' in args and len(args['c_genderpreference']) > 0:
        query = query.format(criteria = "APT.p_gender_preference", value = args["c_genderpreference"])
    elif 'c_inpersonpreference' in args and len(args['c_inpersonpreference']) > 0:
        query = query.format(criteria = "APT.p_in_person_preference", value = args["c_inpersonpreference"])
    elif 'c_vaxstatuspreference' in args and len(args['c_vaxstatuspreference']) > 0:
        query = query.format(criteria = "APT.p_vaxstatus_preference", value = args["c_vaxstatuspreference"])
    else :
        query = query.format(criteria = "1", value = "1")

    if 'limit' in args:
        query = query + " LIMIT 1"
    print(query)
    return query