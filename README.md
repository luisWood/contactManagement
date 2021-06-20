# Contact management
## Description
The goal of this application is to manage contacts.

##### Implemented features
- Search for existing contacts by Id;
- Create new contacts;
- Delete existing contacts;
- Update existing contacts;

##### High priority future implementations:
Not yet implemented due to time constraints
- JWT based authentication & login module
- Audit Logging

##### Nice to haves:
- Better UI - a proper frontend module would greatly improve the user experience.

### Requirements
- python3
- pip3
- postgresql

### Python Setup
> pip3 install -r requirements.txt

### DB Setup
##### Implemented features

```sh
CREATE DATABASE contact_management
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.UTF-8'
    LC_CTYPE = 'en_US.UTF-8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

CREATE TABLE IF NOT EXISTS public.contact_cards
(
    case_id integer NOT NULL,
    title text COLLATE pg_catalog."default",
    first_name text COLLATE pg_catalog."default",
    last_name text COLLATE pg_catalog."default",
    mobile_number bigint,
    address text COLLATE pg_catalog."default",
    CONSTRAINT contact_cards_pkey PRIMARY KEY (case_id)
)
```
### Run application
> flask run

