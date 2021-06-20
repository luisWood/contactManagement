from flask import Flask, request, redirect, url_for
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import HtmlUtils

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/contact_management"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class ContactCardModel(db.Model):
    __tablename__ = 'contact_cards'

    case_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    mobile_number = db.Column(db.String())
    address = db.Column(db.String())

    def __init__(self, case_id, title, first_name, last_name, mobile_number, address):
        self.case_id = case_id
        self.title = title
        self.first_name = first_name
        self.last_name = last_name
        self.mobile_number = mobile_number
        self.address = address

    def __repr__(self):
        return f"<Contact card {self.name}>"


@app.route('/')
def hello():
    return HtmlUtils.get_home_page()


@app.route("/search", methods=["GET", "POST"])
def search_contact():
    if request.method == "GET":
        return HtmlUtils.get_search_contact_form()
    elif request.method == "POST":
        case_id = request.form["case_id"]
        return redirect(url_for("get_case_contact_info", case_id=case_id))


@app.route('/contacts/<case_id>', methods=['GET'])
def get_case_contact_info(case_id):
    try:
        contact_card = ContactCardModel.query.get_or_404(case_id)
        return HtmlUtils.get_contact_info_page(
            contact_card.case_id,
            contact_card.title,
            contact_card.first_name,
            contact_card.last_name,
            contact_card.mobile_number,
            contact_card.address
        )
    except:
        return HtmlUtils.get_case_not_found_page()


@app.route('/contact/new', methods=['POST', 'GET'])
def create_new_contact():
    if request.method == 'POST':
        new_contact_card = ContactCardModel(
            case_id=request.form['case_id'],
            title=request.form['title'],
            first_name=request.form['first_name'],
            last_name=request.form['last_name'],
            mobile_number=request.form['mobile_number'],
            address=request.form['address'],
        )

        if ContactCardModel.query.filter_by(case_id=new_contact_card.case_id).first() is not None:
            return HtmlUtils.get_case_already_exists_page()

        try:
            db.session.add(new_contact_card)
            db.session.commit()

            return HtmlUtils.get_created_successfully_page()
        except:
            return HtmlUtils.get_error_page('/contact/new')
    elif request.method == "GET":
        return HtmlUtils.get_create_new_case_form()


@app.route('/search/update', methods=['GET', 'POST'])
def search_case_to_update():
    if request.method == "GET":
        return HtmlUtils.get_search_case_to_update_page()
    elif request.method == "POST":
        case_id = request.form["case_id"]
        return redirect(url_for("update_contact", case_id=case_id))


@app.route('/case/update/<case_id>', methods=['GET', 'POST'])
def update_contact(case_id):
    temp_contract_card = ContactCardModel.query.filter_by(case_id=case_id).first()

    if request.method == 'POST':
        new_contact_card = ContactCardModel(
            case_id=request.form['case_id'],
            title=request.form['title'],
            first_name=request.form['first_name'],
            last_name=request.form['last_name'],
            mobile_number=request.form['mobile_number'],
            address=request.form['address'],
        )

        try:
            # db.session.add(new_contact_card)
            db.session.query(ContactCardModel).filter(ContactCardModel.case_id == case_id).update({
                ContactCardModel.case_id: new_contact_card.case_id,
                ContactCardModel.title: new_contact_card.title,
                ContactCardModel.first_name: new_contact_card.first_name,
                ContactCardModel.last_name: new_contact_card.last_name,
                ContactCardModel.mobile_number: new_contact_card.mobile_number,
                ContactCardModel.address: new_contact_card.address,
            })
            db.session.commit()
            return HtmlUtils.get_updated_successfully()
        except:
            return HtmlUtils.get_error_page(f"/case/update/{request.form['case_id']}")

    elif request.method == "GET":
        return HtmlUtils.get_update_contact_form(
            temp_contract_card.case_id,
            temp_contract_card.title,
            temp_contract_card.first_name,
            temp_contract_card.last_name,
            temp_contract_card.mobile_number,
            temp_contract_card.address)


@app.route('/contact/delete', methods=['GET', 'POST'])
def delete_contact():
    if request.method == 'POST':
        case_id = request.form['case_id']
        try:
            contact_card = ContactCardModel.query.filter_by(case_id=case_id).first()
            db.session.delete(contact_card)
            db.session.commit()
            return HtmlUtils.get_deleted_successfully_page()
        except:
            return HtmlUtils.get_error_page('/contact/delete')
    elif request.method == "GET":
        return HtmlUtils.get_delete_case_form()


if __name__ == '__main__':
    app.run(debug=True)
