
from flask_app import app
from flask_app.controllers import owners, animals

if __name__ == "__main__":
    app.run(debug=True)


#Semi Restful routing
# GET render
# POST redirect
#owners-  
# /owners/new  GET renders the page
# /owners/create POST create a new owner in the database
# /owners/owner_id/edit GET renders the page with the form
# /owners/owner_id/update POST
# /owners/owner_id/delete GET renders the page with the form
# /owners/owner_id/destroy POST

# new vs create
# edit vs update
# delete vs destroy

# animals-  
# /animals/new  GET renders the page
# /animals/create POST create a new owner in the database
# /animals/animal_id/edit GET renders the page with the form
# /animals/animal_id/update POST
# /animals/animal_id/delete GET renders the page with the form
# /animals/animal_id/destroy POST

# procedures-  
# /procedures/new  GET renders the page
# /procedures/create POST create a new owner in the database
# /procedures/procedure_id/edit GET renders the page with the form
# /procedures/procedure_id/update POST
# /procedures/procedure_id/delete GET renders the page with the form
# /procedures/procedure_id/destroy POST