from webapp.user.decorator import admin_required

from flask import Blueprint,render_template

blueprint = Blueprint('admins',__name__, url_prefix='/admins')

@blueprint.route('/admin')
@admin_required
def admin_1():
    title = "Admin panel"
    return render_template("admin/index.html",title = title)
