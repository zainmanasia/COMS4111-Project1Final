# COMS4111-Project1Final (Tutoring Service Management System)
Mohiuddin Alamgir mma 2204 <br/>
 Zain Manasia zm2401
  
   Postgres Server Details:
    username: zm2401
     password: 3459
      
       The parts that were implemented in this project were a system to query all the clients and their prefereneces present in the database, all the tutors present in the database, the supervisor and information on the tutors associated with a specific supervisor, and a way to query for all the appointments associated with either an appointment ID, client ID, or tutor ID. This aligns with what we had proposed in Part I, and we were able to implement all of the features we had hoped for. This website serves as a management system for existing client, tutors, and supervisors, so the functionality on that front was covered. 
        
         We have a webpage that allows users to look up a specific appointment that was conducted through searching with either the appointment ID, client ID, or tutor ID. We designed it to be such so that this site can be used by both the tutor and client, and two seperate sites for each wouldnt be needed. We achieved this by using natural joins on some of the entity sets and were able to use this to output data that would benefit both parties. We also used the client's preferences as an indicator of which tutors would be best suited for them, but also vice versa. So, on the tutor page, the tutor is asked questions such as their preferred gender to tutor, their preferred teaching medium, and their preferred vaccination status of the client, but this data was not collected from the tutor. Instead, we decided to use the client's preferences and the tutor's inputs during search to find a client-tutor combination that would be best compatible. 
 
