def get_home_page():
    return """
    <form method="get" action="/search">
    <button type="submit">Search contact by Case id</button>
    </form>
    
    <form method="get" action="/contact/new">
        <button type="submit">Create new contact</button>
    </form>
    
    <form method="get" action="/search/update">
        <button type="submit">Update existing contact</button>
    </form>
    
    <form method="get" action="/contact/delete">
        <button type="submit">Delete existing contact</button>
    </form>
"""


def get_search_contact_form():
    return """              
        <form action="#" method="post">
            <label for="case_id">Case ID:</label><br>
            <input type="text" id="case_id" name="case_id" value=""><br>
            <button type="submit">Search</button>
        </form><br>
        <form method="get" action="/">
            <button type="submit">Back</button>
        </form>          
        """


def get_contact_info_page(case_id, title, first_name, last_name, mobile_number, address):
    return f"""
        <form method="get" action="/">
            <label />case_id: {case_id}<br>
            <label />title: {title}<br>
            <label />first_name: {first_name}<br>
            <label />last_name: {last_name}<br>
            <label />mobile_number: {mobile_number}<br>
            <label />address: {address}<br>
        </form>
        <br>
        <form method="get" action="/">
                    <button type="submit">Home</button>
                </form>
        """


def get_case_not_found_page():
    return """
        <p> The specified case does not exist.
        <br>
        <form method="get" action="/">
            <button type="submit">Home</button>
        </form>
        """


def get_case_already_exists_page():
    return f"""
            <p> The case_id already exists. Please try again with different data.
            <form method="get" action="/contact/new">
                <button type="submit">Back</button>
            </form>
            <br>
            <form method="get" action="/">
                <button type="submit">Home</button>
            </form>
            """


def get_created_successfully_page():
    return f"""
            <p> New contact created successfully!
            <form method="get" action="/">
                <button type="submit">Home</button>
            </form>
            """


def get_create_new_case_form():
    return f"""
                <p> Create new contact: <p><br><br>
                <form action="/contact/new" method="post">
                    <label for="case_id">Case ID:</label><br>
                    <input type="text" id="case_id" name="case_id" value=""><br>
                    
                    <label for="title">Title:</label><br>
                    <input type="text" id="title" name="title" value=""><br><br>
                    
                    <label for="first_name">First name:</label><br>
                    <input type="text" id="first_name" name="first_name" value=""><br><br>
    
                    <label for="last_name">Last name:</label><br>
                    <input type="text" id="last_name" name="last_name" value=""><br>
    
                    <label for="mobile_number">Mobile number:</label><br>
                    <input type="text" id="mobile_number" name="mobile_number" value=""><br><br>
    
                    <label for="address">Address</label><br>
                    <input type="text" id="address" name="address" value=""><br><br>
    
                    <input type="submit" value="Create new contact"><br><br>
                    </form>
                    
                 <form method="get" action="/">
                    <button type="submit">Back</button>
                </form>
                """


def get_deleted_successfully_page():
    return f"""
            <p>Contact deleted successfully!
            <form method="get" action="/">
                <button type="submit">Back</button>
            </form>
            """


def get_error_page(origin):
    return f"""
            <p> Something went wrong! Please try again.
            <form method="get" action="{origin}">
                <button type="submit">Back</button>
            </form>
            <form method="get" action="/">
                <button type="submit">Home</button>
            </form>
            """


def get_delete_case_form():
    return f"""
            <p> Delete Contact: <p><br><br>
            <form action="/contact/delete" method="post">
                <label for="case_id">Case ID:</label><br>
                <input type="text" id="case_id" name="case_id" value=""><br>
                <input type="submit" value="Delete contact"><br><br>
            </form>
            <form method="get" action="/">
                <button type="submit">Back</button>
            </form>
            """


def get_update_contact_form(case_id, title, first_name, last_name, mobile_number, address):
    return f"""
            <p> Update contact: <p>
            <form action="/case/update/{case_id}" method="post">
                <label for="case_id">Case ID:</label><br>
                <input type="text" id="case_id" name="case_id" value="{case_id}">
                <br><br>
    
                <label for="title">Title:</label><br>
                <input type="text" id="title" name="title" value="{title}">
                <br><br>
    
                <label for="first_name">First name:</label><br>
                <input type="text" id="first_name" name="first_name" value="{first_name}">
                <br><br>
    
                <label for="last_name">Last name:</label><br>
                <input type="text" id="last_name" name="last_name" value="{last_name}">
                <br><br>
    
                <label for="mobile_number">Mobile number:</label>
                <br><br>
                <input type="text" id="mobile_number" name="mobile_number" 
                value="{mobile_number}">
                <br><br>
    
                <label for="address">Address</label><br>
                <input type="text" id="address" name="address" value="{address}">
                <br><br>
                <input type="submit" value="Update contact"><br>
    
                </form>
             <form method="get" action="/">
                <button type="submit">Back</button>
            </form>
                     """


def get_contact_already_exists(case_id):
    return f"""
                        <p> The case_id already exists. Please try again with different data.
                        <form method="get" action="/case/update/{case_id}">
                            <button type="submit">Back</button>
                        </form>
                        <form method="get" action="/">
                            <button type="submit">Home</button>
                        </form>
                        """


def get_updated_successfully():
    return f"""
            <p> Contact updated successfully!
            <form method="get" action="/">
                <button type="submit">Home</button>
            </form>
            """


def get_search_case_to_update_page():
    return """
        <p>Search case to be updated </p>              
        <form action="#" method="post">
            <label for="case_id">Case ID:</label><br>
            <input type="text" id="case_id" name="case_id" value=""><br>
            <button type="submit">Search</button>
        </form>
        <br>
        <form method="get" action="/">
            <button type="submit">Back</button>
        </form>          
        """