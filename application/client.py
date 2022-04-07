import logging

SEARCH = """
    WITH APT AS(
SELECT
	*
FROM
	tutor t 

)
SELECT
	APT.tutor_id
    APT.t_name
    APT.t_email
    APT.t_location
    APT.t_gender
    APT.overall_rating
    APT.t_vaxstatus
FROM 
	APT
WHERE
    {criteria} = {value}

"""

CRITERIA = {
    "tutor_id": "{}",
    "t_name": "{}",
    "t_location": "{}",
    "t_gender": "{}",
    "t_VaxStatus": "{}",
    

}

  

def fetch_tutor(args):
    query = SEARCH
    if 'tutor_id' in args and len(args['tutor_id']) > 0:
        query = query.format(criteria = "APT.tutor_id", value = args["tutor_id"])
    elif 't_name' in args and len(args['t_name']) > 0:
        query = query.format(criteria = "APT.t_name", value = args["t_name"])
    elif 't_location' in args and len(args['t_location']) > 0:
        query = query.format(criteria = "APT.t_location", value = args["t_location"])
    elif 't_gender' in args and len(args['t_gender']) > 0:
        query = query.format(criteria = "APT.t_gender", value = args["t_gender"])
    elif 't_VaxStatus' in args and len(args['t_VaxStatus']) > 0:
        query = query.format(criteria = "APT.t_vaxstatus", value = args["t_VaxStatus"])
    else :
        query = query.format(criteria = "1", value = "1")

    if 'limit' in args:
        query = query + " LIMIT 1"
    print(query)
    return query